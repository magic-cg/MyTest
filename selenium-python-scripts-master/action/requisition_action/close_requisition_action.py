# -*- coding: utf-8 -*-
from time import sleep
from page.requisition_page.close_requisition_page import CloseRequisitionPage
import config.global_variable as gv


class CloseRequisitionAction:

    def close_requisition(self, driver):
        close_requisi = CloseRequisitionPage(driver)
        # 手动关闭申请单
        close_requisi.find_element1(CloseRequisitionPage.requisitionItem).click()
        # sleep(1)
        close_requisi.find_element1(CloseRequisitionPage.closeFirstOne).click()
        # sleep(1)
        close_requisi.find_element1(CloseRequisitionPage.closeBut).click()
        close_requisi.find_element1(CloseRequisitionPage.inputRequiMoney).send_keys(gv.requisition_amount*2)
        close_requisi.find_element1(CloseRequisitionPage.ensureBut).click()
        sleep(2)

