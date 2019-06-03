# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewTripTypePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # 进入行程类型页面后，点击+
    add = (By.CSS_SELECTOR, ".layout-content-left>div>img")
    # 新增交通行程类型
    addTra = (By.CSS_SELECTOR, ".ant-dropdown-menu-item:nth-child(1)")
    # 新增住宿行程类型
    addHos = (By.CSS_SELECTOR, ".ant-dropdown-menu-item:nth-child(2)")
    # 输入行程类型名称，目前编码取的是系统默认的
    tripTypeName = (By.CSS_SELECTOR, "input[placeholder='请输入行程类型名称']")
    # 保存行程类型的名字
    saveTripType = (By.CSS_SELECTOR, ".modal-footer.horizontal>button:nth-child(2)")
    # 字段设置
    fieldSetting = (By.CSS_SELECTOR, ".ant-tabs-nav.ant-tabs-nav-animated>div:nth-child(3)")
    # 字段设置-停用
    disableSetting = (By.CSS_SELECTOR, ".action-footer-bar___1grEr>div>button:nth-child(1)")
    # 字段设置-保存
    saveSetting = (By.CSS_SELECTOR, ".action-footer-bar___1grEr>div>button:nth-child(2)")
    # 字段设置修改后保存
    #save = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-no-animated>div:nth-child(2)>div>div>div:nth-child(2)>div:nth-child(2)>button")
    # 字段设置页面添加字段
    addField = (By.CSS_SELECTOR, ".simulator-tool-bar>div:nth-child(1)")
    # 添加说明文本
    explanatoryText = (By.CSS_SELECTOR, ".simulator-tool-bar>div:nth-child(3)")
    # 搜索字段名称
    searchField = (By.CSS_SELECTOR, "input[placeholder='搜索字段名称']")
    # 选中搜索的字段
    ensureSearchField = (By.CSS_SELECTOR, ".field-item>div")
    # 确定
    ensureBut = (By.CSS_SELECTOR, ".custom-field-modal>div:nth-child(2)>div:nth-child(2)>button:nth-child(3)")
    # 搜索行程类型
    searchTripType = (By.CSS_SELECTOR, "input[placeholder='输入名称进行搜索']")
    #行程类型确定操作
    ensureSearchTypeTypeOne = (By.CSS_SELECTOR, ".trip-type")
    # 停用确定操作
    ensureDisable = (By.CSS_SELECTOR, ".ant-confirm-btns>button:nth-child(2)")
    # 获取模板
    getTripType = (By.CSS_SELECTOR, ".trip-type>div>div:nth-child(2)")
