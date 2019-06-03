# -*- coding: utf-8 -*-
import unittest
import common.login
from time import sleep
import action.fee_type_action.new_standard_fee_type_action as nsfta
import action.fee_type_action.new_simple_fee_type_action as nsft
import config.global_variable as gv


class TestNewStandardFee(unittest.TestCase):

    def setUp(self):

        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_fee(self):
        new_standard_fee_type = nsfta.NewStandardFeeTypeAction()
        new_fee_type_simple = nsft.NewFeeTypeSimpleAction()

        # 创建费用标准的费用类型
        new_fee_type_simple.new_basic_fee(self.driver, gv.fee_type_name3)
        # 给这些费用标准加上不同的字段
        new_standard_fee_type.new_flight_fee(self.driver)






