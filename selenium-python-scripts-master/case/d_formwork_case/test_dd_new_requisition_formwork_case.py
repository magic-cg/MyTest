# -*- coding: utf-8 -*-
import unittest
import action.formwork_action.new_requisition_formwork_action as nrfa
import config.global_variable as gv
import common.login
from time import sleep
from action.formwork_action.assert_formwork_action import GetFormwork
from common.assertion import Assertion


class NewRequisitionFormWorkCase(unittest.TestCase):

    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    # 新建直接填写申请金额的申请单模板
    def test_new_requisition_formwork(self):
        new_requisition_fw = nrfa.NewRequisitionFormWorkAction()
        get_form = GetFormwork()
        assertion = Assertion(self.driver)
        # 进入模板模块
        new_requisition_fw.enter_requisition_formwork(self.driver)
        # 新建申请单模板
        new_requisition_fw.new_requisition_formwork(self.driver, gv.requisition_model_name2)
        # 设置申请单的审批流
        new_requisition_fw.requisition_flow(self.driver)
        # 设置申请单打印模板
        new_requisition_fw.print_model(self.driver)
        # 设置申请单为直接填写金额
        new_requisition_fw.write_money_direct(self.driver)
        # 保存
        new_requisition_fw.save(self.driver)
        # 验证申请单模板是否已新建成功
        expense_name = get_form.get_formwork_name(self.driver, gv.requisition_model_name2)
        assertion.except_equal(gv.requisition_model_name2, expense_name, u'申请单模板未创建成功', u'新建申请单模板成功')