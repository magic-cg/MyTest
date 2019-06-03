# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.cost_standard_action.ticket_standard_action as tsa
import config.global_variable as gv
from action.cost_standard_action.assertion_standard_action import GetStandard
from common.assertion import Assertion


class TestNewTicketStandard(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_ticket_standard(self):
        new_ticket = tsa.NewTicketStandardAction()
        assertion = Assertion(self.driver)
        get_standard = GetStandard()
        # 新建机票标准
        new_ticket.new_ticket_standard(self.driver)
        # 机票标准基本设置
        new_ticket.basic_setting(self.driver, gv.ticket_sta_name, gv.fee_type_name3[0])
        # 机票标准设置
        new_ticket.standard_setting(self.driver)

        # 获取新建的费用标准的名字
        ticket_name = get_standard.get_standard_name(self.driver, gv.ticket_sta_name)
        # 验证费用标准是否创建成功
        assertion.except_equal(gv.ticket_sta_name, ticket_name, u'机票标准创建失败', u'机票标准创建成果')