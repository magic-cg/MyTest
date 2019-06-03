# -*- coding: utf-8 -*-
from common.common_menu_page import CommonMenus
from page.formwork_page.new_loan_formwork_page import NewLoanFormWorkPage
import config.global_variable as gv
from time import sleep


class NewLoanFormWorkAction:

    # 进入到单据类型模块
    def enter_loan_formwork(self, driver):
        common_menus = CommonMenus(driver)
        common_menus.find_element(CommonMenus.enterpriseManagement).click()
        common_menus.find_element(CommonMenus.documentType).click()

    # 新建借款单
    def new_loan_formwork(self, driver, loan_model_name):

        new_loan_fw = NewLoanFormWorkPage(driver)
        # 新建借款单模板
        new_loan_fw.find_element(NewLoanFormWorkPage.add).click()
        new_loan_fw.find_element1(NewLoanFormWorkPage.addLoan).click()
        # 借款单模板名字
        new_loan_fw.find_element(NewLoanFormWorkPage.loanFormWorkTypeName).send_keys(loan_model_name)

    def loan_flow(self, driver):
        new_loan_fw = NewLoanFormWorkPage(driver)

        # 选择审批流
        new_loan_fw.find_element(NewLoanFormWorkPage.loanFlow).click()
        sleep(1)
        select_flow = driver.find_element_by_css_selector("ul[role = 'listbox']")

        allOption = select_flow.find_elements_by_tag_name("li")
        for option in allOption:
            # print "Value is: " + option.get_attribute("value")
            # print "Text is:" + option.text
            if gv.flow_name1 in option.text:
                option.click()
                break

    def other(self, driver):
        new_loan_fw = NewLoanFormWorkPage(driver)

        # 选择打印模板
        new_loan_fw.find_element(NewLoanFormWorkPage.printModel).click()
        new_loan_fw.find_element(NewLoanFormWorkPage.selectPrintModel).click()
        # 不勾选收款信息
        new_loan_fw.find_element(NewLoanFormWorkPage.payeeInfo).click()
        sleep(1)

    def save(self, driver):

        # 保存
        new_loan_fw = NewLoanFormWorkPage(driver)

        new_loan_fw.find_element(NewLoanFormWorkPage.saveLoanFormWork).click()
        sleep(2)

    def loan_flow1(self, driver):
        new_loan_fw = NewLoanFormWorkPage(driver)

        # 选择审批流
        new_loan_fw.find_element(NewLoanFormWorkPage.loanFlow).click()
        sleep(1)
        select_flow = driver.find_element_by_css_selector("ul[role = 'listbox']")

        allOption = select_flow.find_elements_by_tag_name("li")
        for option in allOption:
            # print "Value is: " + option.get_attribute("value")
            # print "Text is:" + option.text
            if gv.flow_name2 in option.text:
                option.click()
                break



