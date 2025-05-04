import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class AddCustomer():
    #Add Customer Page
    lnk_Customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_Customer_menu_item_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAdd_new_xpath = "//a[normalize-space()='Add new']"
    txt_Email_xpath = "//input[@id='Email']"
    txt_Password_xpath = "//input[@id='Password']"
    txt_FirstName_xpath = "//input[@id='FirstName']"
    txt_LastName_xpath = "//input[@id='LastName']"
    rdMale_Gender_id = "Gender_Male"
    rdFemale_Gender_id = "Gender_Female"
    txt_Company_Name_xpath = "//input[@id='Company']"
    chekTax_Exempt_xpath = "//input[@id='IsTaxExempt']"
    news_search_box_xpath = "//label[text()='Newsletter']/following::input[@role='searchbox'][1]"
    news_search_box_value_xpath = "//input[@class='select2-search__field']"
    txt_Customer_Role_xpath = "//input[@role='searchbox']"
    lst_item_Administrator_id = "select2-SelectedCustomerRoleIds-result-tdqa-1"
    lst_item_Forum_Moderators_id = "select2-SelectedCustomerRoleIds-result-l078-2"
    lst_item_Registered_id = "select2-SelectedCustomerRoleIds-result-2p9m-3"
    lst_item_Guest_id = "select2-SelectedCustomerRoleIds-result-kf3c-4"
    lst_item_Vendors_id = "select2-SelectedCustomerRoleIds-result-ftwa-5"
    lst_item_Manger_of_Vendor_xpath = "VendorId" #"//*[@id='VendorId']"
    check_box_Active_xpath = "//input[@id='Active']"
    chckbox_change_password_xpath = "//input[@id='MustChangePassword']"
    saveButton_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnk_Customers_menu_xpath).click()

    def clickOnCustomerMenuitem(self):
        self.driver.find_element(By.XPATH,self.lnk_Customer_menu_item_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAdd_new_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txt_Password_xpath).send_keys(password)

    def FirstName(self,name):
        self.driver.find_element(By.XPATH,self.txt_FirstName_xpath).send_keys(name)

    def LastName(self,Laname):
        self.driver.find_element(By.XPATH,self.txt_LastName_xpath).send_keys(Laname)

    def setGender(self,Gender):
        if Gender == "Male":
            self.driver.find_element(By.ID,self.rdMale_Gender_id).click()

        elif Gender == "Female":
            self.driver.find_element(By.ID, self.rdFemale_Gender_id).click()

        else:
            self.driver.find_element(By.ID, self.rdMale_Gender_id).click()

    def Companyname(self,Comp_Name):
        self.driver.find_element(By.XPATH, self.txt_Company_Name_xpath).send_keys(Comp_Name)

    def ClickCheckBox_Tax(self):
        self.driver.find_element(By.XPATH, self.chekTax_Exempt_xpath).click()

    def NewsSearchbox(self,value):
        newsletter_input = self.driver.find_element(By.XPATH,self.news_search_box_xpath).click()
        time.sleep(2)
        newsletter_input.send_keys(value)
        newsletter_input.send_keys(Keys.ENTER)


    def setCustomerRole(self,role):
        self.driver.find_element(By.ID,self.txt_Customer_Role_xpath).click()
        time.sleep(3)
        if role==" Registered":
            self.listitem = self.driver.find_element(By.ID,self.lst_item_Registered_id)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.ID, self.lst_item_Administrator_id)
        elif role == "Guests":
            self.listitem = self.driver.find_element(By.ID, self.lst_item_Guest_id)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.ID, self.lst_item_Vendors_id)

        else:
            self.listitem = self.driver.find_element(By.ID, self.lst_item_Guest_id)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drpdown_element = self.driver.find_element(By.ID, self.lst_item_Manger_of_Vendor_xpath)
        drpdown = Select(drpdown_element)
        drpdown.select_by_value(value)

    def clickSaveButton(self):
        self.driver.find_element(By.XPATH,self.saveButton_xpath).click()