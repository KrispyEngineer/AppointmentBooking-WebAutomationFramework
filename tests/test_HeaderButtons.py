import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from Test_Data.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass




class Test_Header_Buttons(BaseClass):

    def test_Header_Butons(self,get_data):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        hp = HomePage(self.driver)

        actual_output = hp.get_homeTitle().text

        expected_output = get_data['Title']
        assert  expected_output in actual_output

        hp.get_Menu().click()

        assert hp.get_SideBar().is_displayed()

        assert hp.get_Home_Btn().is_displayed()

        hp.get_Home_Btn().click()
        log.info("Header validation successful")


    @pytest.fixture(params= HomePageData.getExcelData('TC3'))
    def get_data(self,request):
        return request.param