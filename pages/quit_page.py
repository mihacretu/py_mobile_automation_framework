import unittest
from appium.webdriver.common.appiumby import AppiumBy
from config.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QuitPage():
    def __init__(self, driver):
        self.driver = driver
        if Config.PLATFORM == 'iOS':
            self.page_title = (AppiumBy.ACCESSIBILITY_ID, 'intermediate_element')
            self.list_reasons = (AppiumBy.ACCESSIBILITY_ID, 'list_reasons')
            self.quit_button = (AppiumBy.ACCESSIBILITY_ID, 'finish_button')
            self.back_button = (AppiumBy.ACCESSIBILITY_ID, 'back_button')
        else:
            self.page_title = (AppiumBy.ID, 'io.idnow.autoident:id/title_text')
            self.list_reasons = (AppiumBy.ID, 'io.idnow.autoident:id/list_reasons')
            self.quit_button = (AppiumBy.ID, 'io.idnow.autoident:id/finish_button')
            self.back_button = (AppiumBy.ID, 'io.idnow.autoident:id/back_button')

    def is_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.page_title))
        return self.driver.find_element(*self.page_title).is_displayed()

    def get_reasons_elements(self):
        list_reasons_element = self.driver.find_element(*self.list_reasons)
        list_items_elem = list_reasons_element.find_elements(AppiumBy.CLASS_NAME, 'android.widget.TextView')

        return list_items_elem

    def get_reasons_text(self):
        list_items_elements = self.get_reasons_elements()

        # Extract text from each list item
        reasons_text = [item.text for item in list_items_elements]

        return reasons_text

    def choose_option_and_quit(self, option_text):
        # Wait until the list of reasons is visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.list_reasons)
        )

        list_items_elements = self.get_reasons_elements()

        # Iterate through the list items to find the one with the matching text
        for item in list_items_elements:
            if item.text == option_text:
                item.click()
                break

        # Wait until the quit session button is clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.quit_button)
        )
        quit_btn = self.driver.find_element(*self.quit_button)
        quit_btn.click()
