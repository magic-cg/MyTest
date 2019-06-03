# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from page.flow_page.new_flow_page import NewFlowPage


class AssertFlow:

    # 创建审批流的名字
    def assert_flow_name(self, driver, flow_name):
        new_sample_flow = NewFlowPage(driver)
        # 搜索新建的审批流
        new_sample_flow.find_element(NewFlowPage.search).send_keys(flow_name)
        new_sample_flow.find_element(NewFlowPage.search).send_keys(Keys.ENTER)
        # 获取新建审批流的名字
        new_sample_flow.find_element(NewFlowPage.searchResult).click()
        flow_name_text1 = new_sample_flow.find_element(NewFlowPage.searchResult).text
        sleep(1)
        return flow_name_text1






