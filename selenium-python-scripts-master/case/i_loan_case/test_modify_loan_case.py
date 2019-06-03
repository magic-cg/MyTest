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

    def test_modify_loan(self):

        """审批流程均为三级审批，第三个节点为出纳。第一个节点可修改，第二个节点可撤回单据"""

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
        # 搜索刚提交的单据
        operation.search(self.driver, current_num)
        # 提交人评论
        operation.comment(self.driver)
        # 验证是否出现单据评论成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'单据评论成功', message, u'单据评论失败', u'借款单提交人添加评论成功')
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
        # 第二个审批人查看单据详情
        operation.look_over_details(self.driver, current_num)
        # 第二个审批人修改单据
        operation.modify(self.driver)
        operation.modify_loan(self.driver)
        # 确认修改，填写原因
        operation.modify_save(self.driver, u'修改借款单金额、标题等')
        # 验证是否出现修改保存成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'保存成功', message, u'修改单据失败', u'借款单第二个审批人修改单据成功')
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







