from appium_advance.page_object.unittest.myunit import StartEnd
from appium_advance.page_object.loginView import LoginView
import logging
import unittest

class TestLogin(StartEnd):
    def test_login_xzw2018(self):
        logging.info('=====test_login_xzw2018=====')
        l = LoginView(self.driver)
        l.login_action('自学网2018','zxw2018')

    def test_login_xzw2017(self):
        logging.info('=====test_login_xzw2017=====')
        l = LoginView(self.driver)
        l.login_action('自学网2017', 'zxw2017')

    def test_login_error(self):
        logging.info('=====test_login_error=====')
        l = LoginView(self.driver)
        l.login_action('666', '222')

if __name__ == '__main__':
    unittest.main()
