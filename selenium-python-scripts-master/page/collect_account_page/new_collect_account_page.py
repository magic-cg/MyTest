# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewGatherInfoPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 新建
    newBut = (By.CSS_SELECTOR, ".right-buttons>button:nth-child(2)")
    # 户名
    accountName = (By.ID, "name")
    # 银行账号
    accountNo = (By.ID, "cardNo")
    # 保存
    saveBut = (By.CSS_SELECTOR, ".account-create-footer>button:nth-child(2)")
    # 开户行
    openBank = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(2)>div>span>div>div>div>div>div")
    # 选择银行
    selectBank = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(4)>div:nth-child(2)>div>span>div>div>div>div>div>div:nth-child(3)>div>input")
    # 省市
    city = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(5)>div:nth-child(2)>div>span>div>div:nth-child(1)>div>div")
    # 选择省市
    selectCity = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(5)>div:nth-child(2)>div>span>div>div:nth-child(1)>div>div>div>div>div>input")
    # 县区
    county = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(5)>div:nth-child(2)>div>span>div>div:nth-child(2)>div>div")
    # 选择县区
    selectCounty = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(5)>div:nth-child(2)>div>span>div>div:nth-child(2)>div>div>div>div>div>input")
    # 开户网点
    bankBranches = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(6)>div:nth-child(2)>div>span>div>div>div>div")
    # 选择开户网点
    selectBankBranches = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.pt-20>div:nth-child(6)>div:nth-child(2)>div>span>div>div>div>div>div>div:nth-child(3)>div>input")
    # 其他
    elseInfo = (By.CSS_SELECTOR, "input[placeholder='请输入开户网点']")

