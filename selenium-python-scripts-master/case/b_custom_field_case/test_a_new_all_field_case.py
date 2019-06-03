# -*- coding: utf-8 -*-
import unittest
import common.login
from time import sleep
import config.global_variable as gv
import action.custom_field_action.new_all_field_action as nafa


class TestNewFee(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_field(self):
        new_all_field = nafa.NewAllFieldAction()
        new_all_field.entry_fee_type(self.driver, gv.fee_type_name4)
        new_all_field.entry_field(self.driver)
        # 新建各种类型的字段
        new_all_field.new_field(self.driver)
        # 新建枚举字段
        new_all_field.enumeration_field(self.driver)
        # 新建档案字段
        new_all_field.archives_field(self.driver)

