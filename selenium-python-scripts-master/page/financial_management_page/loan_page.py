# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class LoanPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # 待还款/进行中
    waitToPay = (By.CSS_SELECTOR, ".ant-tabs-nav-scroll>div>div:nth-child(3)")
    # 已完成/已关闭
    done = (By.CSS_SELECTOR, ".ant-tabs-nav-scroll>div>div:nth-child(4)")

