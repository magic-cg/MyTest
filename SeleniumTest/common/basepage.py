# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os

"""
  基础类BasePage，封装所有页面都公用的方法,
  重定义find_element,截图，下载等
  WebDriverWait提供了显式等待方式。

"""


class BasePage(object):
    """
    BasePage封装所有页面都公用的方法
    """
    def __init__(self, driver):
        self.driver = driver
        # self.dict = {}

    def find_element(self, ele_name, time=10):
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            #            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(ele_name))
            # return self.driver.find_element(*ele_name)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, ele_name))

    def find_element1(self, ele_name, time=10):
        try:

            # 注意：以下入参本身是元组，不需要加*
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(ele_name))

        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, ele_name))

    def find_element2(self, ele_name):
        return self.driver.find_element(*ele_name)

    # 获取当前window的截图,filename参数是保存文件的路径
    def screenshot_file(self, filename):
        return self.driver.get_screenshot_as_file(filename)

    # 获取屏幕截图，保存的是base64的编码格式，在HTML界面输出截图的时候，会用到
    def screenshot_base64(self):
        return self.driver.get_screenshot_as_base64()

    # 获取屏幕截图，保存的是二进制数据，很少用到
    def screenshot_png(self):
        return self.driver.get_screenshot_as_png()

    # 下载文件
    # def download(self):
        # fp = webdriver.FirefoxProfile
        # webdriver.ChromeOptions




