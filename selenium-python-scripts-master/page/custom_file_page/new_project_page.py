# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewProjectPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        # 项目
    project = (By.CSS_SELECTOR, ".custom-dimension-content>div:nth-child(1)")
    # 新建
    new = (By.CSS_SELECTOR, ".left-part>div:nth-child(1)>button:nth-child(2)")
    # 项目名称
    projectName = (By.ID, "name")
    # 保存
    save = (By.CSS_SELECTOR, ".ant-col-20>button:nth-child(1)")
    # 停用
    disable = (By.CSS_SELECTOR, ".ant-col-20>button:nth-child(2)")
    # 确定停用
    ensureDisable = (By.CSS_SELECTOR, ".ant-confirm-btns>button:nth-child(2)")
    # 所属上级
    superior = (By.CSS_SELECTOR, ".ant-select-selection__rendered")
    # 搜索所属上级
    selectSuperior = (By.CSS_SELECTOR, ".ant-select-search__field__wrap>input")
    # 确定所选的上级
    ensureSuperior = (By.CSS_SELECTOR, ".ant-select-tree-title")
    # 限制可见人员
    limitPerson = (By.CSS_SELECTOR, ".ant-radio-group>label:nth-child(2)>span>input")
    # 可见人员
    visiblePerson = (By.CSS_SELECTOR, ".select-tag-content>div:nth-child(2)")
    # 左侧搜索框
    search = (By.CSS_SELECTOR, "input[placeholder='输入名称或编码进行搜索']")
    # 点击搜索后项目
    clickSearchProject = (By.CSS_SELECTOR, ".line-style>span>mark")
    # dict = {'project': project,
    #              'new': new,
    #              'projectName': projectName,
    #              'save': save,
    #              'disable': disable,
    #              'ensureDisable': ensureDisable,
    #              'superior': superior,
    #              'selectSuperior': selectSuperior,
    #              'ensureSuperior': ensureSuperior,
    #              'limitPerson': limitPerson,
    #              'visiblePerson': visiblePerson,
    #              'search': search,
    #              'clickSearchProject': clickSearchProject
    #              }


