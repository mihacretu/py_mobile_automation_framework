import os

class Config:
    PLATFORM = os.getenv('PLATFORM', 'Android')  # 'iOS' or 'Android' - Default to 'Android' if PLATFORM is not set

    # Common settings
    APP = os.path.abspath('path/to/app.ipa') if PLATFORM == 'iOS' else os.path.abspath('../apk/app-release-signed-527.apk')

    # iOS settings
    IOS_PLATFORM_NAME = 'iOS'
    IOS_PLATFORM_VERSION = '14.4'  # Change as per your iOS version
    IOS_DEVICE_NAME = 'iPhone Simulator'  # Change as per your device
    IOS_AUTOMATION_NAME = 'XCUITest'

    # Android settings
    ANDROID_PLATFORM_NAME = 'Android'
    ANDROID_PLATFORM_VERSION = '11.0'  # Change as per your Android version
    ANDROID_DEVICE_NAME = 'Android Emulator'  # Change as per your device
    ANDROID_AUTOMATION_NAME = 'UiAutomator2'
