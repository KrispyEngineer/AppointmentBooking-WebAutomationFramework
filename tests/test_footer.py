import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass



class Test_Footer(BaseClass):

    def test_Footer(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        hp = HomePage(self.driver)

        assert hp.get_Footer().is_displayed()
        log.info("Footer validation successful")