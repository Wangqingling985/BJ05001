# 1.导入driver对象(导包)
from appium import webdriver

desired_caps = {}      # server 启动参数
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# App信息
desired_caps['appPackage'] = 'com.android.settings'    # APP包名
desired_caps['appActivity'] = '.Settings'              # 启动名
# 2、声明手机驱动对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.quit()