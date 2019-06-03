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

    def test_batch_loan(self):

        """审批流程均为三级审批，第三个节点为出纳"""

        loan = cla.LoanAction()
        operation = oa.OperationButAction()
        assertion = Assertion(self.driver)
        atta = AttachmentFile()
        collectnum = []
        # 借款单提交循环2次
        for i in range(0, 2):

            # 新建借款单
            loan.create_new_loan(self.driver, gv.loan_title, gv.loan_amount)
            # 上传附件
            atta.upload_attachment(self.driver)
            # 提交
            operation.submit(self.driver)
            # 选择第一个审批人
            operation.select_first_person(self.driver, gv.approver)
            # 验证是否出现提交成功的吐丝
            message = operation.message_reminder(self.driver)
            assertion.except_equal(u'提交成功', message, u'提交失败，可能进入到了提交中状态', u'借款单提交成功')
            # 获取当前单号
            current_num = operation.get_num(self.driver)
            collectnum.append(current_num)

        for i in range(len(collectnum)):

            # 第一个审批人修改第二个审批人
            operation.look_over_details(self.driver, collectnum[i])
            sleep(2)
            operation.look_over_process(self.driver)
            sleep(2)
            operation.modify_approver_two(self.driver)
            # 刷新页面
            self.driver.refresh()
            sleep(2)
        # 进入待审批页面
        operation.pending(self.driver)
        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])
        # 第一个审批人批量审批同意
        operation.batch_agree(self.driver)
        operation.batch_agree_reason(self.driver)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'借款单第一个审批人批量同意')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 进入待审批页面
        operation.pending(self.driver)
        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])
        # 第二个审批人批量驳回
        operation.batch_reject(self.driver)
        # 验证是否出现驳回成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'驳回成功', message, u'驳回失败', u'借款单第二个审批人批量驳回')
        # 重新将这两个借款单提交
        for i in range(len(collectnum)):

            # 搜索被驳回的单据
            operation.search(self.driver, collectnum[i])
            # 再次提交借款单
            operation.submit(self.driver)
            # 选择第一个审批人
            operation.select_first_person(self.driver, gv.approver)
            # 刷新页面
            self.driver.refresh()
            sleep(2)

        # 进入待审批页面
        operation.pending(self.driver)
        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])
        # 第一个审批人批量审批同意
        operation.batch_agree(self.driver)
        operation.batch_agree_reason(self.driver)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'借款单第一个审批人同意')
        # 刷新页面
        self.driver.refresh()
        sleep(2)

        for i in range(len(collectnum)):
            # 第二个审批人修改出纳
            operation.look_over_details(self.driver, collectnum[i])
            sleep(2)
            operation.look_over_process(self.driver)
            sleep(2)
            operation.modify_approver_three(self.driver)
            # 刷新页面
            self.driver.refresh()
            sleep(2)
        sleep(1)
        # 进入待审批页面
        operation.pending(self.driver)
        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])
        # 第二个审批人批量同意
        operation.batch_agree(self.driver)
        operation.batch_agree_reason(self.driver)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'借款单第二个审批人同意')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 进入待支付页面
        operation.tobepaid(self.driver)
        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])
        # 出纳支付
        operation.batch_paid(self.driver)

        # 选择线下支付方式
        operation.offline_payment(self.driver)
        # 验证是否出现确认成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'确认成功', message, u'支付失败或单据进入支付中状态', u'借款单批量支付成功')







