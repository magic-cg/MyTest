# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.requisition_action.new_requisition_action as nra
from action.receipt_flow_action.operations_action import OperationButAction
import config.global_variable as gv
from common.assertion import Assertion


class TestNewRequisition(unittest.TestCase):
    def setUp(self):

        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_agree_requisition(self):
        new_requisition = nra.NewRequisitionPage()
        operation = OperationButAction()
        assertion = Assertion(self.driver)

        exp_describe = u'这是申请单描述'
        # 新建申请单
        new_requisition.new_requisition(self.driver)
        # 选择模板，填写申请单标题
        new_requisition.select_model(self.driver, gv.requisition_title, gv.requisition_model_name1)
        # 添加申请明细
        new_requisition.requisition_detail(self.driver, gv.fee_type_name[0], gv.requisition_amount)
        # 提交申请单
        operation.submit(self.driver)
        # 选择下一审批人
        operation.select_first_person(self.driver, gv.approver)
        # 验证是否出现提交成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'提交成功', message, u'提交失败，可能进入到了提交中状态', u'申请单提交成功')
        # 是否关注易快报企业微信号
        new_requisition.remind(self.driver)
        sleep(1)

        # 获取当前单号
        current_num = operation.get_num(self.driver)
        # 第一个审批人同意
        operation.agree(self.driver, current_num)
        # 选择下一个审批人
        operation.select_next_person(self.driver, gv.approver, gv.approve_remark)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'申请单第一个审批人同意')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 第二个审批人同意
        operation.requi_last_agree(self.driver, current_num, u"申请单最后一个节点审批同意")
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'申请单最后一个审批人同意')