# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
from action.collect_account_action.new_collect_account_action import NewCollectAccount
import config.global_variable as gv


class TestNewCollectAccount(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_collect_account(self):
        new_coll_account = NewCollectAccount()
        new_coll_account.collect_account(self.driver, gv.collect_name, gv.collect_no)

