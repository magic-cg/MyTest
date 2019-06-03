# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
from action.pay_account_action.new_pay_account_action import NewPayAccount
import config.global_variable as gv


class TestNewPayAccount(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_pay_account(self):
        new_pay_account = NewPayAccount()

        new_pay_account.offline_account(self.driver, gv.pay_code[0], gv.pay_name[0])
        new_pay_account.online_account(self.driver, gv.pay_code[1], gv.pay_name[1], gv.account_name[0], gv.bank_card_no[0])
        new_pay_account.ERP_account(self.driver, gv.pay_code[2], gv.pay_name[2], gv.account_name[1], gv.bank_card_no[1])
        # new_pay_account.edit_account(self.driver)
        # new_pay_account.disable_account(self.driver)