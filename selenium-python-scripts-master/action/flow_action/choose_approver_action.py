# -*- coding: utf-8 -*-
from time import sleep
from page.flow_page.new_flow_page import NewFlowPage
from action.select_components_action import Select
from selenium.webdriver.common.action_chains import ActionChains
import config.global_variable as gv

    # 选择审批人


class ChooseApprover:

    def approver_limit_range(self, driver):

        new_sample_flow = NewFlowPage(driver)
        select = Select()
        # 手动选择-由提交人指定
        new_sample_flow.find_element(NewFlowPage.limitRange).click()
        sleep(1)
        new_sample_flow.find_element(NewFlowPage.editLimitPerson).click()

        sleep(2)
        # 调用多选组件
        select.multiple_components(driver)

        sleep(2)

    def role_select(self, driver):
        new_sample_flow = NewFlowPage(driver)
        new_sample_flow.find_element(NewFlowPage.autoSelect).click()
        sleep(1)
        # 通过角色匹配人
        new_sample_flow.find_element(NewFlowPage.role).click()
        new_sample_flow.find_element(NewFlowPage.clickRoleText).click()
        sleep(2)
        # 获取所有的角色组
        select_role = driver.find_element_by_css_selector(".ant-cascader-menu")
        allOptions = select_role.find_elements_by_tag_name("li")
        for option in allOptions:
            # print option.text
            if gv.role_name1 in option.text:
                option.click()
                break
