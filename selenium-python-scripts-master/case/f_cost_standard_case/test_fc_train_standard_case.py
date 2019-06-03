# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.cost_standard_action.train_standard_action as tsa
import config.global_variable as gv
from action.cost_standard_action.assertion_standard_action import GetStandard
from common.assertion import Assertion


class TestNewTrainStandard(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_train_standard(self):
        new_train = tsa.NewTrainStandardAction()
        assertion = Assertion(self.driver)
        get_standard = GetStandard()
        # 新建火车标准
        new_train.new_train_standard(self.driver)
        # 火车标准基本设置
        new_train.basic_setting(self.driver, gv.train_sta_name, gv.fee_type_name3[2])
        # 火车标准设置
        new_train.standard_setting(self.driver)

        # 获取新建的费用标准的名字
        train_name = get_standard.get_standard_name(self.driver, gv.train_sta_name)
        # 验证费用标准是否创建成功
        assertion.except_equal(gv.train_sta_name, train_name, u'火车标准创建失败', u'火车标准创建成功')