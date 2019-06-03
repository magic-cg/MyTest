# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewPayAccountPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 新建支付账户
    newPayAccount = (By.CSS_SELECTOR, ".right-buttons>button:nth-child(2)")
    # 新建线下支付账户
    # 账户编码
    accountCode = (By.ID, "code")
    # 账户名称
    account = (By.ID, "name")
    # 保存按钮
    saveBut = (By.CSS_SELECTOR, ".ant-btn.mr-10.ant-btn-primary.ant-btn-lg")
    # 在线支付按钮
    onlineBut = (By.CSS_SELECTOR, ".ant-checkbox-group.ekb-select-third-payment-method>label:nth-child(2)>span:nth-child(2)")
    # 点击ERP账户
    ERPBut = (By.CSS_SELECTOR, ".ant-checkbox-group.ekb-select-third-payment-method>label:nth-child(3)>span:nth-child(2)>div")
    # 开户行
    openBank = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(3)>div:nth-child(2)>div>span>div>div>div>div>span")
    # 支付账户-输入银行
    selectBank = (By.CSS_SELECTOR,".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(3)>div:nth-child(2)>div>span>div>div>div>div>div>div:nth-child(3)>div>input")
    # 户名
    accountName = (By.ID, "detail.name")
    # 银行账号
    bankCardNo = (By.ID, "detail.number")
    # 省市
    city = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(4)>div:nth-child(2)>div>span>div>div:nth-child(1)>div>div>span")
    selectCity = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(4)>div:nth-child(2)>div>span>div>div:nth-child(1)>div>div>div>div>div>input")
    # 县区
    county = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(4)>div:nth-child(2)>div>span>div>div:nth-child(2)>div>div>span")
    selectCounty = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(4)>div:nth-child(2)>div>span>div>div:nth-child(2)>div>div>div>div>div>input")
    # 开户网点
    bankBranches = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(5)>div:nth-child(2)>div>span>div>div>div>div>span")
    selectBankBranches = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(5)>div:nth-child(2)>div>span>div>div>div>div>div>div:nth-child(3)>div>input")
    # 其他
    elseInfo = (By.CSS_SELECTOR, "input[placeholder='请输入开户网点']")
    # 搜索
    searchAccount = (By.CSS_SELECTOR, "input[placeholder='搜索支付账户名称或编码']")
    # 编辑
    editAccount = (By.CSS_SELECTOR, ".left-part>div:nth-child(2)")
    # 停用
    disabledAccount = (By.CSS_SELECTOR, ".enable-switch.ant-switch.ant-switch-checked")
    # 确定停用
    disabledBut = (By.CSS_SELECTOR, ".ant-confirm-btns>button:nth-child(2)")
    # dict = {'newPayAccount': newPayAccount,
    #              'accountCode': accountCode,
    #              'account': account,
    #              'saveBut': saveBut,
    #              'onlineBut': onlineBut,
    #              'ERPBut': ERPBut,
    #              'openBank': openBank,
    #              'selectBank': selectBank,
    #              'accountName': accountName,
    #              'bankCardNo': bankCardNo,
    #              'city': city,
    #              'selectCity': selectCity,
    #              'county': county,
    #              'selectCounty': selectCounty,
    #              'bankBranches': bankBranches,
    #              'selectBankBranches': selectBankBranches,
    #              'elseInfo': elseInfo,
    #              'searchAccount': searchAccount,
    #              'editAccount': editAccount,
    #              'disabledAccount': disabledAccount,
    #              'disabledBut': disabledBut
    #              }

