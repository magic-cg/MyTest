# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewRequisitionFormWorkPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # +号
    add = (By.CSS_SELECTOR, ".box-content-left___1BJ3c>div>div>i")
    # 新增申请单模板
    addRequisition = (By.CSS_SELECTOR, ".add-card>div:nth-child(3)")
    # 申请单类型模板名称
    requisitionFormWorkTypeName = (By.CSS_SELECTOR, ".mt-40>div>div>div:nth-child(2)>div>span>input")
    # 审批流程
    requisitionFlow = (By.CSS_SELECTOR, ".mt-40>div>div:nth-child(2)>div:nth-child(2)>div>span>div")
    # 选择新建的审批流
    selectRequisitionFlow = (By.XPATH, "//div[7]/div/div/div/ul/li[1]")
    # 打印模板
    printModel = (By.CSS_SELECTOR, ".dis-f.jc-sb>div:nth-child(1)>div>div:nth-child(1)")
    # 选择某一模板
    selectPrintModel = (By.XPATH, "//div[8]/div/div/div/ul/li[1]")
    # 限制可见范围
    # 申请内容-直接填写金额
    requisitionContent1 = (By.CSS_SELECTOR, ".mt-40>div>div:nth-child(5)>div:nth-child(2)>div>span>div>label:nth-child(1)")
    # 申请内容-直接填写行程
    requisitionContent3 = (By.CSS_SELECTOR, ".mt-40>div>div:nth-child(5)>div:nth-child(2)>div>span>div>label:nth-child(3)")
    # 申请内容-填写申请金额和差旅行程
    requisitionContent4 = (By.CSS_SELECTOR, ".mt-40>div>div:nth-child(5)>div:nth-child(2)>div>span>div>label:nth-child(4)")
    # 申请关闭方式-报销金额≥申请金额时自动关闭
    closeRequisitionRule2 = (By.CSS_SELECTOR, ".mt-40>div>div:nth-child(7)>div>div>span>div>label:nth-child(2)")
    # 申请关闭方式-达到报销次数自动关闭
    closeRequisitionRule3 = (By.CSS_SELECTOR, ".mt-40>div>div:nth-child(7)>div>div>span>div>label:nth-child(3)")
    # 保存申请单模板
    saveRequisitionFormWork = (By.CSS_SELECTOR, ".actions-part___2Xxwy>button:nth-child(3)")
    # 字段设置
    fieldSetting = (By.CSS_SELECTOR, ".ant-tabs-nav.ant-tabs-nav-animated>div:nth-child(3)")
    # 添加字段
    addField = (By.CSS_SELECTOR, ".simulator-tool-bar>div:nth-child(1)")
    # 添加分割线
    divider = (By.CSS_SELECTOR, ".simulator-tool-bar>div:nth-child(5)")
    # 添加说明文本
    explanatoryText = (By.CSS_SELECTOR, ".simulator-tool-bar>div:nth-child(3)")
    # 搜索字段名称
    searchField = (By.CSS_SELECTOR, "input[placeholder='搜索字段名称']")
    # 选中搜索的字段
    ensureSearchField = (By.CSS_SELECTOR, ".field-item>div")
    # 确定
    ensureBut = (By.CSS_SELECTOR, ".custom-field-modal>div:nth-child(2)>div:nth-child(2)>button:nth-child(3)")

