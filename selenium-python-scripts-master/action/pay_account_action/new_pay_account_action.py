# -*- coding: utf-8 -*-
from page.pay_account_page.new_pay_account_page import NewPayAccountPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.common_menu_page import CommonMenus
from time import sleep


class NewPayAccount:

    def offline_account(self, driver, offline_account_code, offline_account):
        common_menu = CommonMenus(driver)
        new_pay_acc = NewPayAccountPage(driver)
        # 点击菜单栏：企业管理
        ActionChains(driver).move_to_element(common_menu.find_element(CommonMenus.enterpriseManagement)).perform()
        # 点击菜单栏：支付账户
        common_menu.find_element(CommonMenus.paymentAccount).click()
        # 点击新建
        new_pay_acc.find_element(NewPayAccountPage.newPayAccount).click()
        new_pay_acc.find_element(NewPayAccountPage.accountCode).send_keys(offline_account_code)
        new_pay_acc.find_element(NewPayAccountPage.account).send_keys(offline_account)
        # 点击保存
        new_pay_acc.find_element(NewPayAccountPage.saveBut).click()
        sleep(1)
        driver.refresh()
        sleep(5)

    def online_account(self, driver, online_account_code, online_account, online_account_name, online_bank_card_no):
        new_pay_acc = NewPayAccountPage(driver)

        # common_menu = CommonMenus(driver)
        # new_pay_acc = NewPayAccountPage(driver)
        # # 点击菜单栏：企业管理
        # ActionChains(driver).move_to_element(common_menu.find_element(CommonMenus.enterpriseManagement)).perform()
        # # 点击菜单栏：支付账户
        # common_menu.find_element(CommonMenus.paymentAccount).click()

        new_pay_acc.find_element(NewPayAccountPage.newPayAccount).click()
        # 点击在线支付账户
        new_pay_acc.find_element(NewPayAccountPage.onlineBut).click()
        sleep(1)
        # 输入账户编码、名称等
        new_pay_acc.find_element(NewPayAccountPage.accountCode).send_keys(online_account_code)
        new_pay_acc.find_element(NewPayAccountPage.account).send_keys(online_account)
        new_pay_acc.find_element(NewPayAccountPage.accountName).send_keys(online_account_name)
        new_pay_acc.find_element(NewPayAccountPage.bankCardNo).send_keys(online_bank_card_no)
        new_pay_acc.find_element(NewPayAccountPage.openBank).click()
        # 选择开户银行（目前写死了是中国建设银行）
        new_pay_acc.find_element(NewPayAccountPage.selectBank).send_keys(u'中国建设银行')
        sleep(1)
        new_pay_acc.find_element(NewPayAccountPage.selectBank).send_keys(Keys.ENTER)
        # 选择城市区县
        new_pay_acc.find_element(NewPayAccountPage.city).click()
        new_pay_acc.find_element(NewPayAccountPage.selectCity).send_keys(u'北京市')
        new_pay_acc.find_element(NewPayAccountPage.selectCity).send_keys(Keys.ENTER)
        new_pay_acc.find_element(NewPayAccountPage.county).click()
        new_pay_acc.find_element(NewPayAccountPage.selectCounty).send_keys(Keys.ENTER)
        sleep(1)

        # 选择网点（选择中关村支行）
        new_pay_acc.find_element(NewPayAccountPage.bankBranches).click()
        new_pay_acc.find_element(NewPayAccountPage.selectBankBranches).send_keys(u'中关村支行')
        sleep(1)
        new_pay_acc.find_element(NewPayAccountPage.selectBankBranches).send_keys(Keys.ENTER)
        new_pay_acc.find_element(NewPayAccountPage.saveBut).click()
        sleep(1)
        driver.refresh()
        sleep(2)

    def ERP_account(self, driver, ERP_account_code, ERP_account, ERP_account_name, ERP_bank_card_no):

        new_pay_acc = NewPayAccountPage(driver)

        common_menu = CommonMenus(driver)
        new_pay_acc = NewPayAccountPage(driver)
        # 点击菜单栏：企业管理
        ActionChains(driver).move_to_element(common_menu.find_element(CommonMenus.enterpriseManagement)).perform()
        # 点击菜单栏：支付账户
        common_menu.find_element(CommonMenus.paymentAccount).click()

        new_pay_acc.find_element(NewPayAccountPage.newPayAccount).click()
        # 点击在ERP账户
        new_pay_acc.find_element(NewPayAccountPage.ERPBut).click()
        # 输入账户编码、名称等
        new_pay_acc.find_element(NewPayAccountPage.accountCode).send_keys(ERP_account_code)
        new_pay_acc.find_element(NewPayAccountPage.account).send_keys(ERP_account)
        new_pay_acc.find_element(NewPayAccountPage.accountName).send_keys(ERP_account_name)
        new_pay_acc.find_element(NewPayAccountPage.bankCardNo).send_keys(ERP_bank_card_no)
        new_pay_acc.find_element(NewPayAccountPage.openBank).click()
        # 选择开户银行（目前写死了是中国建设银行）
        new_pay_acc.find_element(NewPayAccountPage.selectBank).send_keys(u'中国银行')
        new_pay_acc.find_element(NewPayAccountPage.selectBank).send_keys(Keys.ENTER)
        # 选择城市区县
        new_pay_acc.find_element(NewPayAccountPage.city).click()
        new_pay_acc.find_element(NewPayAccountPage.selectCity).send_keys(u'天津市')
        new_pay_acc.find_element(NewPayAccountPage.selectCity).send_keys(Keys.ENTER)
        new_pay_acc.find_element(NewPayAccountPage.county).click()
        new_pay_acc.find_element(NewPayAccountPage.selectCounty).send_keys(Keys.ENTER)
        sleep(2)

        # 选择网点（选择其他支行）
        new_pay_acc.find_element(NewPayAccountPage.bankBranches).click()
        new_pay_acc.find_element(NewPayAccountPage.selectBankBranches).send_keys(u'其他')
        new_pay_acc.find_element(NewPayAccountPage.selectBankBranches).send_keys(Keys.ENTER)
        new_pay_acc.find_element(NewPayAccountPage.elseInfo).send_keys(u'天津支行')
        new_pay_acc.find_element(NewPayAccountPage.saveBut).click()
        sleep(2)

    def edit_account(self, driver, online_account_code):
        new_pay_acc = NewPayAccountPage(driver)

        # 搜索在线支付的账户
        new_pay_acc.find_element(NewPayAccountPage.searchAccount).send_keys(online_account_code)
        # 编辑，修改银行账户
        new_pay_acc.find_element(NewPayAccountPage.editAccount).click()
        new_pay_acc.find_element(NewPayAccountPage.bankCardNo).clear()
        new_pay_acc.find_element(NewPayAccountPage.bankCardNo).send_keys(622780019900)
        # 保存
        new_pay_acc.find_element(NewPayAccountPage.saveBut).click()
        sleep(2)

    def disable_account(self, driver, ERP_account_code):

        new_pay_acc = NewPayAccountPage(driver)
        # 清空之前的搜索内容
        # new_pay_acc.find_element(NewPayAccountPage.searchAccount).clear()
        # 刷新页面
        driver.refresh()
        sleep(2)
        new_pay_acc.find_element(NewPayAccountPage.searchAccount).send_keys(ERP_account_code)
        new_pay_acc.find_element(NewPayAccountPage.disabledAccount).click()
        new_pay_acc.find_element(NewPayAccountPage.disabledBut).click()
        sleep(2)





