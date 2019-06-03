# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewLoanFormWorkPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # +号
    add = (By.CSS_SELECTOR, ".box-content-left___1BJ3c>div>div>i")
    # 新增借款单模板
    addLoan = (By.CSS_SELECTOR, ".add-card>div:nth-child(2)")
    # 借款单类型模板名称
    loanFormWorkTypeName = (By.CSS_SELECTOR, ".mt-40>div>div>div:nth-child(2)>div>span>input")
    # 审批流程
    loanFlow = (By.CSS_SELECTOR, ".mt-40>div>div:nth-child(2)>div:nth-child(2)>div>span>div")
    # 选择新建的审批流
    # selectExpFlow = (By.CSS_SELECTOR, "div[style='overflow: auto;']>ul>li:nth-child(2)")
    selectLoanFlow = (By.XPATH, "//div[7]/div/div/div/ul/li[1]")
    # 打印模板
    printModel = (By.CSS_SELECTOR, ".dis-f.jc-sb>div:nth-child(1)>div>div:nth-child(1)")
    # self.printModelLoc = (By.XPATH, "//div[3]/div[2]/div/div/div/div/div")
    # 选择某一模板
    # self.selectPrintModelLoc = (By.CSS_SELECTOR, "div[style='overflow: auto;']>ul>li:nth-child(2)")
    selectPrintModel = (By.XPATH, "//div[8]/div/div/div/ul/li[1]")
    # 限制可见范围

    # 是否填写收款信息
    payeeInfo = (By.CSS_SELECTOR, ".mt-40>div>div:nth-child(6)>div>div>span>div>label>span>input")
    # 保存借款单模板
    saveLoanFormWork = (By.CSS_SELECTOR, ".actions-part___2Xxwy>button:nth-child(3)")
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
    # dict = {'add': self.add,
    #                  'addLoan': self.addLoan,
    #                  'loanFormWorkTypeName': self.loanFormWorkTypeName,
    #                  'loanFlow': self.loanFlow,
    #                  'selectLoanFlow': self.selectLoanFlow,
    #                  'printModel': self.printModel,
    #                  'selectPrintModel': self.selectPrintModel,
    #                  'payeeInfo': self.payeeInfo,
    #                  'saveLoanFormWork': self.saveLoanFormWork,
    #                  'fieldSetting': self.fieldSetting,
    #                  'addField': self.addField,
    #                  'divider': self.divider,
    #                  'explanatoryText': self.explanatoryText,
    #                  'searchField': self.searchField,
    #                  'ensureSearchField': self.ensureSearchField,
    #                  'ensureBut': self.ensureBut
    #                  }


