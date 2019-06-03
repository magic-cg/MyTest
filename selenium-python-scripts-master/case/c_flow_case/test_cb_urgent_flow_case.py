# -*- coding: utf-8 -*-
import unittest
from time import sleep
import common.login
from action.flow_action.new_flow_action import NewFlowAction
from action.flow_action.choose_approver_action import ChooseApprover
from action.flow_action.effect_condition_action import EffcetCondition
from action.flow_action.flow_buttons_action import Buttons
import config.global_variable as gv
from common.assertion import Assertion
from action.flow_action.assert_flow_action import AssertFlow
from action.flow_action.other_setting_action import Setting


class TestNewFlow(unittest.TestCase):
    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_flow(self):
        new_flow_sample = NewFlowAction()
        choose_app = ChooseApprover()
        effect_con = EffcetCondition()
        button = Buttons()
        assertion = Assertion(self.driver)
        assert_flow = AssertFlow()
        setting = Setting()

        new_flow_sample.new_simple_flow_name(self.driver, gv.flow_name2)

        # 节点一命名
        button.node_name(self.driver, gv.nodename[0])
        # 节点一生效条件为：无条件
        # 节点一选择审批人方式：由提交人/审批人选择
        choose_app.approver_limit_range(self.driver)
        # 提交人可撤回单据
        setting.allow_revote(self.driver)
        # 点击右下角创建按钮
        button.create(self.driver)

        # 开始节点选择加急审批配置
        new_flow_sample.new_satrt_node(self.driver, gv.reason)
        # 保存
        button.save(self.driver)

        # 验证此流程名称是否正确
        actual_name = assert_flow.assert_flow_name(self.driver, gv.flow_name2)
        assertion.except_equal(gv.flow_name2, actual_name, u'审批流名称不正确', u'新建加急审批流成功')


