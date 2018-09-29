# 1.导入driver对象(导包)
import base64
from time import sleep
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


"""需求：把1.txt发送到手机"""
with open("./1.txt", "r", encoding="utf-8") as f:
    data = str(base64.b64encode(f.read().encode("utf-8")), "utf-8")
    driver.push_file("/sdcard/1.txt", data)


driver.quit()

