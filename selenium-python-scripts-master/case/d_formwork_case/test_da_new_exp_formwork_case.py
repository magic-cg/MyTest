# -*- coding: utf-8 -*-
import unittest
import action.formwork_action.new_exp_formwork_action as nefa
from action.formwork_action.assert_formwork_action import GetFormwork
import config.global_variable as gv
import common.login
from time import sleep
from common.assertion import Assertion


class NewExpFormWorkCase(unittest.TestCase):

    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    # 新建报销单模板
    def test_new_exp_formwork(self):

        new_expense_fw = nefa.NewExpenseFormWorkAction()
        get_form = GetFormwork()
        assertion = Assertion(self.driver)
        new_expense_fw.enter_exp_formwork(self.driver)
        # 设置报销单的基本设置
        new_expense_fw.new_exp_formwork(self.driver, gv.exp_model_name1)
        # 设置审批流
        new_expense_fw.exp_flow(self.driver)
        # 添加其他项
        new_expense_fw.other(self.driver)
        # 添加自定义字段
        new_expense_fw.field_setting(self.driver)
        # 添加说明文本
        new_expense_fw.explanatory(self.driver)
        # 添加分割线
        new_expense_fw.divider(self.driver)
        # 保存
        new_expense_fw.save(self.driver)
        # 验证报销单模板是否已新建成功
        expense_name = get_form.get_formwork_name(self.driver, gv.exp_model_name1)
        assertion.except_equal(gv.exp_model_name1, expense_name, u'报销单模板未创建成功', u'新建报销单模板成功')
