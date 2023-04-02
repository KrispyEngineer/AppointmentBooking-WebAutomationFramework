import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from PageObject.BookingPage import BookingPage
from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from Test_Data.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class Test_Login(BaseClass):

    def test_Login(self,get_data):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        bp = BookingPage(self.driver)


        hp.get_Menu().click()
        log.info("Clicked on Menu")
        hp.get_Login().click()
        log.info("Clicked on Login")
        lp.get_Username().send_keys(get_data['Username'])
        log.info("Entered Username")
        lp.get_Passwd().send_keys(get_data['Password'])
        log.info("Entered Password")
        lp.get_Login_Btn().click()
        log.info("Clicked on login button")

        heading = bp.get_header_Booking().text
        assert heading == get_data['Appoint']
        log.info("Login successful")
        bp.get_Menu().click()
        bp.get_Logout().click()
        log.info("Clicked on logout")


    @pytest.fixture(params=HomePageData.getExcelData('TC1'))
    def get_data(self, request):
        return request.param
