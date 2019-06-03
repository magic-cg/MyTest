# -*- coding: utf-8 -*-

from common.common_menu_page import CommonMenus
from page.role_page.new_role_page import NewRole
from time import sleep
from action.select_components_action import Select
import config.global_variable as gv

class NewRoler:

    def new_group_role(self, driver, group_role_name):
        commom_menu = CommonMenus(driver)
        new_role = NewRole(driver)
        # 进入到角色管理页面下
        commom_menu.find_element(CommonMenus.enterpriseManagement).click()
        commom_menu.find_element(CommonMenus.roleManagement).click()
        # 新增角色组
        new_role.find_element(NewRole.newRole).click()
        new_role.find_element(NewRole.groupRole).click()
        new_role.find_element(NewRole.groupRoleName).send_keys(group_role_name)
        # 确定
        new_role.find_element(NewRole.ensureBut1).click()
        sleep(2)
        driver.refresh()
        sleep(2)

    def new_role(self, driver, role_name):

        new_role = NewRole(driver)
        new_role.find_element(NewRole.newRole).click()
        new_role.find_element(NewRole.role).click()
        new_role.find_element(NewRole.roleName).send_keys(role_name)
        # 角色类型默认为：普通
        # 指定角色组：获取不到指定的角色组，忧伤，只能取默认的角色组了
        new_role.find_element(NewRole.selectRoleGroup).click()
        sleep(1)
        # 获取下拉框中所有的角色组
        # select_role = driver.find_element_by_css_selector("ul[role = 'menu']")
        # allOptions = select_role.find_elements_by_tag_name("li")
        # for option in allOptions:
        #     print option.text
        #     if u'职务' in option.text:
        #         if option.is_enabled():
        #             option.click()
        #             break

        # 确定
        new_role.find_element(NewRole.ensureBut).click()
        sleep(2)

    def select_roler(self, driver):

        new_role = NewRole(driver)
        select = Select()
        # 添加角色人
        new_role.find_element(NewRole.addRoler).click()
        sleep(1)
        # 调用多选选人组件
        select.multiple_components(driver)
        sleep(2)


