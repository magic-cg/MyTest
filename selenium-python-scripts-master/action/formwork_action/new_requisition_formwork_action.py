# -*- coding: utf-8 -*-
from common.common_menu_page import CommonMenus
from page.formwork_page.new_requisition_formwork_page import NewRequisitionFormWorkPage
from time import sleep
import config.global_variable as gv


class NewRequisitionFormWorkAction:

    # 进入到单据类型模块
    def enter_requisition_formwork(self, driver):
        common_menus = CommonMenus(driver)
        common_menus.find_element(CommonMenus.enterpriseManagement).click()
        common_menus.find_element(CommonMenus.documentType).click()

    # 新建报销单
    def new_requisition_formwork(self, driver, requisition_model_name):

        new_requisition_fw = NewRequisitionFormWorkPage(driver)
        # 新建申请单模板
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.add).click()
        sleep(1)
        new_requisition_fw.find_element1(NewRequisitionFormWorkPage.addRequisition).click()
        # 申请单模板名字
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.requisitionFormWorkTypeName).send_keys(requisition_model_name)

    def requisition_flow(self, driver):
        new_requisition_fw = NewRequisitionFormWorkPage(driver)

        # 选择审批流
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.requisitionFlow).click()
        sleep(1)
        select_flow = driver.find_element_by_css_selector("ul[role = 'listbox']")

        allOption = select_flow.find_elements_by_tag_name("li")
        for option in allOption:
            # print "Value is: " + option.get_attribute("value")
            # print "Text is:" + option.text
            if gv.flow_name1 in option.text:
                option.click()
                break

    def print_model(self, driver):
        new_requisition_fw = NewRequisitionFormWorkPage(driver)

        # 选择打印模板
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.printModel).click()
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.selectPrintModel).click()

    def write_money_direct(self, driver):
        new_requisition_fw = NewRequisitionFormWorkPage(driver)

        # 申请为直接填写金额
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.requisitionContent1).click()

    def write_trip_direct(self, driver):
        new_requisition_fw = NewRequisitionFormWorkPage(driver)

        # 申请内容选择直接填写行程
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.requisitionContent3).click()

    def close_requisition_rule2(self, driver):
        new_requisition_fw = NewRequisitionFormWorkPage(driver)

        # 申请关闭方式选择报销金额≥申请金额时自动关闭
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.closeRequisitionRule2).click()

    def close_requisition_rule3(self, driver):
        new_requisition_fw = NewRequisitionFormWorkPage(driver)

        # 申请关闭方式选择达到报销次数自动关闭
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.closeRequisitionRule3).click()

    def save(self, driver):
        new_requisition_fw = NewRequisitionFormWorkPage(driver)

        # 保存
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.saveRequisitionFormWork).click()
        sleep(2)

    def requisition_flow1(self, driver):
        new_requisition_fw = NewRequisitionFormWorkPage(driver)

        # 选择审批流
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.requisitionFlow).click()
        sleep(1)
        select_flow = driver.find_element_by_css_selector("ul[role = 'listbox']")

        allOption = select_flow.find_elements_by_tag_name("li")
        for option in allOption:
            # print "Value is: " + option.get_attribute("value")
            # print "Text is:" + option.text
            if gv.flow_name2 in option.text:
                option.click()
                break