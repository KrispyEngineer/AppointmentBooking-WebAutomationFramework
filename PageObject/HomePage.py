from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.ID, "menu-toggle")

    menu = (By.ID, "menu-toggle")

    def get_Menu(self):
        return self.driver.find_element(*HomePage.menu)

    #self.driver.find_element(By.LINK_TEXT, "Login")

    login = (By.LINK_TEXT, "Login")

    def get_Login(self):

        return self.driver.find_element(*HomePage.login)

    # self.driver.find_element(By.CSS_SELECTOR, "h1")

    home_title = (By.CSS_SELECTOR, "h1")

    def get_homeTitle(self):
        return self.driver.find_element(*HomePage.home_title)

    # self.driver.find_element(By.ID, "sidebar-wrapper")

    sidebar = (By.ID, "sidebar-wrapper")
    def get_SideBar(self):
        return self.driver.find_element(*HomePage.sidebar)

    # self.driver.find_element(By.LINK_TEXT, "Home")

    home_btn = (By.LINK_TEXT, "Home")
    def get_Home_Btn(self):
        return self.driver.find_element(*HomePage.home_btn)

    # self.driver.find_element(By.CSS_SELECTOR, "footer")

    footer = (By.CSS_SELECTOR, "footer")

    def get_Footer(self):
        return self.driver.find_element(*HomePage.footer)

    # self.driver.find_element(By.ID, "btn-make-appointment")

    appointment = (By.ID, "btn-make-appointment")
    def get_appointment(self):
        return self.driver.find_element(*HomePage.appointment)