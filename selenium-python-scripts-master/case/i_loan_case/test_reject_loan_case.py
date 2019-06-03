# -*- coding: utf-8 -*-
import unittest
from time import sleep

import action.loan_action.create_loan_action as cla
from action.attachment_action import AttachmentFile
import action.receipt_flow_action.operations_action as oa
from common.assertion import Assertion
import config.global_variable as gv
import common.login


class TestCreateLoan(unittest.TestCase):

    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()
    # 新建借款单

    def test_reject_loan(self):

        """审批流程均为三级审批，第三个节点为出纳"""

        loan = cla.LoanAction()
        operation = oa.OperationButAction()
        assertion = Assertion(self.driver)
        atta = AttachmentFile()
        # 新建借款单
        loan.create_new_loan(self.driver, gv.loan_title, gv.loan_amount)
        # 上传附件
        atta.upload_attachment(self.driver)
        # 提交
        operation.submit(self.driver)
        # 选择第一个审批人
        operation.select_first_person(self.driver, gv.approver)
        # 获取当前单号
        current_num = operation.get_num(self.driver)
        # 验证是否出现提交成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'提交成功', message, u'提交失败，可能进入到了提交中状态', u'借款单提交成功')

        # 第一个审批人同意
        operation.agree(self.driver, current_num)
        # 选择下一个审批人
        operation.select_next_person(self.driver, gv.approver, gv.approve_remark)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'借款单第一个审批人同意')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 第二个审批人驳回
        operation.reject(self.driver, current_num)
        # 验证是否出现驳回成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'驳回成功', message, u'审批失败', u'借款单第二个审批人驳回单据')
        # 搜索被驳回的单据
        operation.search(self.driver, current_num)
        # 再次提交借款单
        operation.submit(self.driver)

        # 选择第一个审批人
        operation.select_first_person(self.driver, gv.approver)
        self.driver.refresh()
        sleep(1)
        # 第一个审批人同意
        operation.agree(self.driver, current_num)
        # 选择下一个审批人
        operation.select_next_person(self.driver, gv.approver, gv.approve_remark)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'借款单驳回后再提交，审批人同意')
        # 刷新页面
        self.driver.refresh()
        sleep(2)

        # 第二个审批人同意
        operation.agree(self.driver, current_num)
        # 选择出纳
        operation.select_next_person(self.driver, gv.approver, gv.approve_remark)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'借款单第二个审批人同意')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 出纳支付
        operation.paid(self.driver, current_num)
        # 选择线下支付方式
        operation.offline_payment(self.driver)
        # 验证是否出现确认成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'确认成功', message, u'支付失败或单据进入支付中状态', u'借款单支付成功')







