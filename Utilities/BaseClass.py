import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def VerifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(((By.LINK_TEXT, text))))

    def SelectByText(self,locator,text):
        dropdown = Select((locator))
        dropdown.select_by_visible_text(text)

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        file_handler = logging.FileHandler("logFile.log")

        logger.addHandler(file_handler)  # This takes a object which will have file path or name or details

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        return logger