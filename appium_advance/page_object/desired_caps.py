from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import yaml
import logging
import logging.config


CON_LOG = '../log/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

def appium_desired():
    file = open('../yaml/desired_caps.yaml', 'r')
    data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['polatformVersion'] = data['polatformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('start app.....')
    driver = webdriver.Remote('http://'+str(data['ip']) + ':' + str(data['port']) + '/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()