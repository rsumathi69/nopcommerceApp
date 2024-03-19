import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from utilities import XlsUtlity


class Test_002_Login_DDT:
    baseURL = ReadConfig.getApplicationURL()
    path = './/Testdata/LoginTestData.xlsx'
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*********** Verifying test_login_ddt ***************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XlsUtlity.getRowCount(self.path, 'Sheet1')
        print(f"no of rows in excel is {self.rows}")
        ls_status = []
        for r in range(2, self.rows + 1):
            self.username = XlsUtlity.readData(self.path, 'Sheet1', r, 1)
            self.password = XlsUtlity.readData(self.path, 'Sheet1', r, 2)
            self.exp = XlsUtlity.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("****Passed****")
                    self.lp.clickLogout()
                    ls_status.append("Pass")
                    self.logger.info("*********** Verifying test_ddt_login passed ***************** ")
                elif self.exp == 'Fail':
                    self.logger.info("****Failed****")
                    ls_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("****failed****")
                    ls_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("****Passed for invalid data ****")
                    ls_status.append("Pass")
                    self.logger.info("*********** Verifying test_ddt_login passed ***************** ")

        if 'Fail' not in ls_status:
            self.logger.info("*********** test_ddt_login passed ***************** ")
            assert True
        else:
            self.logger.info("*********** test_login_ddt failed ***************** ")
            assert False

        self.logger.info("*********** End of test_login_ddt ***************** ")
        self.logger.info("*********** Test_002_DDT_Login completed ***************** ")
        self.driver.close()
