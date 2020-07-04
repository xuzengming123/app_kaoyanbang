import time

from appium import webdriver

# 考研帮app配置
from selenium.common.exceptions import NoSuchElementException

Desired_Capabilities = {
  "platformName": "Android",
  "platformVersion": "8.0.0",
  "deviceName": "Redmi_Note_5",
  "automationName": "appium",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": False,
  "unicodeKeyboard": True,
  "resetKeyboard": True,
  'skipServerInstallation': True,
  'skipDeviceInitialization': True,
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",Desired_Capabilities)
driver.implicitly_wait(5)

def check_cancelBtn():
    print('取消升级')
    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException as e:
        print(e)
        print('no cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    print('跳过广告')
    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException as e:
        print(e)
        print('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()
# check_skipBtn()
