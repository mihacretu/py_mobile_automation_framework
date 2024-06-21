from appium.webdriver.common.appiumby import AppiumBy
from config.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FinishPage:
    def __init__(self, driver):
        self.driver = driver
        if Config.PLATFORM == 'iOS':
            self.finish_title = (AppiumBy.ACCESSIBILITY_ID, 'finish_title')
        else:
            self.finish_title = (AppiumBy.ID, 'io.idnow.autoident:id/finish_title')

    def is_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.finish_title))
        return self.driver.find_element(*self.finish_title).is_displayed()

    def id_not_complete_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.finish_title,"Identification not completed"))
