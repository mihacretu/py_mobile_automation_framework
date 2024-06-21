from appium import webdriver
from config.config import Config
from appium.options.android import UiAutomator2Options

def create_driver():
    if Config.PLATFORM == 'iOS':
        capabilities  = {
            'platformName': Config.IOS_PLATFORM_NAME,
            'appium:platformVersion': Config.IOS_PLATFORM_VERSION,
            'appium:deviceName': Config.IOS_DEVICE_NAME,
            'appium:automationName': Config.IOS_AUTOMATION_NAME,
            'app': Config.APP,
            'newCommandTimeout': 600
        }
    else:
        capabilities  = {
            'platformName': Config.ANDROID_PLATFORM_NAME,
            'appium:udid': 'emulator-5554',
            'appium:platformVersion': Config.ANDROID_PLATFORM_VERSION,
            'appium:deviceName': Config.ANDROID_DEVICE_NAME,
            'appium:automationName': Config.ANDROID_AUTOMATION_NAME,
            'appium:app': Config.APP,
            'newCommandTimeout': 600
        }
    # Converts capabilities to AppiumOptions instance
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

    driver = webdriver.Remote(command_executor='http://localhost:4723', options=capabilities_options )
    return driver
