import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("*********** Test_001_login ***************** ")
        self.logger.info("*********** Verifying Home Page Title ***************** ")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=='Your store. Login':
            assert True
            self.logger.info("*********** Verifying Home Page Title passed  ***************** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.info("*********** Verifying Home Page Title Failed ***************** ")
            assert False

        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*********** Verifying test_login ***************** ")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if  act_title=='Dashboard / nopCommerce administration':
            assert True
            self.logger.info("*********** Verifying test_login passed ***************** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.info("*********** Verifying test_login failed ***************** ")
            assert False
        self.driver.close()