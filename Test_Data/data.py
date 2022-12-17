# This file consists of Test Information like username, password, XPATH, etc.

# Python Class for Username and Password
class OrangeHRM_Data:
    username = 'Admin'
    password_invalid = 'Invalid password'
    password_valid = 'admin123'
    firstname = 'Desabandhu'
    middlename = 'R'
    lastname = 'S'
    nickname = 'Buvanesh'
    Title = 'OrangeHRM'
    
# Python Class for Selenium Selectors
class OrangeHRM_Selectors:
    Username_NAME = 'username'
    Password_NAME = 'password'
    Login_XPATH = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    PIM_XPATH = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    Add_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    Firstname_Name = 'firstName'
    Middlename_Name = 'middleName'
    Last_Name = 'lastName'
    Savebutton_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    Nickname_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    Gender_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label'
    Editsavebutton_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    Select_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[9]/div/div[1]/div/div/label/span/i'
    Delete_XPATH = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[9]/div/div[9]/div/button[1]/i'
    Confirm_XPATH = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'