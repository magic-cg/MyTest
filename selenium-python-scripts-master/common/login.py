# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import platform
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# reload(sys)
# sys.setdefaultencoding("utf-8")


def get_driver_cyj():
    options = webdriver.ChromeOptions()
    # Windows电脑启动最大化
    options.add_argument("--start-maximized")
    # mac电脑启动最大化
    # options.add_argument("--kiosk")

    # 设置下载的默认路径
    prefs = {'profile.defalut_content_setting.popups': 0, 'download.default_directory': 'E:\\Downloads'}
    options.add_experimental_option('prefs', prefs)

    # 判断是mac电脑还是Windows电脑来匹配driver

    currentLocation = os.path.dirname(os.path.dirname(os.getcwd()))

    if platform.system() == 'Windows':
        chromedriver = currentLocation + '/chromedriver.exe'
    else:

        chromedriver = currentLocation + '/chromedriver'
    #
    # driver = webdriver.Chrome(chromedriver, desired_capabilities=options.to_capabilities())

    # 配合脚本最大化
    # driver = webdriver.Chrome(desired_capabilities=options.to_capabilities())

    # driver = webdriver.Firefox(）

    driver = webdriver.Chrome(chromedriver, chrome_options=options)
    # driver = webdriver.Chrome()

    # 钉钉测试登录链接
    url_cyj = 'http://4470.qhose.com.cn:58080/web/debugger.html?corpId=dingf26874cd5c6c16c035c2f4657eb6378f&accessToken=fkXiVcEBkS-L3sSh_Tm_b0&ekbCorpId=iXo7igqG700000#/bills'

    # 企业微信测试登录链接
    # url_cyj = 'http://wx480.qhose.com.cn/web/weixin.html?from=applet&auth_code=JXN-ljYUBAVojThU-wI2RVMHtyL5OVtmUeTJRG-XgGA&corpId=ww765915f2a8d3e2d1&ekbCorpId=CeQ6IFSwEM0000&accessToken=RTG-We53WX0m767fCCPYk0&billState=undefined#/bills'

    # 云之家测试登录链接
    # url_cyj = 'http://kd430.qhose.com.cn:58080/web/kdcloud.html?ticket=APPURLWITHTICKET8350da66741eae68bc92ca03b7d82a31#/bills'

    # 企业微信线上
    # url_cyj = 'https://wx2.ekuaibao.com/web/weixin.html?from=applet&auth_code=Nwonmji4WK9yCE4OsIn8K0HJERUlCR7pqubsLeKdnwU&corpId=ww765915f2a8d3e2d1&ekbCorpId=jsw646Uwfo0400&accessToken=hmACCGlGVBm4w5XRpxmUeM&billState=undefined#/bills'

    # 云之家线上
    # url_cyj = 'https://kdcloud2.ekuaibao.com/web/kdcloud.html?ticket=APPURLWITHTICKETb82a3ffb248f15a2ed115ffd4bfab3d1#/bills'

    # 钉钉线上
    # url_cyj = 'https://dd2.ekuaibao.com/4.28/web/debugger.html?accessToken=wbhzxRXir7GfXlaPTVznLg&corpId=ding27b1a375a0aea94535c2f4657eb6378f&ekbCorpId=ding27b1a375a0aea94535c2f4657eb6378f#/bills'

    driver.get(url_cyj)
    return driver


