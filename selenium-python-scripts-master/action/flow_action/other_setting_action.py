# -*- coding: utf-8 -*-
from page.flow_page.new_flow_page import NewFlowPage


# 其他设置
class Setting:
    # 审批人与提交人重复时
    def repeat_one(self, driver):
        new_sample_flow = NewFlowPage(driver)
        new_sample_flow.find_element(NewFlowPage.automaticAgreeOne).click()

    # 审批人与前面审批人重复时
    def repeat_two(self, driver):
        new_sample_flow = NewFlowPage(driver)
        new_sample_flow.find_element(NewFlowPage.automaticAgreeTwo).click()

    # 允许提交人撤回单据
    def allow_revote(self, driver):
        new_sample_flow = NewFlowPage(driver)
        new_sample_flow.find_element(NewFlowPage.revoke).click()

    # 允许审批人修改单据
    def allow_modify(self, driver):
        new_sample_flow = NewFlowPage(driver)
        new_sample_flow.find_element(NewFlowPage.modify).click()




