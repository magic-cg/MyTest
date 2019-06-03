# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.loan_action.create_loan_action as cla
import action.expense_action.new_expense_action as nea
import action.requisition_action.new_requisition_action as nra
from action.receipt_flow_action.operations_action import OperationButAction
import config.global_variable as gv
from common.assertion import Assertion
from action.attachment_action import AttachmentFile
atta = AttachmentFile()


class TestNewRequisition(unittest.TestCase):
    def setUp(self):

        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_batch(self):
        new_requisition = nra.NewRequisitionPage()
        loan = cla.LoanAction()
        new_expense = nea.NewExpenseAction()

        operation = OperationButAction()
        assertion = Assertion(self.driver)

        collectnum = []

        # 提交报销单
        for i in range(0, 1):
            # 点击报销单按钮
            new_expense.new_expense_button(self.driver)
            # 报销单标题等
            new_expense.new_expense1(self.driver, gv.exp_title1)
            # 点击添加明细按钮
            new_expense.write_fee_type(self.driver)
            # 报销单普通的费用类型
            new_expense.simple_fee_type(self.driver, gv.expense_amount, gv.fee_type_name[0])
            # 保存
            new_expense.save(self.driver)
            # 项目
            new_expense.new_project_field(self.driver, gv.project_name[0])
            # 提交
            operation.submit(self.driver)
            # 有借款未核销，是否继续
            operation.loan_not_add(self.driver)
            # 选择加急和下一审批人
            operation.select_urgent_switch1(self.driver, gv.approver)
            # 费用超标
            operation.fee_more_except(self.driver)
            # 验证是否出现提交成功的吐丝
            message = operation.message_reminder(self.driver)
            assertion.except_equal(u'提交成功', message, u'提交失败，可能进入到了提交中状态', u'报销单提交成功')
            # 获取当前单号
            current_num = operation.get_num(self.driver)
            collectnum.append(current_num)
        # 提交借款单
        for i in range(0, 1):
            # 新建借款单
            loan.create_new_loan1(self.driver, gv.loan_title1, gv.loan_amount)
            # 上传附件
            atta.upload_attachment(self.driver)
            # 提交
            operation.submit(self.driver)
            # 选择第一个审批人
            operation.select_urgent_switch(self.driver, gv.approver)
            # 验证是否出现提交成功的吐丝
            message = operation.message_reminder(self.driver)
            assertion.except_equal(u'提交成功', message, u'提交失败，可能进入到了提交中状态', u'借款单提交成功')
            # 获取当前单号
            current_num = operation.get_num(self.driver)
            collectnum.append(current_num)
        # 提交申请单
        for i in range(0, 1):

            # 新建申请单
            new_requisition.new_requisition(self.driver)
            # 选择模板，填写申请单标题
            new_requisition.select_model(self.driver, gv.requisition_title, gv.requisition_model_name5)
            # 添加申请明细
            new_requisition.requisition_detail(self.driver, gv.fee_type_name[0], gv.requisition_amount)
            # 提交申请单
            operation.submit(self.driver)
            # 选择下一审批人
            operation.select_urgent_switch(self.driver, gv.approver)
            # 验证是否出现提交成功的吐丝
            message = operation.message_reminder(self.driver)
            assertion.except_equal(u'提交成功', message, u'提交失败，可能进入到了提交中状态', u'申请单提交成功')
            sleep(0.5)
            # 是否关注易快报企业微信号
            new_requisition.remind(self.driver)
            sleep(1)

            # 获取当前单号
            current_num = operation.get_num(self.driver)
            collectnum.append(current_num)

        # 进入待审批页面
        operation.pending(self.driver)
        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])


        # 审批人批量转交审批
        operation.batch_approve_transfer(self.driver)
        # 预算超标，是否继续
        operation.budget_excess(self.driver)
        # 审批人选择转交审批-转交
        operation.approve_transfer1(self.driver)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'操作成功!', message, u'审批失败', u'批量转交成功')
        # 刷新页面
        self.driver.refresh()
        sleep(1)

        # 进入待审批页面
        operation.pending(self.driver)
        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])
        # 审批人批量转交审批
        operation.batch_approve_transfer(self.driver)
        # 预算超标，是否继续
        operation.budget_excess(self.driver)
        # 审批人选择转交审批-前加签
        operation.approve_transfer2(self.driver)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'操作成功!', message, u'审批失败', u'批量前加签成功')
        # 刷新页面
        self.driver.refresh()
        sleep(1)

        # 进入待审批页面
        operation.pending(self.driver)
        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])
        # 审批人批量转交审批
        operation.batch_approve_transfer(self.driver)
        # 预算超标，是否继续
        operation.budget_excess(self.driver)
        # 审批人选择转交审批-后加签
        operation.approve_transfer3(self.driver)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'操作成功!', message, u'审批失败', u'批量后加签成功')
        # 刷新页面
        self.driver.refresh()
        sleep(1)

        # 进入待审批页面
        operation.pending(self.driver)

        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])
        # 第一个审批人批量同意
        operation.batch_agree(self.driver)
        # 预算超标，是否继续
        operation.budget_excess(self.driver)
        # 审批人填写批量同意原因
        operation.batch_agree_reason(self.driver)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'第一个审批人批量同意')
        # 刷新页面
        self.driver.refresh()
        sleep(1)

        # 进入待审批页面
        operation.pending(self.driver)
        for i in range(len(collectnum)):
            operation.batch_check(self.driver, collectnum[i])
        # 第二个审批人批量同意
        operation.batch_agree(self.driver)
        # 预算超标，是否继续
        operation.budget_excess(self.driver)
        # 审批人填写批量同意原因
        operation.batch_agree_reason(self.driver)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'第二个审批人批量同意')
        # 刷新页面
        self.driver.refresh()
        sleep(2)

        # 进入待支付页面
        operation.tobepaid(self.driver)
        for i in range(len(collectnum)-1):
            operation.batch_check(self.driver, collectnum[i])
        operation.batch_paid(self.driver)
        # 预算超标，是否继续
        operation.budget_excess(self.driver)
        # 选择线下支付方式
        operation.offline_payment(self.driver)
        # 验证是否出现确认成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'确认成功', message, u'支付失败或单据进入支付中状态', u'批量支付成功')
