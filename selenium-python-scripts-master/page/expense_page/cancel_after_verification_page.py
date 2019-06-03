# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewExpenseWithCancelAfterVerificationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        # 添加核销
    addCancelAfterVerification = (By.CSS_SELECTOR, ".empty-btn")
    # 勾选核销的借款
    clickOn = (By.CSS_SELECTOR, ".check-button.ant-checkbox-wrapper>span>input")
    # 确定
    ensureBut = (By.CSS_SELECTOR, ".ant-btn.btn-ml.ant-btn-primary")
    # self.dict = {'addCancelAfterVerification': self.addCancelAfterVerification,
    #              'clickOn': self.clickOn,
    #              'ensureBut': self.ensureBut
    #              }
