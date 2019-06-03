# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.permissions_action.permissions_setting_action as psa
import config.global_variable as gv


class TestPermission(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_permissions(self):
        permiss = psa.Permission()
        # 报销单管理权限
        permiss.perssion_expense(self.driver)
        # 借款管理权限
        permiss.perssion_loan(self.driver)
        # 申请单管理权限
        permiss.perssion_requisition(self.driver)
        # 预算管理权限
        # permiss.perssion_budget(self.driver)

