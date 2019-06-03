# -*- coding: utf-8 -*-
from common.common_menu_page import CommonMenus
from page.financial_management_page.loan_page import LoanPage
from time import sleep


class Export:
    def expense_export(self, driver):
        common_menu = CommonMenus(driver)
        # 进入报销单管理页面
        common_menu.find_element(CommonMenus.financeManagement).click()
        common_menu.find_element(CommonMenus.expenseManagement).click()
        sleep(1)

    def loan_doing_export(self, driver):
        # 进入借款管理-申请中
        common_menu = CommonMenus(driver)
        common_menu.find_element(CommonMenus.financeManagement).click()
        common_menu.find_element(CommonMenus.loanManagement).click()

    def loan_wait_export(self, driver):
        # 进入借款管理-待还款
        loan_page = LoanPage(driver)
        common_menu = CommonMenus(driver)
        common_menu.find_element(CommonMenus.financeManagement).click()
        common_menu.find_element(CommonMenus.loanManagement).click()
        sleep(1)
        loan_page.find_element(LoanPage.waitToPay).click()
        sleep(1)

    def loan_done_export(self, driver):
        # 进入借款管理-已完成
        loan_page = LoanPage(driver)
        loan_page.find_element(LoanPage.done).click()

    def requisition_doing_export(self, driver):
        # 进入申请管理-申请中
        common_menu = CommonMenus(driver)
        common_menu.find_element(CommonMenus.financeManagement).click()
        common_menu.find_element(CommonMenus.applicationManagement).click()

    def requisition_wait_export(self, driver):
        # 进入申请管理-进行中
        loan_page = LoanPage(driver)
        common_menu = CommonMenus(driver)
        common_menu.find_element(CommonMenus.financeManagement).click()
        common_menu.find_element(CommonMenus.applicationManagement).click()
        sleep(1)
        loan_page.find_element(LoanPage.waitToPay).click()
        sleep(1)

    def requisition_done_export(self, driver):
        # 进入申请管理-已关闭
        loan_page = LoanPage(driver)
        loan_page.find_element(LoanPage.done).click()







