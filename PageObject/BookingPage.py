from selenium.webdriver.common.by import By


class BookingPage:

    def __init__(self,driver):
        self.driver = driver


    # self.driver.find_element(By.CSS_SELECTOR, "h2")

    heading_validation = (By.CSS_SELECTOR, "h2")


    def get_header_Booking(self):
        return self.driver.find_element(*BookingPage.heading_validation)

    # self.driver.find_element(By.ID, "menu-toggle")

    menu = (By.ID, "menu-toggle")

    def get_Menu(self):
        return self.driver.find_element(*BookingPage.menu)

    # self.driver.find_element(By.LINK_TEXT, "Logout")

    logout = (By.LINK_TEXT, "Logout")

    def get_Logout(self):
        return self.driver.find_element(*BookingPage.logout)

    # self.driver.find_element(By.ID, "combo_facility")
    facility = (By.ID, "combo_facility")

    def get_Facility(self):
        return self.driver.find_element(*BookingPage.facility)

    # self.driver.find_element(By.ID,"chk_hospotal_readmission")
    checkbox = (By.ID,"chk_hospotal_readmission")

    def get_Checkbox(self):
        return self.driver.find_element(*BookingPage.checkbox)

    # self.driver.find_element(By.CSS_SELECTOR, "input[value='Medicaid']")
    radio = (By.CSS_SELECTOR, "input[value='Medicaid']")
    def get_radio(self):
        return self.driver.find_element(*BookingPage.radio)

    # self.driver.find_element(By.CSS_SELECTOR, "input[name='visit_date']")
    date = (By.CSS_SELECTOR, "input[name='visit_date']")
    def get_Date(self):
        return self.driver.find_element(*BookingPage.date)

    # self.driver.find_element(By.ID, "txt_comment")
    comment = (By.ID, "txt_comment")

    def get_Comment(self):
        return self.driver.find_element(*BookingPage.comment)

    # self.driver.find_element(By.ID, "btn-book-appointment")
    book_btn = (By.ID, "btn-book-appointment")

    def get_Book_Btn(self):
        return self.driver.find_element(*BookingPage.book_btn)