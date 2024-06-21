import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

class TermsConditionsPage:
    def __init__(self, driver):
        self.driver = driver
        if Config.PLATFORM == 'iOS':
            self.page_logo = (AppiumBy.ACCESSIBILITY_ID, 'close_icon')
            self.close_icon = (AppiumBy.ACCESSIBILITY_ID, 'close_icon')
        else:
            self.page_logo = (AppiumBy.ID, 'io.idnow.autoident:id/consentScreenHeader')
            self.close_icon = (AppiumBy.ID, 'io.idnow.autoident:id/idnow_close_button')

    def is_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.page_logo))
        return self.driver.find_element(*self.page_logo).is_displayed()

    def click_close(self):
        self.driver.find_element(*self.close_icon).click()
