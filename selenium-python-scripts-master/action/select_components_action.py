# -*- coding: utf-8 -*-
from common.common_flow_page import FlowPage
from time import sleep
import config.global_variable as gv


class Select:

    def multiple_components(self, driver):

        flow = FlowPage(driver)

        # for循环
        for i in range(len(gv.list_name)):
            flow.find_element(FlowPage.searchPerson).send_keys(gv.list_name[i])
            flow.find_element(FlowPage.multipleChoice).click()
            flow.find_element(FlowPage.searchPerson).clear()
            sleep(1)
        flow.find_element(FlowPage.ensureSelectPerson).click()

    # def single_components(self, driver):

    def permission_components(self, driver):

        flow = FlowPage(driver)

        for i in range(len(gv.list_person)):
            flow.find_element(FlowPage.searchPerson).send_keys(gv.list_person[i])
            sleep(2)
            select_state = flow.find_element(FlowPage.multipleChoice).is_selected()
            if select_state:
                # 关闭选人组件页面
                flow.find_element(FlowPage.searchPerson).clear()

            else:
                flow.find_element(FlowPage.multipleChoice).click()
                flow.find_element(FlowPage.searchPerson).clear()
                sleep(1)
        flow.find_element(FlowPage.ensureSelectPersonTwo).click()
        sleep(1)




