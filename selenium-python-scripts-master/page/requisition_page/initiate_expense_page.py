# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class InitiateExpensePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 申请事项
    requisitionItem = (By.CSS_SELECTOR, ".right-part>div:nth-child(4)")
    # 第一条申请发起还款
    initiateFirstOne = (By.CSS_SELECTOR, ".apply-list___2YUEt>div:nth-child(2)>div>div:nth-child(1)")
    # 发起报销
    initiateRequisition = (By.CSS_SELECTOR, ".ant-btn.ant-btn-primary")
    # 关闭申请
    closeRequisition = (By.CSS_SELECTOR, ".footer>div>button:nth-child(2)")
    # 共享
    shareRequisition = (By.CSS_SELECTOR, ".footer>div>button:nth-child(3)")
    # 转交
    shiftRequisition = (By.CSS_SELECTOR, ".footer>div>button:nth-child(4)")
    # 添加共享人
    addSharer = (By.CSS_SELECTOR, ".tag-selector>button")
    # 确认共享人
    ensure = (By.CSS_SELECTOR, ".modal-footer>button:nth-child(2)")
    # 选择转交人
    selectShifter = (By.CSS_SELECTOR, "input[placeholder='请选择员工']")

    # dict = {'requisitionItem': requisitionItem,
    #                  'initiateFirstOne': initiateFirstOne,
    #                  'initiateRequisition': initiateRequisition,
    #                  }


    