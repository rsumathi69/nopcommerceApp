import random
import string

import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*********** Verifying test_login ***************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********** login successful *****************")

        self.logger.info("*********** starting Add customer Test *****************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuMenuItem()
        self.addcust.clickOnCAddnew()

        self.logger.info("**************Providing customer info***************")
        self.email = Test_003_AddCustomer.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Sundar")
        self.addcust.setLastName("Raghu")
        self.addcust.setDob("05/28/1980")
        self.addcust.setCompanyName("QATalents")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setMgrofVendor("Vendor 2")
        self.addcust.setAdminComment("This is for testing selenium UI automation")
        self.addcust.clickOnSave()

        self.logger.info("**************saving customer info***************")
        self.logger.info("**************validating add customer information started ***************")
        self.msg=self.driver.page_source
        print(self.msg)

        if 'The new customer has been added successfully.' in self.driver.page_source:
            assert True == True
            self.logger.info("****************Add customer Test passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.info("****************Add customer Test failed ****************")
            assert True == False

        self.driver.close()
        self.logger.info("****************Ending Add customer Test ****************")


    def random_generator(chrs=string.ascii_lowercase + string.digits):
        rndstr=''.join((random.choice(chrs)) for x in range(8))
        print(rndstr)
        return rndstr
