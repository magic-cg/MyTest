# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.cost_standard_action.hotel_standard_action as hsa
import config.global_variable as gv
from action.cost_standard_action.assertion_standard_action import GetStandard
from common.assertion import Assertion


class TestNewHotelStandard(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_hotel_standard(self):
        new_hotel = hsa.NewHotelStandardAction()
        assertion = Assertion(self.driver)
        get_standard = GetStandard()
        # 新建酒店标准
        new_hotel.new_hotel_standard(self.driver)
        # 酒店标准的基本设置
        new_hotel.basic_setting(self.driver, gv.hotel_sta_name, gv.fee_type_name3[1])
        # 酒店标准设置
        new_hotel.standard_setting(self.driver, gv.hotel_money[0])

        # 获取新建的费用标准的名字
        hotel_name = get_standard.get_standard_name(self.driver, gv.hotel_sta_name)
        # 验证费用标准是否创建成功
        assertion.except_equal(gv.hotel_sta_name, hotel_name, u'酒店标准创建失败', u'酒店标准创建成功')