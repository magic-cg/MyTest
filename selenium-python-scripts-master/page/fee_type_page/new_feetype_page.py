# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewFeeTypePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 进入费用类型页面后，点击+
    addFee = (By.CSS_SELECTOR, ".feetype-search>button")
    # 输入费用类型名称，目前编码取的是系统默认的
    feeTypeName = (By.CSS_SELECTOR, ".ant-input.input-tags")
    # 保存费用类型的名字
    # saveFeeType = (By.CSS_SELECTOR, ".add-feetype-modal>div:nth-child(3)>button:nth-child(2)")
    saveFeeType = (By.CSS_SELECTOR, ".modal-footer.horizontal>button:nth-child(2)")
    # 报销字段
    expense = (By.CSS_SELECTOR, ".ant-tabs-nav.ant-tabs-nav-animated>div:nth-child(3)")
    # 申请字段
    requisition = (By.CSS_SELECTOR, ".ant-tabs-nav.ant-tabs-nav-animated>div:nth-child(4)")
    # 基本设置-保存
    saveBasicSetting = (By.CSS_SELECTOR, ".ant-col-16.ant-col-offset-4.bd-button>button")
    # 报销字段修改后保存
    save = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-no-animated>div:nth-child(2)>div>div>div:nth-child(2)>div:nth-child(2)>button")
    # 申请字段修改后保存
    saveTwo = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-no-animated>div:nth-child(3)>div>div>div:nth-child(2)>div:nth-child(2)>button")

    # 报销字段页面添加字段
    addField = (By.CSS_SELECTOR, ".simulator-tool-bar>div:nth-child(1)")
    # 申请字段页面添加字段
    addFieldTwo = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-no-animated>div:nth-child(3)>div>div>div:nth-child(1)>div>div:nth-child(1)>div>div:nth-child(2)>div:nth-child(1)")
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
    # 预置金额字段
    presetMoney = (By.CSS_SELECTOR, ".react-grid-layout.ekb-list-layout>div:nth-child(1)>div>div>div>div")
    # 勾选自动计算
    autCalculation = (By.CSS_SELECTOR, ".ant-radio-group.radio-group-wrapper___fTZ0q>label:nth-child(2)>span>input")
    # 点击自动计算
    clickAutCalculation = (By.CSS_SELECTOR, ".content_obj>span")
    # 公式中的数量
    clickNum = (By.CSS_SELECTOR, ".computer-obj-wrapper>div:nth-child(2)")
    # 公式中的单价
    clickMoney = (By.CSS_SELECTOR, ".computer-obj-wrapper>div:nth-child(3)")
    # 公式中的乘号
    xSymbol = (By.CSS_SELECTOR, ".symbol0>div:nth-child(4)")
    # 公式中的加号
    plusSign = (By.CSS_SELECTOR, ".symbol0>div:nth-child(2)")
    # 公式确定
    formulaEnsure = (By.CSS_SELECTOR, ".computer-modal-wrapper___13K6n>div:nth-child(3)>button:nth-child(2)")
    # 搜索费用类型
    searchFeeType = (By.CSS_SELECTOR, "input[placeholder='输入名称或编码进行搜索']")
    # 一级费用类型确定操作
    ensureSearchFeeTypeOne = (By.CSS_SELECTOR, ".type-name")
    # 二级费用类型确定操作
    ensureSearchFeeTypeTwo = (By.CSS_SELECTOR, ".node-1>span:nth-child(2)>span>div>div:nth-child(2)>div")