from appium import webdriver

# 考研帮app配置
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

