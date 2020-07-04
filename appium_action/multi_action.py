import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

Desired_Capabilities = {
  "platformName": "Android",
  "platformVersion": "8.0.0",
  "deviceName": "mi6",
  "automationName": "appium",
  "appPackage": "com.baidu.BaiduMap",
  "appActivity": "com.baidu.baidumaps.WelcomeScreen",
  "noReset": True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',Desired_Capabilities)
driver.implicitly_wait(5)
time.sleep(3)

x = driver.get_window_size()['width']
y = driver.get_window_size()['height']

#进入地图
# driver.find_element_by_id('com.baidu.BaiduMap:id/dj2').click()
# driver.find_element_by_id('com.baidu.BaiduMap:id/byo').click()


def pinch():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    pinch_action=MultiAction(driver)

    action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8,y=y*0.8).wait(1000).move_to(x=x*0.6,y=y*0.6).wait(1000).release()

    pinch_action.add(action1,action2)
    print('start pinch...')
    pinch_action.perform()

def zoom():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
    action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()

    zoom_action.add(action1,action2)
    print("start zoom...")
    zoom_action.perform()

if __name__ == '__main__':

    for i in range(3):
        pinch()

    for i in range(3):
        zoom()
