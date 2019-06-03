# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class Permissions(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # 系统管理-编辑
    editOne = (By.CSS_SELECTOR, ".ant-table-tbody>tr:nth-child(1)>td:nth-child(2)>div>div:nth-child(2)>a")
    # 费用报表查看-编辑
    editTwo = (By.CSS_SELECTOR, ".ant-table-tbody>tr:nth-child(2)>td:nth-child(2)>div>div:nth-child(2)>a")
    # 报销单管理-编辑
    editThree = (By.CSS_SELECTOR, ".ant-table-tbody>tr:nth-child(3)>td:nth-child(2)>div>div:nth-child(2)>a")
    # 借款单管理-编辑
    editFour = (By.CSS_SELECTOR, ".ant-table-tbody>tr:nth-child(4)>td:nth-child(2)>div>div:nth-child(2)>a")
    # 申请单管理-编辑
    editFive = (By.CSS_SELECTOR, ".ant-table-tbody>tr:nth-child(5)>td:nth-child(2)>div>div:nth-child(2)>a")
    # 预算管理-编辑
    editSix = (By.CSS_SELECTOR, ".ant-table-tbody>tr:nth-child(6)>td:nth-child(2)>div>div:nth-child(2)>a")
    # 高级报表-编辑
    editSeven = (By.CSS_SELECTOR, ".ant-table-tbody>tr:nth-child(7)>td:nth-child(2)>div>div:nth-child(2)>a")

