# -*- coding:utf-8 -*-
import unittest
import common.login
import action.baidu_action as BD
import config.global_variable as GV
from time import sleep
class BaiDu(unittest.TestCase):

    def setUp(self):
        self.driver = common.login.get_url()

    def test_baidu_search1(self):
        driver = BD.NewBaiDu()
        driver.baidu_search1(self.driver)
        sleep(2)
        driver.baidu_search2(self.driver)
    # def test_baidu_search2(self):
    #     driver = BD.NewBaiDu()
    #     driver.baidu_search2(self.driver)
    # def test_baidu_search3(self):
    #     driver = BD.NewBaiDu()
    #     driver.baidu_search3(self.driver,GV.name1)




    def tearDown(self):
        self.driver.quit()
#
