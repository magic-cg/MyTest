# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewSubsidyStandard(BasePage):
    def __init__(self, driver):
        self.driver = driver
        # 补助金额
    subsidyMoney = (By.CSS_SELECTOR, ".number_wrap>div>div:nth-child(2)>input")
    # dict = {'subsidyMoney': self.subsidyMoneyLoc
    #                  }
