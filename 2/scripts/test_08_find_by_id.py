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


# 3.3.3.通过id定位
"""
  业务场景:
      1.进入设置页面
      2.通过ID定位方式点击搜索按钮
"""
# driver.find_element_by_id("com.android.settings:id/search").click()

'''3.通过class定位方式点击输入框的 返回按钮'''
# sleep(2)
# driver.find_element_by_class_name('android.widget.ImageButton').click()

"""
    业务场景:
        1.进入设置页面
        2.点击WLAN菜单栏
"""''
'''方法一：使用xpath-contains定位'''
# sleep(2)
driver.find_element_by_xpath("//*[contains(@resource-id,'com.android.settings:id/title')]").click()
# driver.find_element_by_xpath("//*[contains(@text,'WLA')]").click()
# driver.find_element_by_xpath("//*[contains(@class,'android.widget.TextView')]").click()     # class不是唯一的定位不到

'''方法二：使用xpath 属性定位'''
driver.find_element_by_xpath("//*[@text='WLAN']").click()



# 3.3.6.定位一组元素,注意element -> elements
# title = driver.find_elements_by_id("com.android.settings:id/title")




sleep(2)
driver.quit()