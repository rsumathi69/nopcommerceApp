from selenium.webdriver.common.by import By


class SearchCustomer:
    txtEmail_id='SearchEmail'
    txtFirstName_id='SearchFirstName'
    txtLastName_id='SearchLastName'
    btnSearch_id='search-customers'
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self, fName):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fName)

    def setLastName(self, lName):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lName)
    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getCols(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getRows()+1):
            emailid = self.driver.find_element(By.XPATH,self.tableRows_xpath+"["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerByFullName(self, name):
        flag = False
        for r in range(1, self.getRows() + 1):
            fullname = self.driver.find_element(By.XPATH, self.tableRows_xpath + "[" + str(r) + "]/td[3]").text
            if fullname == name:
                flag = True
                break
        return flag
