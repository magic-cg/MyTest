# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.cost_standard_action.subsidy_standard_action as ssa
import config.global_variable as gv
from action.cost_standard_action.assertion_standard_action import GetStandard
from common.assertion import Assertion


class TestNewSubSIDYStandard(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_subsidy_standard(self):
        new_subsidy = ssa.NewSubsidyStandardAction()
        assertion = Assertion(self.driver)
        get_standard = GetStandard()
        # 新建补助标准
        new_subsidy.new_subsidy_standard(self.driver)
        # 补助基本设置
        new_subsidy.basic_setting(self.driver, gv.subsidy_sta_name, gv.fee_type_name3[4])
        # 补助标准设置
        new_subsidy.standard_setting(self.driver, gv.subsidy_money[0])

        # 获取新建的费用标准的名字
        subsidy_name = get_standard.get_standard_name(self.driver, gv.subsidy_sta_name)
        # 验证费用标准是否创建成功
        assertion.except_equal(gv.subsidy_sta_name, subsidy_name, u'补助标准创建失败', u'补助标准创建成功')