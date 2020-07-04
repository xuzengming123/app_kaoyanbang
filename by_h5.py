import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = '427e79ff'
desired_caps['appPackage'] = 'com.wondershare.drfone'
desired_caps['appActivity'] = 'com.wondershare.drfone.ui.activity.WelcomeActivity'
desired_caps['noReset'] = True


driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(3)

# 点击Backup
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

WebDriverWait(driver,15).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

time.sleep(2)
WebDriverWait(driver,8).until(lambda x:x.find_element_by_class_name('android.webkit.WebView'))
contexts = driver.contexts
# print(contexts)

driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
driver.find_element_by_id('email').send_keys('shuqing2018@163.com')
driver.find_element_by_class_name('btn_send').click()

driver.switch_to.contexts('NATIVE_APP')
driver.find_element_by_class_name('android.widget.ImageButton').click()