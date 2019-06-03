# -*- coding: utf-8 -*-
import unittest
import common.login
from time import sleep
import action.fee_type_action.new_auto_fee_type_action as nfta
import action.fee_type_action.new_simple_fee_type_action as nsfta

import config.global_variable as gv


class TestNewFee(unittest.TestCase):

    def setUp(self):

        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_fee(self):
        new_fee_aut_fee = nfta.NewFeeTypeWithAuoAction()
        # 创建自动计算的费用类型
        new_fee_aut_fee.new_basic_fee(self.driver, gv.fee_type_name1)
        # 报销字段
        new_fee_aut_fee.new_expense_fee(self.driver)
        new_fee_aut_fee.serch_fee_type(self.driver, gv.fee_type_name1)

        # 申请字段
        new_fee_aut_fee.new_requisition_fee(self.driver)




