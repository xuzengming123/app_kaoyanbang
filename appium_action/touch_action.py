from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep

Desired_Capabilities = {
  "platformName": "Android",
  "platformVersion": "8.0.0",
  "deviceName": "mi6",
  "automationName": "appium",
  "appPackage": "com.mymoney",
  "appActivity": "com.mymoney.biz.splash.SplashScreenActivity",
  "noReset": False,
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',Desired_Capabilities)
driver.implicitly_wait(5)

#获取屏幕尺寸
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

#显示屏幕尺寸
l = get_size()
print(l)
#向左滑动
def swipeLeft():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[0]*0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1,y1,x2,y1,1000)
#向上滑动
def swipeUp():
    l = get_size()
    y1 = int(l[0]*0.9)
    x1 = int(l[0]*0.5)
    y2 = int(l[0] * 0.1)
    driver.swipe(x1,y1,x1,y2,1000)

WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.mymoney:id/next_btn'))
for i in range(2):
    swipeLeft()
    sleep(0.5)

driver.find_element_by_id('com.mymoney:id/begin_btn').click()
try:
    closeBtn = driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
else:
    closeBtn.click()
driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()
WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.mymoney:id/title_tv'))
swipeUp()
swipeUp()
driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()
driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()
driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()

#手势滑动
for i in range(2):
    TouchAction(driver).press(x = 256,y = 566).wait(2000)\
    .move_to(x = 546,y = 555).wait(1000)\
    .move_to(x = 840,y = 872).wait(1000)\
    .move_to(x = 835,y = 1160).wait(1000)\
    .release().perform()