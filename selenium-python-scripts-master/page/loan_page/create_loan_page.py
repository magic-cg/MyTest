# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class CreateLoanPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 新建借款
    newLoan = (By.CLASS_NAME, "loan-hover")
    # 借款单模板
    loanModel = (By.CSS_SELECTOR, "div[style = 'display: block; opacity: 1;")
    # 借款单的标题
    loanTitle = (By.CSS_SELECTOR, "input[placeholder='请输入标题']")
    # 借款金额
    loanMoney = (By.CSS_SELECTOR, "input[placeholder='请输入金额']")
    # 提交送审
    submitLoan = (By.CSS_SELECTOR, ".button_group_wrapper___3M-uZ>button:nth-child(3)")






