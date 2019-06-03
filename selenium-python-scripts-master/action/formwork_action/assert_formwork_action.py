# -*- coding: utf-8 -*-


from page.formwork_page.new_expense_formwork_page import NewExpenseFormWorkPage
from selenium.webdriver.common.keys import Keys
from time import sleep


class GetFormwork:

    def get_formwork_name(self, driver, formwork_name):
        new_exp_work = NewExpenseFormWorkPage(driver)
        # 输入模板名称
        new_exp_work.find_element(NewExpenseFormWorkPage.search).send_keys(formwork_name)
        # 回车
        new_exp_work.find_element(NewExpenseFormWorkPage.search).send_keys(Keys.ENTER)
        sleep(1)
        # 获取搜索到模板名称
        forkwork_name_text = new_exp_work.find_element(NewExpenseFormWorkPage.getFormwork).text
        sleep(1)
        return forkwork_name_text