from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    # self.driver.find_element(By.CSS_SELECTOR, "h2")
    confirm_title = (By.CSS_SELECTOR, "h2")
    def get_confirm_title(self):
        return self.driver.find_element(*ConfirmPage.confirm_title)

    # self.driver.find_ellement(By.LINK_TEXT, "Go to Homepage")
    goto = (By.LINK_TEXT, "Go to Homepage")
    def get_Goto(self):
        return self.driver.find_element(*ConfirmPage.goto)