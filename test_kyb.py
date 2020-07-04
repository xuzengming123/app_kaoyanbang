import time

from appium import webdriver

# 考研帮app配置
from selenium.common.exceptions import NoSuchElementException

Desired_Capabilities = {
  "platformName": "Android",
  "platformVersion": "8.0.0",
  "deviceName": "Redmi_Note_5",
  "automationName": "Appium",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True,
  "unicodeKeyboard": True,
  "resetKeyboard": True,
  'skipServerInstallation': True,
  'skipDeviceInitialization': True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",Desired_Capabilities)
driver.implicitly_wait(10)
class LoginKYB:
    #开屏广告跳过
    def check_ad(self):
        try:
            self.locat = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
        except NoSuchElementException:
            print("没有开屏广告")
        else:
            self.locat.click()

    # 确定专业和院校弹框
    def check_toase(self):
        try:
            self.toase = driver.find_element_by_id('com.tal.kaoyan:id/kaoyan_home_schtip_close')
        except NoSuchElementException:
            print('没有弹框')
        else:
            self.toase.click()

    # 点击我的页面
    def click_myself(self):
        try:
            self.myself = driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
        except NoSuchElementException:
            print('没有找到元素')
        else:
            self.myself.click()

    #点击密码-登录
    def click_passwordlogin(self):
        try:
            self.click_passwordlogin = driver.find_element_by_id('com.tal.kaoyan:id/login_code_touname')
        except NoSuchElementException:
            print('没有找到元素')
        else:
            self.click_passwordlogin.click()

    #输入手机号和密码
    def send_value(self):
        try:
            self.send_mobile = driver.find_element_by_id('')
            self.send_password = driver.find_element_by_id('')
        except NoSuchElementException:
            print('没有找到元素')
        else:
            self.send_mobile.clear()
            self.send_mobile.send_keys('自学网2018')
            self.send_password.clear()
            self.send_password.send_keys('zxw2018')

    #点击登录按钮
    def login(self):
        try:
            self.login_button = driver.find_element_by_id('')
        except NoSuchElementException:
            print('没有找到元素')
        else:
            self.login_button.click()

if __name__ == '__main__':
    A = LoginKYB()
    A.check_ad()
    A.check_toase()
    A.click_myself()
    A.click_passwordlogin()
    A.send_password()
    A.login()