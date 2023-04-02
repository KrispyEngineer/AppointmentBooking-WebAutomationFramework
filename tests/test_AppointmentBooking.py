import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.BookingPage import BookingPage
from PageObject.ConfirmPage import ConfirmPage
from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from Test_Data.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass



class Test_Book_Apointment(BaseClass):

    def test_Book_Apointment(self, get_data):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        bp = BookingPage(self.driver)
        cp = ConfirmPage(self.driver)

        hp.get_appointment().click()
        log.info("Clicked on Get Appointment")


        lp.get_Username().send_keys(get_data['Username'])
        log.info("Filled username")
        lp.get_Passwd().send_keys(get_data['Password'])
        log.info("Filled Password")
        lp.get_Login_Btn().click()
        log.info("Clicked on Login Button")

        self.SelectByText(bp.get_Facility(),get_data['Facility'])
        log.info("Selected Facility option")

        bp.get_Checkbox().click()
        log.info("Selected Readmission")

        bp.get_radio().click()
        bp.get_Date().send_keys(get_data['Visit Date'])
        log.info("Selected Date")
        bp.get_Comment().send_keys(get_data['Comment'])
        log.info("Entered comment")
        bp.get_Book_Btn().click()
        log.info("Clicked on book button")

        assert get_data['Confirm'] in cp.get_confirm_title().text
        assert cp.get_Goto().is_displayed()
        log.info("Booking Successful")

    @pytest.fixture(params=(HomePageData.getExcelData('TC2')))
    def get_data(self, request):
        return request.param