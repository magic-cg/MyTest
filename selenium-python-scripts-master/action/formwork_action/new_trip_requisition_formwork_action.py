# -*- coding: utf-8 -*-
from common.common_menu_page import CommonMenus
from page.formwork_page.new_requisition_formwork_page import NewRequisitionFormWorkPage
from time import sleep


class NewTrapRequisitionFormWorkAction:

    # 进入到单据类型模块
    def enter_requisition_formwork(self, driver):
        common_menus = CommonMenus(driver)
        common_menus.find_element(CommonMenus.enterpriseManagement).click()
        common_menus.find_element(CommonMenus.documentType).click()

    # 新建申请单
    def new_requisition_formwork(self, driver, requisition_model_name):

        new_requisition_fw = NewRequisitionFormWorkPage(driver)
        # 新建申请单模板
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.add).click()
        sleep(1)
        new_requisition_fw.find_element1(NewRequisitionFormWorkPage.addRequisition).click()
        # 申请单模板名字
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.requisitionFormWorkTypeName).send_keys(requisition_model_name)
        # 选择审批流
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.requisitionFlow).click()
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.selectRequisitionFlow).click()
        # 选择打印模板
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.printModel).click()
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.selectPrintModel).click()
        # 申请内容选择填写申请金额和差旅行程
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.requisitionContent4).click()
        # 保存
        new_requisition_fw.find_element(NewRequisitionFormWorkPage.saveRequisitionFormWork).click()
        sleep(2)




