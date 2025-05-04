import random
import pytest
import time
import string
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen
from pageObjects.addCustomerPage import AddCustomer
from selenium.webdriver.common.by import By

class Test_003_AddCustomer:  # Fixed Typo here

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_addcustomer(self, setup):
        self.logger.info("************ Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.logger.info("************ Login Successful **********")

        self.ad = AddCustomer(self.driver)
        self.ad.clickOnCustomerMenu()
        time.sleep(2)  # Ideally should use WebDriverWait here
        self.ad.clickOnCustomerMenuitem()
        time.sleep(2)
        self.ad.clickOnAddnew()
        time.sleep(2)

        self.logger.info("**** Providing Customer Info ****")

        self.email = random_generator() + "@gmail.com"
        self.ad.setEmail(self.email)
        time.sleep(2)
        self.ad.setPassword("12345")
        time.sleep(2)
        self.ad.FirstName("Nitin")
        time.sleep(2)
        self.ad.LastName("Pallavi")
        time.sleep(2)
        self.ad.setGender("Male")
        time.sleep(1)
        self.ad.Companyname("Learningkida")
        time.sleep(1)
        self.ad.ClickCheckBox_Tax()
        time.sleep(1)
        #self.ad.NewsSearchbox("nopCommerce admin demo store")
        time.sleep(1)
        #self.ad.setCustomerRole("Guests")
        time.sleep(1)
        self.ad.setManagerOfVendor("2")
        time.sleep(1)
        self.ad.clickSaveButton()
        time.sleep(3)

        self.logger.info("****** Saving Cusomer Info *****")

        self.logger.info("******** Add Customer Validation Started ********")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info(" ****** Add Customer Test Passed ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_addCustomer_scr.png")
            self.logger.info(" ****** Add Customer Test Failed ******")
            assert True == False
        self.driver.close()
        self.logger.info("****** Ending Test_003_AddCustomer Test ******")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
     return ''.join(random.choice(chars) for x in range(size))



