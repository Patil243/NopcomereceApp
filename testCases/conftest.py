import undetected_chromedriver as uc
import pytest

@pytest.fixture(scope="function")   # <= important: function-level isolation
def setup(browser):
    if browser == 'Chrome':
        options = uc.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-insecure-localhost')
        driver = uc.Chrome(options=options)
        driver.maximize_window()
        print("Launching Chrome Browser........")
    elif browser == 'Firefox':
        options = uc.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-insecure-localhost')
        driver = uc.Firefox(options=options)
        driver.maximize_window()
        print("Launching Firefox Browser........")
    else:
        options = uc.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-insecure-localhost')
        driver = uc.Chrome(options=options)
        driver.maximize_window()
        print("Launching Chrome Browser........")

    yield driver  # <== Important: use yield instead of return

    driver.quit()  # <== close browser after test ends


def pytest_addoption(parser):               #This Will Get Value from CLI/Hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                       # this will return he browser value to HTML Report
    return request.config.getoption("--browser")

############################# Pytest HTML Report #############################
#Run his command in cli to generate html report
#pytest -v -s -n=2 --html=Report\report.html E:\Python_Project\NopcomereceApp\testCases\test_login.py --browser Chrome

def pytest_configure(config):
    # Nothing special needed here now
    pass

def pytest_metadata(metadata):
    metadata['Project Name'] = 'Nop Commerce'
    metadata['Module Name'] = 'Login'
    metadata['Tester'] = 'Patil Nitin'
    return metadata