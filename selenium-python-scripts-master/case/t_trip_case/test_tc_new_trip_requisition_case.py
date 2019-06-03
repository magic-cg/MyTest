# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.requisition_action.new_trip_requisition_action as ntra
from action.requisition_action.new_requisition_action import NewRequisitionPage
from action.receipt_flow_action.operations_action import OperationButAction
import config.global_variable as gv
from common.assertion import Assertion


class TestNewRequisition(unittest.TestCase):
    def setUp(self):

        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_requisition(self):

        requisition = NewRequisitionPage()
        operation = OperationButAction()
        new_requisition = ntra.NewTripRequisitionAction()
        assertion = Assertion(self.driver)
        exp_describe = u'这是申请单描述'
        # 点击新建申请单
        requisition.new_requisition(self.driver)
        # 选择带有行程类型的模板
        requisition.select_model(self.driver, gv.requisition_title, gv.trip_requisition_model_name1)
        # 添加行程
        new_requisition.add_trip(self.driver)
        # 添加交通行程
        new_requisition.traffic_trip(self.driver, gv.requisition_tripFromCity, gv.requisition_tripToCity)
        # 再次添加住宿行程
        new_requisition.trip_again(self.driver)
        # 添加住宿类型
        new_requisition.accommodation_trip(self.driver, gv.requisition_tripToCity)
        # 保存
        new_requisition.save(self.driver)
        # 提交申请单
        operation.submit(self.driver)
        # 选择下一审批人
        operation.select_first_person(self.driver, gv.approver)
        # 验证是否出现提交成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'提交成功', message, u'提交失败，可能进入到了提交中状态', u'申请单提交成功')
        # 获取当前单号
        current_num = operation.get_num(self.driver)
        # 是否关注易快报企业微信号
        new_requisition.remind(self.driver)
        sleep(1)
        # 审批人同意（此申请单关联的模板的审批流只有一个审批节点）
        operation.requi_last_agree(self.driver, current_num, u"申请单最后一个节点审批同意")
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'申请单最后一个审批人同意')
