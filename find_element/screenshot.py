from find_element.capability import driver

driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('sssss')
driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
# driver.save_screenshot('login.png')
print('1')
try:
    driver.get_screenshot_as_file('./images/login.png')
except Exception as e:
    print(e)
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()