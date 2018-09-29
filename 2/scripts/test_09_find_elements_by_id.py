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

"""
    业务场景:
        1.进入设置页面
        2.点击WLAN菜单栏(id定位对象列表中第1个)
"""
'''通过 id 方式定位一组元素'''
# elements = driver.find_elements_by_id("com.android.settings:id/title")
# print("总共获取了多个少元素：",len(elements))
# for i in elements:
#     print('列表元素内容为：',i.text)
# # 点击下标为1的元素
# elements[0].click()


'''通过 class 方式定位一组元素'''

"""通过元素的 【属性名和值】"""
# elements=driver.find_elements_by_xpath("//*[@class='android.widget.TextView']")

"""通过contains形式"""
elements=driver.find_elements_by_xpath('//*[contains(@class,"widget.TextView")]')

for ele in elements:
     print(ele.text)
elements[3].click()


sleep(2)
driver.quit()