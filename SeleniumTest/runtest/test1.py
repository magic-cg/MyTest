# -*- coding:utf-8 -*-
# 这是将page、case、action写在同一个页面下的，不可发邮件 2019/06/27

from HTMLTestRunner import HTMLTestRunner
import unittest
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BaiDu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("ceshi 1")
        driver.find_element_by_id("su").click()




    def tearDown(self):
        self.driver.quit()

# if  __name__ == "__main__":
#     testunit = unittest.TestSuite()
#     testunit.addTest(BaiDu("test_baidu_search"))
#
#     fp = open('./result.html', 'wb')
#
#     runner = HTMLTestRunner(stream=fp,
#                             title="测试报告",
#                             description='用例执行情况')
#
#     runner.run(testunit)
#     fp.close()

