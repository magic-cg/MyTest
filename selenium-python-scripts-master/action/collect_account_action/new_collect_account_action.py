# -*- coding: utf-8 -*-
from page.pay_account_page.new_pay_account_page import NewPayAccountPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.common_menu_page import CommonMenus
from page.collect_account_page.new_collect_account_page import NewGatherInfoPage
from time import sleep


class NewCollectAccount:

    def collect_account(self, driver, account_name, bank_card_no):

        common_menu = CommonMenus(driver)
        new_pay_acc = NewPayAccountPage(driver)
        new_coll_acc = NewGatherInfoPage(driver)
        # 点击菜单栏：企业管理
        ActionChains(driver).move_to_element(common_menu.find_element(CommonMenus.enterpriseManagement)).perform()
        # 点击菜单栏：收款信息
        common_menu.find_element(CommonMenus.collInfo).click()

        # 新建个人账户
        new_coll_acc.find_element(NewGatherInfoPage.newBut).click()
        # 输入户名和账号
        new_coll_acc.find_element(NewGatherInfoPage.accountName).send_keys(account_name)
        new_coll_acc.find_element(NewGatherInfoPage.accountNo).send_keys(bank_card_no)

        # 选择开户银行（目前写死了是中国建设银行）
        new_pay_acc.find_element(NewGatherInfoPage.openBank).click()
        new_pay_acc.find_element(NewGatherInfoPage.selectBank).send_keys(u'中国建设银行')
        sleep(1)
        new_pay_acc.find_element(NewGatherInfoPage.selectBank).send_keys(Keys.ENTER)
        # 选择城市区县
        new_pay_acc.find_element(NewGatherInfoPage.city).click()
        new_pay_acc.find_element(NewGatherInfoPage.selectCity).send_keys(u'北京市')
        new_pay_acc.find_element(NewGatherInfoPage.selectCity).send_keys(Keys.ENTER)
        new_pay_acc.find_element(NewGatherInfoPage.county).click()
        new_pay_acc.find_element(NewGatherInfoPage.selectCounty).send_keys(Keys.ENTER)
        sleep(1)

        # 选择网点（选择中关村支行）
        new_pay_acc.find_element(NewGatherInfoPage.bankBranches).click()
        new_pay_acc.find_element(NewGatherInfoPage.selectBankBranches).send_keys(u'中关村支行')
        sleep(1)
        new_pay_acc.find_element(NewGatherInfoPage.selectBankBranches).send_keys(Keys.ENTER)
        new_pay_acc.find_element(NewGatherInfoPage.saveBut).click()
        sleep(1)
        driver.refresh()
        sleep(2)








