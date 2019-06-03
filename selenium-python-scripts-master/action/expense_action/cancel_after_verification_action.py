# -*- coding: utf-8 -*-
from time import sleep
from page.expense_page.create_expense_page import NewExpensePage
from page.expense_page.cancel_after_verification_page import NewExpenseWithCancelAfterVerificationPage
from common.common_flow_page import FlowPage


class NewExpenseWithCancelAfterVerificationAction:

    def new_expense_with_cancel(self, driver, exp_title, exp_amount, exp_fee_type, project_name):
        new_exp = NewExpensePage(driver)
        new_expense_with = NewExpenseWithCancelAfterVerificationPage(driver)
        # 新建报销单
        new_exp.find_element(NewExpensePage.newExpense).click()
        # 填写标题、费用明细等
        new_exp.find_element(NewExpensePage.expenseTitle).send_keys(exp_title)
        # new_exp.find_element('describe').send_keys(exp_describe)
        sleep(1)

        new_exp.find_element(NewExpensePage.costDetail).click()

        new_exp.find_element1(NewExpensePage.feeType).click()
        sleep(1)
        new_exp.find_element1(NewExpensePage.selectFeeType).send_keys(exp_fee_type)
        new_exp.find_element1(NewExpensePage.ensureFeeType).click()
        sleep(1)
        # 填写费用金额
        new_exp.find_element(NewExpensePage.expenseAmount).send_keys(exp_amount)
        # 保存
        new_exp.find_element(NewExpensePage.saveCostDetail).click()
        sleep(3)
        # 填写项目、航班等字段
        new_exp.find_element(NewExpensePage.project).click()
        # 项目
        new_exp.find_element(NewExpensePage.selectProject).send_keys(project_name)
        new_exp.find_element(NewExpensePage.ensureProject).click()

        # 添加核销
        new_expense_with.find_element(NewExpenseWithCancelAfterVerificationPage.addCancelAfterVerification).click()
        new_expense_with.find_element(NewExpenseWithCancelAfterVerificationPage.clickOn).click()
        new_expense_with.find_element(NewExpenseWithCancelAfterVerificationPage.ensureBut).click()
        sleep(2)

    def submit_expense(self, driver, input_approve_person):

        flow = FlowPage(driver)
        new_exp = NewExpensePage(driver)
        # 提交送审报销单
        new_exp.find_element(NewExpensePage.submitExpense).click()
        flow.find_element(FlowPage.selectFirstPerson).click()
        flow.find_element(FlowPage.searchPerson).send_keys(input_approve_person)
        flow.find_element(FlowPage.getPerson).click()
        flow.find_element(FlowPage.makeSureBut).click()
        flow.find_element(FlowPage.selectFirstPersonBut).click()
        sleep(2)