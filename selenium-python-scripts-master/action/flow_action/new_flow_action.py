# -*- coding: utf-8 -*-
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from page.flow_page.new_flow_page import NewFlowPage
from common.common_menu_page import CommonMenus
from action.select_components_action import Select


class NewFlowAction:

    # 创建审批流的名字
    def new_simple_flow_name(self, driver, flow_name):
        new_sample_flow = NewFlowPage(driver)
        common_menu = CommonMenus(driver)
        # 进入到审批流页面下
        ActionChains(driver).move_to_element(common_menu.find_element(CommonMenus.enterpriseManagement)).perform()
        common_menu.find_element(CommonMenus.flow).click()
        # 新建新的审批流
        new_sample_flow.find_element(NewFlowPage.addFlow).click()
        # sleep(1)
        new_sample_flow.find_element(NewFlowPage.addName).send_keys(flow_name)
        sleep(1)

        new_sample_flow.find_element(NewFlowPage.ensureBut).click()
        # 创建第一个节点,生效节点：无条件，限制可选范围
        sleep(2)

    def new_satrt_node(self, driver, reason):
        new_sample_flow = NewFlowPage(driver)
        select = Select()
        new_sample_flow.find_element(NewFlowPage.startNode).click()
        sleep(1)
        new_sample_flow.find_element(NewFlowPage.selectUrgent).click()
        sleep(2)
        new_sample_flow.find_element(NewFlowPage.selectUrgentRole).click()
        sleep(1)
        new_sample_flow.find_element(NewFlowPage.urgentRole).click()

        # 手动选择-由提交人指定
        # new_sample_flow.find_element(NewFlowPage.limitRange).click()
        # sleep(1)
        #  new_sample_flow.find_element(NewFlowPage.editLimitPerson).click()

        sleep(2)
        # 调用多选组件
        select.multiple_components(driver)
        new_sample_flow.find_element(NewFlowPage.addReason).click()
        sleep(1)
        new_sample_flow.find_element(NewFlowPage.reason).send_keys(reason)
        sleep(1)