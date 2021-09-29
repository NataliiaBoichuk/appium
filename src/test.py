from appium import webdriver
from selenium.webdriver.common.by import By

# url = 'http://127.0.0.1:4723/wd/hub'
url = "https://oauth-natalia.boichuk-d6f64:d5f3e9d6-1fa5-4eb8-b975-00f78ec999d9@ondemand" \
      ".eu-central-1.saucelabs.com:443/wd/hub"
caps = {
    "platformName": "Android",
    "platformVersion": "6",
    "deviceName": "Android Emulator",
    "appActivity": "com.swaglabsmobileapp.MainActivity",
    "appPackage": "com.swaglabsmobileapp",
    # "app": "C:\\Users\\nboichuk\\PycharmProjects\\appium_sauce_labs\\src\\app\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
    "app": "https://github.com/saucelabs/sample-app-mobile/releases/download/2.7.1/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
    "automationName": "UiAutomator2"
}
driver = webdriver.Remote(command_executor=url, desired_capabilities=caps)
driver.implicitly_wait(5)
# locators
driver.find_element_by_accessibility_id('test-Username').send_keys("standard_user")
driver.find_element_by_accessibility_id('test-Password').send_keys("secret_sauce")
driver.find_element_by_accessibility_id('test-LOGIN').click()

assert driver.find_element_by_accessibility_id("test-PRODUCTS").is_displayed()


