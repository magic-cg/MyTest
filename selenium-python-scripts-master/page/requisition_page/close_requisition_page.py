# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class CloseRequisitionPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 申请事项
    requisitionItem = (By.CSS_SELECTOR, ".right-part>div:nth-child(4)")
    # 关闭第一条申请
    closeFirstOne = (By.CSS_SELECTOR, ".apply-list___2YUEt>div:nth-child(2)>div>div:nth-child(1)")
    # 关闭申请
    closeBut = (By.CSS_SELECTOR, ".ant-btn.ant-btn-ghost")
    # 输入申请金额
    inputRequiMoney = (By.ID, "name")
    # 确定
    ensureBut = (By.CSS_SELECTOR, ".requisition-event-close-modal___1uoWs>div:nth-child(3)>button:nth-child(2)")


