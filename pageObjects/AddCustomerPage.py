import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Add customer Page
class AddCustomer:
    lnkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtcustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    txtcustomerroleclear="//span[@title='delete']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrofVendors_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickOnCustomersMenuMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickOnCAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()

    def setCompanyName(self, compname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(compname)

    def setCustomerRoles(self, role):
        # clear any
        self.driver.find_element(By.XPATH, self.txtcustomerroleclear).click()
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        # self.custlist = self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath)
        # self.driver.execute_script("arguments[0].click();", self.custlist)

        if role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        elif role == 'Guests':
            # user can't be registered and Guest either only one so remove the existing one if it is available
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("argument[0].click():", self.listitem)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(comment)

    def setMgrofVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrofVendors_xpath))
        drp.select_by_visible_text(value)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()