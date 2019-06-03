# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.cost_standard_action.ship_standard_action as ssa
import config.global_variable as gv
from action.cost_standard_action.assertion_standard_action import GetStandard
from common.assertion import Assertion


class TestNewShipStandard(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_ship_standard(self):
        new_ship = ssa.NewShipStandardAction()
        assertion = Assertion(self.driver)
        get_standard = GetStandard()
        # 新建轮船标准
        new_ship.new_ship_standard(self.driver)
        # 轮船基本设置
        new_ship.basic_setting(self.driver, gv.ship_sta_name, gv.fee_type_name3[3])
        # 轮船标准设置
        new_ship.standard_setting(self.driver)

        # 获取新建的费用标准的名字
        ship_name = get_standard.get_standard_name(self.driver, gv.ship_sta_name)
        # 验证费用标准是否创建成功
        assertion.except_equal(gv.ship_sta_name, ship_name, u'轮船标准创建失败', u'轮船标准创建成功')