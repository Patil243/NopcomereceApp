import pytest
import time
import random
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen
from utilities import XLUtils

class Test_002_DD_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    def test_login_DD(self,setup):
        self.logger.info("************ Test_002_DD_Login **********")
        self.logger.info("******* Verifying the logging test *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        self.column = XLUtils.getRowCount(self.path,"Sheet1")

        list_status=[]

        for row in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path,'Sheet1',row,1)
            self.password = XLUtils.readData(self.path,'Sheet1',row,2)
            self.expected =XLUtils.readData(self.path,'Sheet1',row,3)

            #for item in self.username:
            #  time.sleep(random.uniform(0.3, .5))

            self.lp.setUserName(self.username)

            time.sleep(2)

            #for item in self.password:
             # time.sleep(random.uniform(0.3, .5))
            self.lp.setPassword(self.password)

            time.sleep(2)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("************ Login test is passed **********")
                    self.lp.clicklogout()
                    list_status.append("Pass")
                    time.sleep(5)

                elif self.expected == "Fail":
                    self.logger.info("************ Login test is Failed **********")
                    self.lp.clicklogout()
                    list_status.append("Fail")

            elif act_title != exp_title:

                if self.expected == "Pass":
                    self.logger.info("**** failed ****")
                    list_status.append("Fail")

                elif self.expected == "Fsil":
                    self.logger.info("**** Passed ****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("**** Login DD Test Is Passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DD Test Is Failed ****")
            self.driver.close()
            assert False

        self.logger.info("**** End Of Login DD test ****")
        self.logger.info("**** Completed Test_002_DD_Login **** ")


