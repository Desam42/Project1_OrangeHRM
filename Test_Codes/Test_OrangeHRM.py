from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_OrangeHRM:
    url = 'https://opensource-demo.orangehrmlive.com/'
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()
            
    def test_TC_login_01(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Username_NAME).send_keys(data.OrangeHRM_Data.username)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Password_NAME).send_keys(data.OrangeHRM_Data.password_valid)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Login_XPATH).click()
        assert self.driver.title == data.OrangeHRM_Data.Title
        print("SUCCESS # Successfully logged in")
        
    def test_TC_login_02(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Username_NAME).send_keys(data.OrangeHRM_Data.username)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Password_NAME).send_keys(data.OrangeHRM_Data.password_invalid)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Login_XPATH).click()
        print("SUCCESS # Invalid credential")
        
    def test_TC_PIM_01(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Username_NAME).send_keys(data.OrangeHRM_Data.username)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Password_NAME).send_keys(data.OrangeHRM_Data.password_valid)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Login_XPATH).click()
        time.sleep(5)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.PIM_XPATH).click()
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Add_XPATH).click()
        time.sleep(3)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Firstname_Name).send_keys(data.OrangeHRM_Data.firstname)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Middlename_Name).send_keys(data.OrangeHRM_Data.middlename)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Last_Name).send_keys(data.OrangeHRM_Data.lastname) 
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Savebutton_XPATH).click()
        print("SUCCESS # New Employee Added Successfully")
        
    def test_TC_PIM_02(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Username_NAME).send_keys(data.OrangeHRM_Data.username)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Password_NAME).send_keys(data.OrangeHRM_Data.password_valid)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Login_XPATH).click()
        time.sleep(5)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.PIM_XPATH).click()
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Add_XPATH).click()
        time.sleep(3)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Firstname_Name).send_keys(data.OrangeHRM_Data.firstname)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Middlename_Name).send_keys(data.OrangeHRM_Data.middlename)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Last_Name).send_keys(data.OrangeHRM_Data.lastname) 
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Savebutton_XPATH).click()
        time.sleep(8)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Nickname_XPATH).send_keys(data.OrangeHRM_Data.nickname)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Gender_XPATH).click()
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Editsavebutton_XPATH).click()
        print("SUCCESS # Employee Details Added Successfully")
        
    def test_TC_PIM_03(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Username_NAME).send_keys(data.OrangeHRM_Data.username)
        self.driver.find_element(by = By.NAME, value=data.OrangeHRM_Selectors.Password_NAME).send_keys(data.OrangeHRM_Data.password_valid)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Login_XPATH).click()
        time.sleep(5)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.PIM_XPATH).click()
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Select_XPATH).click()
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Delete_XPATH).click()
        time.sleep(3)
        self.driver.find_element(by = By.XPATH, value=data.OrangeHRM_Selectors.Confirm_XPATH).click()
        print("SUCCESS # Employee details deleted successfully")