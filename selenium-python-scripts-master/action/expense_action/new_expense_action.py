# -*- coding: utf-8 -*-
from page.expense_page.create_expense_page import NewExpensePage
from time import sleep
import config.global_variable as gv


class NewExpenseAction:

    def new_expense_button(self, driver):
        new_exp = NewExpensePage(driver)
        new_exp.find_element(NewExpensePage.newExpense).click()

    def new_expense(self, driver, exp_title):
        new_exp = NewExpensePage(driver)

        # 由于单据模板列表下好多单据，根据单据名称来选择想要的模板

        new_exp.find_element1(NewExpensePage.chooseModel).click()
        sleep(2)
        select_model = driver.find_element_by_css_selector("ul[role = 'listbox']")

        allOption = select_model.find_elements_by_tag_name("li")
        for option in allOption:
            # print "Value is: " + option.get_attribute("value")
            # print "Text is:" + option.text
            if gv.exp_model_name1 in option.text:
                option.click()
                break

        # 填写报销单中的字段,标题、描述等
        new_exp.find_element(NewExpensePage.expenseTitle).send_keys(exp_title)

        # new_exp.find_element('describe').send_keys(exp_describe)
        sleep(1)

    def write_fee_type(self, driver):
        # 点击填写费用明细按钮
        new_exp = NewExpensePage(driver)
        new_exp.find_element(NewExpensePage.costDetail).click()
        sleep(2)

    def simple_fee_type(self, driver, exp_amount, fee_type1):
        new_exp = NewExpensePage(driver)

        # 选择费用类型

        new_exp.find_element1(NewExpensePage.feeType).click()
        sleep(1)
        # 清空费用类型搜索
        new_exp.find_element1(NewExpensePage.selectFeeType).clear()

        new_exp.find_element1(NewExpensePage.selectFeeType).click()
        new_exp.find_element1(NewExpensePage.selectFeeType).send_keys(fee_type1)
        new_exp.find_element1(NewExpensePage.ensureFeeType).click()
        sleep(1)
        # 填写费用金额
        new_exp.find_element(NewExpensePage.expenseAmount).send_keys(exp_amount)


    def flight_field(self, driver):
        new_exp = NewExpensePage(driver)
        # 点击航班字段
        new_exp.find_element(NewExpensePage.flightSta).click()



    # 保存费用类型
    def save(self, driver):
        new_exp = NewExpensePage(driver)
        new_exp.find_element(NewExpensePage.saveCostDetail).click()
        sleep(2)

    # 再记一笔
    def write_other(self, driver):
        new_exp = NewExpensePage(driver)
        new_exp.find_element(NewExpensePage.writeAgain).click()

    # 自动计算
    def auto_fee_type(self, driver, fee_type2):
        new_exp = NewExpensePage(driver)

        # 带有自动计算的费用类型
        new_exp.find_element(NewExpensePage.feeType).click()
        sleep(1)
        # 清除第一次选择的费用类型,若没有，也可做一次清除动作
        new_exp.find_element(NewExpensePage.selectFeeType).clear()
        sleep(1)
        new_exp.find_element(NewExpensePage.selectFeeType).send_keys(fee_type2)
        new_exp.find_element(NewExpensePage.ensureFeeType).click()
        sleep(2)
        new_exp.find_element(NewExpensePage.unitPrice).send_keys('2')
        new_exp.find_element(NewExpensePage.quantity).send_keys('5')
        sleep(2)
        # amount_result = new_exp.find_element(NewExpensePage.autExpenseAmount).text
        # result2 = new_exp.find_element(NewExpensePage.quantity).text

    def new_project_field(self, driver, project_name):
        new_exp = NewExpensePage(driver)
        new_exp.find_element(NewExpensePage.project).click()
        # 项目
        new_exp.find_element(NewExpensePage.selectProject).send_keys(project_name)
        new_exp.find_element(NewExpensePage.ensureProject).click()
        sleep(2)



