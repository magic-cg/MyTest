# -*- coding: utf-8 -*-
from page.requisition_page.initiate_expense_page import InitiateExpensePage
from time import sleep
from common.common_menu_page import CommonMenus
from action.select_components_action import Select
import config.global_variable as gv

class InitiateExpenseAction:

    def initiate_expense(self, driver):

        initiate_requis = InitiateExpensePage(driver)
        # 进入申请单列表下
        initiate_requis.find_element(InitiateExpensePage.requisitionItem).click()
        # 选择列表下第一个申请单，发起报销
        initiate_requis.find_element1(InitiateExpensePage.initiateFirstOne).click()
        # 发起报销
        initiate_requis.find_element1(InitiateExpensePage.initiateRequisition).click()
        sleep(2)

    def share_requistion(self, driver):
        initiate_requis = InitiateExpensePage(driver)
        select = Select()
        common_menus = CommonMenus(driver)
        # 返回到首页
        common_menus.find_element(CommonMenus.firstPage).click()
        # 进入申请单列表下
        initiate_requis.find_element(InitiateExpensePage.requisitionItem).click()
        # 选择列表下第一个申请单
        initiate_requis.find_element1(InitiateExpensePage.initiateFirstOne).click()
        # 共享
        initiate_requis.find_element(InitiateExpensePage.shareRequisition).click()
        sleep(2)
        # 添加共享人
        initiate_requis.find_element(InitiateExpensePage.addSharer).click()
        sleep(1)
        # 调用多选选人组件
        select.multiple_components(driver)
        # 确定
        initiate_requis.find_element(InitiateExpensePage.ensure).click()
        sleep(2)

    def shift_requistion(self, driver):
        initiate_requis = InitiateExpensePage(driver)
        select = Select()
        common_menus = CommonMenus(driver)
        # 返回到首页
        common_menus.find_element(CommonMenus.firstPage).click()
        # 进入申请单列表下
        initiate_requis.find_element(InitiateExpensePage.requisitionItem).click()
        # 选择列表下第一个申请单
        initiate_requis.find_element1(InitiateExpensePage.initiateFirstOne).click()
        # 共享
        initiate_requis.find_element(InitiateExpensePage.shiftRequisition).click()
        sleep(2)
        # 添加共享人
        initiate_requis.find_element(InitiateExpensePage.selectShifter).click()
        sleep(1)
        # 调用多选选人组件
        select.multiple_components(driver)
        # 确定
        initiate_requis.find_element(InitiateExpensePage.ensure).click()
        sleep(2)