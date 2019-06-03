# -*- coding: utf-8 -*-
from time import sleep
from page.flow_page.new_flow_page import NewFlowPage

# 定义审批流中创建、保存、+号等按钮


class Buttons:
    # 创建
    def create(self, driver):
        new_sample_flow = NewFlowPage(driver)

        # 创建
        new_sample_flow.find_element(NewFlowPage.create).click()
        sleep(1)

    # 保存
    def save(self, driver):
        new_sample_flow = NewFlowPage(driver)
        # 保存
        new_sample_flow.find_element(NewFlowPage.save).click()
        sleep(1)

    # "+"按钮
    def add(self, driver):
        new_sample_flow = NewFlowPage(driver)
        new_sample_flow.find_element(NewFlowPage.addNewNodeOne).click()


    #节点名字
    def node_name(self, driver, node_name):
        new_sample_flow = NewFlowPage(driver)

        new_sample_flow.find_element(NewFlowPage.firstNode).click()
        sleep(1)
        new_sample_flow.find_element(NewFlowPage.firstNodeName).send_keys(node_name)

    # 开始节点
    def start(self, driver):
        new_sample_flow = NewFlowPage(driver)

        # 创建
        new_sample_flow.find_element(NewFlowPage.create).click()
        sleep(1)