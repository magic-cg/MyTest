# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.expense_action.new_expense_action as nea
from action.receipt_flow_action.operations_action import OperationButAction
from common.assertion import Assertion
import config.global_variable as gv


class TestNewExpense(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_comment_expense(self):
        new_expense = nea.NewExpenseAction()
        assertion = Assertion(self.driver)
        operation = OperationButAction()
        exp_describe = u'这是报销单描述'
        # 点击报销单按钮
        new_expense.new_expense_button(self.driver)
        # 报销单标题等
        new_expense.new_expense1(self.driver, gv.exp_title)
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
        # 选择下一审批人
        operation.select_urgent_switch(self.driver, gv.approver)
        # 费用超标
        operation.fee_more_except(self.driver)
        # 验证是否出现提交成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'提交成功', message, u'提交失败，可能进入到了提交中状态', u'报销单提交成功')
        # 获取当前单号
        current_num = operation.get_num(self.driver)

        # 第一个审批人查看单据详情
        operation.look_over_details(self.driver, current_num)
        # 第一个审批人转交审批
        operation.approve_transfer(self.driver)
        # 预算超标，是否继续
        operation.budget_excess(self.driver)
        # 第一个审批人选择转交审批理由
        operation.approve_transfer3(self.driver)
        # 验证是否出现单据评论成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'操作成功!', message, u'单据评论失败', u'报销单转交审批成功')
        sleep(1)
        # 选择下一个审批人
        # operation.select_next_person(self.driver, gv.approver, gv.approve_remark)
        # 刷新页面
        self.driver.refresh()
        # 第一个审批人同意
        operation.agree(self.driver, current_num)
        # 预算超标，是否继续
        operation.budget_excess(self.driver)
        # 选择出纳
        operation.select_next_person(self.driver, gv.approver, gv.approve_remark)
        # 验证是否出现审批成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'审批成功', message, u'审批失败', u'报销单第二个审批人同意')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 出纳支付
        operation.paid(self.driver, current_num)
        # 预算超标，是否继续
        operation.budget_excess(self.driver)
        # 选择线下支付方式
        operation.offline_payment(self.driver)
        # 验证是否出现确认成功的吐丝
        message = operation.message_reminder(self.driver)
        assertion.except_equal(u'确认成功', message, u'支付失败或单据进入支付中状态', u'报销单支付成功')



