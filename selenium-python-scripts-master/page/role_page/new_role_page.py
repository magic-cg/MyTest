# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewRole(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # 新建
    newRole = (By.CSS_SELECTOR, ".ant-btn.ant-dropdown-trigger.ant-btn-primary")
    # 角色分组
    groupRole = (By.CSS_SELECTOR, ".ant-dropdown-menu.ant-dropdown-menu-vertical.ant-dropdown-menu-light.ant-dropdown-menu-root>li:nth-child(1)>a")
    # 角色
    role = (By.CSS_SELECTOR, ".ant-dropdown-menu.ant-dropdown-menu-vertical.ant-dropdown-menu-light.ant-dropdown-menu-root>li:nth-child(2)>a")
    # 角色组名称
    groupRoleName = (By.ID, "name")
    # 角色名称
    roleName = (By.ID, "name")
    # 角色类型(默认为普通，暂不修改)

    # 指定角色组
    selectRoleGroup = (By.CSS_SELECTOR, "div[title='未分组']")
    # 确定选择的角色组
    ensureRoleGroup = (By.CSS_SELECTOR, "ul[role='menu']>li:nth-child(2)")
    # 确定角色
    ensureBut = (By.CSS_SELECTOR, ".add-role-modal>div:nth-child(3)>button:nth-child(2)")
    # 确定角色组
    ensureBut1 = (By.CSS_SELECTOR, ".ant-btn.btn-ml.ant-btn-primary")
    # 添加
    addRoler = (By.CSS_SELECTOR, ".ant-btn.add-button.mr-10")
