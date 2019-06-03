# -*- coding: utf-8 -*-
from common.common_menu_page import CommonMenus
from page.permissions_page.permissions_setting_page import Permissions
from time import sleep
from action.select_components_action import Select


class Permission:

    def perssion_expense(self, driver):

        # 进入权限管理
        common_menu = CommonMenus(driver)
        permissions = Permissions(driver)
        select = Select()

        common_menu.find_element(CommonMenus.enterpriseManagement).click()
        common_menu.find_element(CommonMenus.rightsManagement).click()

        # 设置报销单管理权限人员
        permissions.find_element(Permissions.editThree).click()
        sleep(1)
        select.permission_components(driver)

    def perssion_loan(self, driver):

        # 设置借款管理权限人员
        permissions = Permissions(driver)
        select = Select()

        permissions.find_element(Permissions.editFour).click()
        sleep(1)
        select.permission_components(driver)

    def perssion_requisition(self, driver):

        # 设置申请管理权限人员
        permissions = Permissions(driver)
        select = Select()

        permissions.find_element(Permissions.editFive).click()
        sleep(1)
        select.permission_components(driver)

    def perssion_budget(self, driver):

        # 设置申请管理权限人员
        permissions = Permissions(driver)
        select = Select()

        permissions.find_element(Permissions.editSix).click()
        sleep(1)
        select.permission_components(driver)
