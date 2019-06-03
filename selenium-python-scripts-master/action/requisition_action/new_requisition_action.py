# -*- coding: utf-8 -*-
from time import sleep
from page.requisition_page.create_requisition_page import CreateRequisitionPage
from common.exist import Exist

import config.global_variable as gv


class NewRequisitionPage:

    def new_requisition(self, driver):

        create_requisition = CreateRequisitionPage(driver)
        create_requisition.find_element(CreateRequisitionPage.newRequisition).click()

    # 选择申请单模板
    def select_model(self, driver, requisition_title, requisition_model_name):
        create_requisition = CreateRequisitionPage(driver)
        # 选择申请单模板
        create_requisition.find_element(CreateRequisitionPage.selectModel).click()
        sleep(2)
        selectModel = driver.find_element_by_css_selector("ul[role = 'listbox']")
        allOption = selectModel.find_elements_by_tag_name("li")
        for option in allOption:
            if requisition_model_name in option.text:
                option.click()
                break
        sleep(0.5)
        # 填写申请单标题
        create_requisition.find_element(CreateRequisitionPage.requisitionTitle).send_keys(requisition_title)

    def requisition_detail(self, driver, fee_type, requisition_amount):
        create_requisition = CreateRequisitionPage(driver)

        # 填写申请单费用明细
        create_requisition.find_element(CreateRequisitionPage.costDetail).click()
        sleep(2)
        # 选择费用类型

        create_requisition.find_element(CreateRequisitionPage.feeType).click()
        create_requisition.find_element(CreateRequisitionPage.selectFeeType).send_keys(fee_type)
        sleep(1)
        create_requisition.find_element(CreateRequisitionPage.ensureFeeType).click()
        sleep(0.5)
        create_requisition.find_element(CreateRequisitionPage.requisitionMoney).send_keys(requisition_amount)
        # 再记一笔
        create_requisition.find_element(CreateRequisitionPage.writeAgain).click()
        create_requisition.find_element(CreateRequisitionPage.requisitionMoney).send_keys(requisition_amount)
        # 保存费用明细
        create_requisition.find_element(CreateRequisitionPage.saveCostDetailBut).click()
        sleep(2)

    def requisition_money(self, driver):
        create_requisition = CreateRequisitionPage(driver)
        # 直接填写申请金额
        create_requisition.find_element(CreateRequisitionPage.costDirectly).send_keys(50)

    # 提交申请单成功后，弹出关注易快报微信服务号
    def remind(self, driver):
        create_requisition = CreateRequisitionPage(driver)
        exist = Exist(driver)
        remind_text = exist.is_element_exist(CreateRequisitionPage.noRemindText)
        # 根据是否弹出提示框来判断要不要进行下列操作
        if remind_text:
            create_requisition.find_element(CreateRequisitionPage.noRemind).click()
            sleep(1)
            # 确定
            create_requisition.find_element(CreateRequisitionPage.remindEnsure).click()
            sleep(0.5)
        else:
            pass






