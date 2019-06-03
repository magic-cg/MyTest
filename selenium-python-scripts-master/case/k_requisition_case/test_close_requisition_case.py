# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.requisition_action.close_requisition_action as cra


class TestCloseRequisition(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_close_requisition(self):
        close_requisition = cra.CloseRequisitionAction()
        # 关闭申请单
        close_requisition.close_requisition(self.driver)
