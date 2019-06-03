# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class AttachmentPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    # 上传附件
    uploadAttachment = (By.CSS_SELECTOR, ".ekb-files-input")
    # 以借款管理为例，申请中页面，选中当前第一页
    selectCurrent = (By.CSS_SELECTOR, ".ant-table-thead>tr>th:nth-child(1)>span>div>label>span>input")
    # 以借款管理为例，待还款页面，选中当前第一页
    selectCurrentTwo = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-animated>div:nth-child(2)>div>div>div:nth-child(3)>div>div>div>div>div>div>div>div>table>thead:nth-child(2)>tr>th:nth-child(1)>span>div>label>span>input")
    # 以借款管理为例，已完成页面，选中当前第一页
    selectCurrentThree = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-animated>div:nth-child(3)>div>div>div:nth-child(3)>div>div>div>div>div>div>div>div>table>thead:nth-child(2)>tr>th:nth-child(1)>span>div>label>span>input")

    # 以借款管理为例，申请中页面，导出选中
    exportSelect = (By.NAME, "export_selected")
    # 以借款管理为例，待还款页面，导出选中
    exportSelectTwo = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-animated>div:nth-child(2)>div>div>div:nth-child(4)>div:nth-child(1)>div>button")
    # 以借款管理为例，已完成页面，导出选中
    exportSelectThree = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-animated>div:nth-child(3)>div>div>div:nth-child(4)>div:nth-child(1)>div>button")

    # 导出全部
    exportAll = (By.NAME, "export_all")
    # 导出选中操作下的导出按钮
    exportButOne = (By.CSS_SELECTOR, ".export-excel-modal___eAT4m>div:nth-child(3)>button:nth-child(2)")
    # 借款管理--申请中选择全部X项
    selectAllOne = (By.CSS_SELECTOR, ".selectAllBtn___2yowL")
    # 借款管理--待还款选择全部X项
    selectAllTwo = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-animated>div:nth-child(2)>div>div>div:nth-child(4)>div>span:nth-child(2)")
    # 借款管理--已完成选择全部X项
    selectAllThree = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-animated>div:nth-child(3)>div>div>div:nth-child(4)>div>span:nth-child(2)")
    # 选择全部X项的导出
    exportButTWo = (By.CSS_SELECTOR, ".action-box>button:nth-child(1)")

