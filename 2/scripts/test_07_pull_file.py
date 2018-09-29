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

"""需求：把手机内/sdcard/2.txt拉去到本地"""
data = driver.pull_file('/sdcard/1.txt')  #
# 返回数据为base64编码
data01=str(base64.b64decode(data), 'utf-8')
with open("./write_1.txt", "w", encoding="utf-8") as f:
    f.write(data01)


"""获取设置页面元素结构："""
# 3.1.7获取当前屏幕内元素结构
# driver.page_source
# assert '电池' in driver.page_source   # 断言

driver.quit()