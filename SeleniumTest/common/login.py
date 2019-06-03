# -*- coding: utf-8 -*-

from selenium import webdriver

def get_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    return driver