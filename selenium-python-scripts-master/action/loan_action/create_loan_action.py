# -*- coding: utf-8 -*-
from time import sleep

from page.loan_page.create_loan_page import CreateLoanPage
import config.global_variable as gv


class LoanAction:
    # 点击新建借款

    def create_new_loan(self, driver, input_loan_title, input_loan_amount):
        create_loan = CreateLoanPage(driver)
        create_loan.find_element(CreateLoanPage.newLoan).click()
        # 选择借款单模板
        create_loan.find_element(CreateLoanPage.loanModel).click()
        sleep(2)
        select_model = driver.find_element_by_css_selector("ul[role = 'listbox']")
        allOption = select_model.find_elements_by_tag_name("li")
        for option in allOption:
            if gv.loan_model_name1 in option.text:
                option.click()
                break
        # 输入借款单标题
        create_loan.find_element(CreateLoanPage.loanTitle).send_keys(input_loan_title)
        # 输入借款金额
        create_loan.find_element(CreateLoanPage.loanMoney).send_keys(input_loan_amount)
        # 暂时先无其他参数参与

    def create_new_loan1(self, driver, input_loan_title, input_loan_amount):
        create_loan = CreateLoanPage(driver)
        create_loan.find_element(CreateLoanPage.newLoan).click()
        # 选择借款单模板
        create_loan.find_element(CreateLoanPage.loanModel).click()
        sleep(2)
        select_model = driver.find_element_by_css_selector("ul[role = 'listbox']")
        allOption = select_model.find_elements_by_tag_name("li")
        for option in allOption:
            if gv.loan_model_name2 in option.text:
                option.click()
                break
        # 输入借款单标题
        create_loan.find_element(CreateLoanPage.loanTitle).send_keys(input_loan_title)
        # 输入借款金额
        create_loan.find_element(CreateLoanPage.loanMoney).send_keys(input_loan_amount)
        # 暂时先无其他参数参与





















