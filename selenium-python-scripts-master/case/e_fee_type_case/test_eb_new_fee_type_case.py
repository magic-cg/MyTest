# -*- coding: utf-8 -*-
import unittest
import common.login
from time import sleep
import action.fee_type_action.new_simple_fee_type_action as nsfta
import config.global_variable as gv


class TestNewFee(unittest.TestCase):

    def setUp(self):

        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_fee(self):
        new_fee_type_simple = nsfta.NewFeeTypeSimpleAction()

        # 创建普通的费用类型
        new_fee_type_simple.new_basic_fee(self.driver, gv.fee_type_name)




