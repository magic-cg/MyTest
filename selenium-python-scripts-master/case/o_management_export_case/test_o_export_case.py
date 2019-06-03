# -*- coding: utf-8 -*-
import unittest
from time import sleep

from action.attachment_action import AttachmentFile
from action.management_export_action.export_action import Export
import common.login


class TestExport(unittest.TestCase):

    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_export(self):
        export = Export()
        atta = AttachmentFile()
        # 报销单管理导出全部
        export.expense_export(self.driver)
        # atta.downlaod_all_one(self.driver, '报销单管理下没有单据')
        # 报销单管理导出选中
        atta.download_part(self.driver, '报销单管理下没有单据')
        # 刷新页面
        self.driver.refresh()
        sleep(2)

        # 借款管理-申请中-导出选中
        export.loan_doing_export(self.driver)
        sleep(0.5)
        atta.download_part(self.driver, '借款管理-申请中下没有单据')
        # 借款管理-申请中-导出全部
        atta.downlaod_all_one(self.driver, '借款管理-申请中下没有单据')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 借款管理-待还款-导出全部
        export.loan_wait_export(self.driver)
        sleep(0.5)
        atta.downlaod_all_two(self.driver, '借款管理-待还款下没有单据')
        # 借款管理-待还款-导出选中
        atta.download_part_two(self.driver, '借款管理-待还款下没有单据')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 借款管理-已完成-导出全部
        export.loan_done_export(self.driver)
        sleep(0.5)
        atta.downlaod_all_three(self.driver, '借款管理-已完成下没有单据')
        # 借款管理-已完成-导出选中
        atta.download_part_three(self.driver, '借款管理-已完成下没有单据')
        # 刷新页面
        self.driver.refresh()
        sleep(2)

        # 申请管理-申请中-导出全部
        export.requisition_doing_export(self.driver)
        sleep(0.5)
        atta.downlaod_all_one(self.driver, '申请管理-申请中下没有单据')
        # 申请管理-申请中-导出选中
        atta.download_part(self.driver, '申请管理-申请中下没有单据')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 申请管理-进行中-导出全部
        export.requisition_wait_export(self.driver)
        sleep(0.5)
        atta.downlaod_all_two(self.driver, '申请管理-进行中下没有单据')
        # 申请管理-进行中-导出选中
        atta.download_part_two(self.driver, '申请管理-进行中下没有单据')
        # 刷新页面
        self.driver.refresh()
        sleep(2)
        # 申请管理-已完成-导出全部
        export.requisition_done_export(self.driver)
        sleep(0.5)
        atta.downlaod_all_three(self.driver, '申请管理-已关闭下没有单据')
        # 申请管理-已完成-导出选中
        atta.download_part_three(self.driver, '申请管理-已关闭下没有单据')












