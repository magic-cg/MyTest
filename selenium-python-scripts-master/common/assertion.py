# -*- coding: utf-8 -*-
import unittest
import time


class Assertion(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver
        self._type_equality_funcs = {}

        # self.exception = exception
        # self.actual = actual

    def except_equal(self, exception, actual, message, successful_text):
        try:
            self.assertEqual(exception, actual, message)
            print successful_text
        except BaseException, msg:
            print(u"此用例运行失败，异常原因:%s" % msg)
            # 图片名称可以加个时间戳
            nowTime = time.strftime("%Y-%m-%d %H-%M-%S")
            self.driver.get_screenshot_as_file('/Users/wei/Downloads/screenshot%s.png' % nowTime)

