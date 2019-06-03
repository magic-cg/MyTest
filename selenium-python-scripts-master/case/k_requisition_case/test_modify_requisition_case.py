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

    def test_modify_requisition(self):
        new_requisition = nra.NewRequisitionPage()
        operation = OperationButAction()
        assertion = Assertion(self.driver)

        # 新建申请单
        new_requisition.new_requisition(self.driver)
        new_requisition.select_model(self.driver, gv.requisition_title, gv.requisition_model_name1)

        # 添加申请明细
        new_requisition.requisition_detail(self.driver, gv.fee_type_name[1], gv.requisition_amount)
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
        # 搜索刚提交的单据
        operation.search(self.driver, current_num)
        # 提交人撤回申请单
        operation.revoke(self.driver)
        # 验证是否出现单据撤回成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'单据撤回成功', message, u'撤回失败，可能此单据不允许提交人撤回', u'借款单撤回成功')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 搜索撤回的单据
        operation.search(self.driver, current_num)
        # 再次提交申请单
        operation.submit(self.driver)
        # 选择下一审批人
        operation.select_first_person(self.driver, gv.approver)
        # 是否关注易快报企业微信号
        new_requisition.remind(self.driver)
        sleep(1)
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
        # 第二个审批人查看单据详情
        operation.look_over_details(self.driver, current_num)
        # 第二个审批人修改申请单
        operation.modify(self.driver)
        new_requisition.requisition_detail(self.driver, gv.fee_type_name[2], gv.requisition_amount)
        # 确认修改，填写原因
        operation.modify_save(self.driver, u'修改借款单金额、标题等')
        # 验证是否出现修改保存成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'保存成功', message, u'修改单据失败', u'借款单第二个审批人修改单据成功')
        # 刷新页面
        self.driver.refresh()
        sleep(1)
        # 第二个审批人添加评论
        operation.look_over_details(self.driver, current_num)
        # 第二个审批人增加评论
        operation.comment1(self.driver)
        # 验证是否出现单据评论成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'单据评论成功', message, u'单据评论失败', u'借款单审批人添加评论成功')
        # 刷新页面
        self.driver.refresh()
        sleep(1)
        # 第二个审批人同意
        operation.requi_last_agree(self.driver, current_num, u"申请单最后一个节点审批同意")
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'申请单第二个审批人同意')
