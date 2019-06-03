# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class BaiduPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    kw = (By.ID,"kw")
    su = (By.ID,"su")
