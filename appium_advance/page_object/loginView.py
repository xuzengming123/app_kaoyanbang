from appium_advance.page_object.desired_caps import appium_desired
import logging
from selenium.webdriver.common.by import By
from appium_advance.page_object.common_fun import Common

class LoginView(Common):
    username_type = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn_type = (By.ID,'com.tal.kaoyan:id/login_login_btn')

    def login_action(self,username,password):
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
        driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
        logging.info('================login================')
        logging.info('input username: %s'% username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('input password: %s'% password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn_type).click()
        logging.info('login finished')

if __name__ == '__main__':
    driver = appium_desired()
    loger = LoginView(driver)
    loger.login_action('自学网2018','zxw2018')
