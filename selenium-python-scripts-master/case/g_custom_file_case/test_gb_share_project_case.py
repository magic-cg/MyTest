# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
import action.custom_file_action.new_project_action as npa
import config.global_variable as gv


class TestNewFlow(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    # 创建费用分摊里用的项目
    def test_share_project(self):
        new_project = npa.NewProjectAction()
        # 进入到项目页面
        new_project.new_project(self.driver)
        # 新建父级项目
        new_project.father_project(self.driver, gv.project)

