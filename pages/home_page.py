from appium.webdriver.common.appiumby import AppiumBy
from config.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        if Config.PLATFORM == 'iOS':
            self.home_screen_logo = (AppiumBy.ACCESSIBILITY_ID, 'home_screen_logo')
            self.ident_id_input = (AppiumBy.ACCESSIBILITY_ID, 'editTextCode')
            self.start_ident_button = (AppiumBy.ACCESSIBILITY_ID, 'start_ident')
        else:
            self.home_screen_logo = (AppiumBy.ID, 'io.idnow.autoident:id/homescreen_idnow_logo')
            self.ident_id_input = (AppiumBy.ID, 'io.idnow.autoident:id/editTextCode')
            self.start_ident_button = (AppiumBy.ID, 'io.idnow.autoident:id/start_ident')

    def is_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.home_screen_logo))
        return self.driver.find_element(*self.home_screen_logo).is_displayed()

    def input_id_is_displayed(self):
        return self.driver.find_element(*self.ident_id_input).is_displayed()

    def start_button_is_displayed(self):
        is_displayed = self.driver.find_element(*self.start_ident_button).is_displayed()
        button_text = self.driver.find_element(*self.start_ident_button).text

        return is_displayed and button_text == "Start"

    def enter_ident_id(self, ident_id):
        self.driver.find_element(*self.ident_id_input).send_keys(ident_id)

    def click_start_ident(self):
        self.driver.find_element(*self.start_ident_button).click()
