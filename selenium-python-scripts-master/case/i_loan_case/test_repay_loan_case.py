# -*- coding: utf-8 -*-
import unittest
import common.login
import action.loan_action.repay_loan_action as rla
from time import sleep


class TestRepayLoanCase(unittest.TestCase):

    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)
        return

    def tearDown(self):
        self.driver.quit()

    def test_repay(self):
        repay_loan = rla.RepayLoanAction()
        refused_reason = u'填写不规范'
        # 发起还款
        loan_value = repay_loan.get_loan_list(self.driver)
        sleep(1)
        repay_loan.repay(self.driver, loan_value)
        repay_loan.cashier_reject(self.driver, refused_reason)
        # 再次发起还款
        loan_value = repay_loan.get_loan_list(self.driver)
        repay_loan.repay(self.driver, loan_value)
        repay_loan.cashier_agree(self.driver)


