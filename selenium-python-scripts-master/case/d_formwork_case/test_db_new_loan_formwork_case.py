# -*- coding: utf-8 -*-
import unittest
import action.formwork_action.new_loan_formwork_action as nlfa
import config.global_variable as gv
import common.login
from time import sleep
from common.assertion import Assertion
from action.formwork_action.assert_formwork_action import GetFormwork


class NewLoanFormWorkCase(unittest.TestCase):

    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    # 新建报销单模板
    def test_new_loan_formwork(self):
        new_loan_fw = nlfa.NewLoanFormWorkAction()
        get_form = GetFormwork()

        assertion = Assertion(self.driver)

        new_loan_fw.enter_loan_formwork(self.driver)
        # 借款单模板基本设置
        new_loan_fw.new_loan_formwork(self.driver, gv.loan_model_name1)
        # 设置审批流
        new_loan_fw.loan_flow(self.driver)
        # 设置其他项
        new_loan_fw.other(self.driver)
        # 保存
        new_loan_fw.save(self.driver)
        # 验证借款单模板是否已新建成功
        expense_name = get_form.get_formwork_name(self.driver, gv.loan_model_name1)
        assertion.except_equal(gv.loan_model_name1, expense_name, u'借款单模板未创建成功', u'新建借款单模板成功')
