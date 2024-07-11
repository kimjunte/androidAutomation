import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Google Pixel',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://192.168.0.23:4723'

@pytest.fixture(scope="module")
def driver():
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=options)
    yield driver
    driver.quit()

def test_find_battery(driver):
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
