# -*- coding: utf-8 -*-
import unittest
import common.login
from common.assertion import Assertion
import action.trip_type_action.new_trip_type_action as ntta
from action.trip_type_action.assert_trip_type_action import GetTripType
import config.global_variable as gv
from time import sleep


class TestNewTrip(unittest.TestCase):

    def setUp(self):

        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_trip(self):
        new_trip = ntta.NewTripTypeAction()
        get_trip_type = GetTripType()
        assertion = Assertion(self.driver)
        # 创建行程类型
        new_trip.new_trip(self.driver, gv.trip_type_name[0], gv.trip_type_name[1], gv.trip_type_name[2])

        # 验证交通行程类型是否已新建成功
        expense_name = get_trip_type.get_trip_type_name(self.driver, gv.trip_type_name[0])
        assertion.except_equal(gv.trip_type_name[0], expense_name, u'交通行程类型未创建成功', u'新建交通行程类型成功')
        # 验证住宿行程类型是否已新建成功
        expense_name = get_trip_type.get_trip_type_name(self.driver, gv.trip_type_name[2])
        assertion.except_equal(gv.trip_type_name[2], expense_name, u'住宿行程类型未创建成功', u'新建住宿行程类型成功')