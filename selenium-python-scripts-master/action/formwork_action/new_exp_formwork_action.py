# -*- coding: utf-8 -*-
from  selenium.webdriver.common.keys import Keys
from common.common_menu_page import CommonMenus
from page.formwork_page.new_expense_formwork_page import NewExpenseFormWorkPage
from time import sleep
import config.global_variable as gv


class NewExpenseFormWorkAction:

    # 进入到单据类型模块
    def enter_exp_formwork(self, driver):
        common_menus = CommonMenus(driver)
        common_menus.find_element(CommonMenus.enterpriseManagement).click()
        common_menus.find_element(CommonMenus.documentType).click()

    # 新建报销单
    def new_exp_formwork(self, driver, exp_model_name):

        new_expense_formwork = NewExpenseFormWorkPage(driver)
        # 新建报销单模板
        new_expense_formwork.find_element(NewExpenseFormWorkPage.add).click()
        new_expense_formwork.find_element1(NewExpenseFormWorkPage.addExp).click()
        # 报销单模板名字
        new_expense_formwork.find_element(NewExpenseFormWorkPage.expFormWorkTypeName).send_keys(exp_model_name)

    def exp_flow(self, driver):

        # 选择审批流
        new_expense_formwork = NewExpenseFormWorkPage(driver)

        new_expense_formwork.find_element(NewExpenseFormWorkPage.expFlow).click()
        sleep(1)
        select_flow = driver.find_element_by_css_selector("ul[role = 'listbox']")

        allOption = select_flow.find_elements_by_tag_name("li")
        for option in allOption:
            # print "Value is: " + option.get_attribute("value")
            # print "Text is:" + option.text
            if gv.flow_name1 in option.text:
                option.click()
                break

    # 后期此块需优化，分成不同的方法
    def other(self, driver):
        new_expense_formwork = NewExpenseFormWorkPage(driver)

        # 选择打印模板
        new_expense_formwork.find_element(NewExpenseFormWorkPage.printModel).click()
        new_expense_formwork.find_element(NewExpenseFormWorkPage.selectPrintModel).click()
        # 不勾选收款信息
        new_expense_formwork.find_element(NewExpenseFormWorkPage.payeeInfo).click()
        sleep(2)

    def field_setting(self, driver):

        # 报销单模板字段设置中增加自定义字段
        new_expense_formwork = NewExpenseFormWorkPage(driver)
        new_expense_formwork.find_element(NewExpenseFormWorkPage.fieldSetting).click()
        sleep(2)
        list_exp_add = [u'项目']
        for i in range(len(list_exp_add)):
            new_expense_formwork.find_element(NewExpenseFormWorkPage.addField).click()
            new_expense_formwork.find_element(NewExpenseFormWorkPage.searchField).send_keys(list_exp_add[i])
            new_expense_formwork.find_element(NewExpenseFormWorkPage.ensureSearchField).click()
            new_expense_formwork.find_element(NewExpenseFormWorkPage.ensureBut).click()
            sleep(1)

    def explanatory(self, driver):
        # 添加说明文本
        new_expense_formwork = NewExpenseFormWorkPage(driver)

        new_expense_formwork.find_element(NewExpenseFormWorkPage.explanatoryText).click()

    def divider(self, driver):
        # 添加分割线
        new_expense_formwork = NewExpenseFormWorkPage(driver)

        new_expense_formwork.find_element(NewExpenseFormWorkPage.divider).click()

    def save(self, driver):

        # 保存
        new_expense_formwork = NewExpenseFormWorkPage(driver)

        new_expense_formwork.find_element(NewExpenseFormWorkPage.saveExpFormWork).click()
        sleep(2)


    def exp_flow1(self, driver):

        # 选择审批流
        new_expense_formwork = NewExpenseFormWorkPage(driver)

        new_expense_formwork.find_element(NewExpenseFormWorkPage.expFlow).click()
        sleep(1)
        select_flow = driver.find_element_by_css_selector("ul[role = 'listbox']")

        allOption = select_flow.find_elements_by_tag_name("li")
        for option in allOption:
            # print "Value is: " + option.get_attribute("value")
            # print "Text is:" + option.text
            if gv.flow_name2 in option.text:
                option.click()
                break


