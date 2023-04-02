from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.XPATH, "(//input[@placeholder='Username'])[2]")

    username = (By.XPATH, "(//input[@placeholder='Username'])[2]")

    def get_Username(self):
        return self.driver.find_element(*LoginPage.username)

    # self.driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[2]")
    password = (By.XPATH, "(//input[@placeholder='Password'])[2]")

    def get_Passwd(self):
        return self.driver.find_element(*LoginPage.password)

    #     # self.driver.find_element(By.ID, "btn-login")

    login_btn = (By.ID, "btn-login")

    def get_Login_Btn(self):
        return self.driver.find_element(*LoginPage.login_btn)

