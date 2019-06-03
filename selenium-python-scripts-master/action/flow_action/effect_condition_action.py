# -*- coding: utf-8 -*-

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from page.flow_page.new_flow_page import NewFlowPage
from common.common_menu_page import CommonMenus
from action.select_components_action import Select
import config.global_variable as gv


class EffcetCondition:
    # 生效条件：报销/借款/申请金额大于设定值
    _result = None

    def money_than(self, driver):
        if self._result is None:
            new_sample_flow = NewFlowPage(driver)
            new_sample_flow.find_element(NewFlowPage.greaterThanSetValue).click()
            new_sample_flow.find_element(NewFlowPage.settingValue).click()
            new_sample_flow.find_element(NewFlowPage.settingValue).send_keys('10')
            self._result = new_sample_flow.find_element(NewFlowPage.greaterThanSetValue).is_selected()
        # return self._result
