# 1.导入driver对象(导包)
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

"""需求：判断百年奥莱app是否安装，如果安装了，进行卸载；否则进行安装"""
flag=driver.is_app_installed('com.yunmall.lc')
print("百年奥莱APK是否已安装：",flag)
if flag:        # if 后面可以用 True
    try:
        driver.remove_app('com.yunmall.lc')
        print('卸载成功！')
    except:
        print('卸载失败！')
else:
    try:
        driver.install_app('C:\\bainianaolai.apk')
        print('安装成功！')
    except:
        print('安装失败！')




#
# flag=driver.is_app_installed('com.fmd.mall')
# print("聚加尚品APK是否已安装：",flag)
# if flag:        # if 后面可以用 True
#     try:
#         driver.remove_app('com.fmd.mall')
#         print('卸载成功！')
#     except:
#         print('卸载失败！')
# else:
#     try:
#         driver.install_app('C:\\com.fmd.mall_1.2_12.apk')
#         print('安装成功！')
#     except:
#         print('安装失败！')







driver.quit()


