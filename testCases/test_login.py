import pytest
import time
import random
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password  = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************ Test_001_Login **********" )
        self.logger.info("******* Verifying Home Page Title *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        time.sleep(2)

        if act_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("******* Home Page Title Test Is Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "homePageTitle.png")
            self.driver.close()
            self.logger.info("******* Home Page Title Test Is Failed *******")
            assert False

    def test_login(self,setup):
        self.logger.info("************ Test_001_Login **********")
        self.logger.info("******* Verifying the logging test *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        for item in self.username:
            time.sleep(random.uniform(0.3,.5))
            self.lp.setUserName(item)
        time.sleep(2)
        for item in self.password:
            time.sleep(random.uniform(0.3, .5))
            self.lp.setPassword(item)
        time.sleep(2)
        self.lp.clicklogin()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            time.sleep(5)
            self.lp.clicklogout()
            assert True
            self.logger.info("************ Login test is passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************ Login test is failed **********")
            assert False


