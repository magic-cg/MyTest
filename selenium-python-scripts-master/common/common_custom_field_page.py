# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from basepage import BasePage


class CustomFieldPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    # 添加字段
    addField = (By.CSS_SELECTOR, ".simulator-tool-bar>div:nth-child(1)")
    # 添加分割线
    divider = (By.CSS_SELECTOR, ".simulator-tool-bar>div:nth-child(5)")
    # 添加说明文本
    explanatoryText = (By.CSS_SELECTOR, ".simulator-tool-bar>div:nth-child(3)")
    # 添加自定义字段
    addCustomField = (By.CSS_SELECTOR, ".create-btn___2VA8M")
    # 确定
    ensureBut = (By.CSS_SELECTOR, ".custom-field-modal>div:nth-child(2)>div:nth-child(2)>button:nth-child(2)")
    # 取消
    cancelBut = (By.CSS_SELECTOR, ".custom-field-modal>div:nth-child(2)>div:nth-child(2)>button:nth-child(2)")
    # 添加文本类型字段,默认勾选
    addTextType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(1)>label:nth-child(1)>span>input")
    # 添加数字类型字段
    addNumType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(1)>label:nth-child(2)>span>input")
    # 单位
    unit = (By.ID, "dataType.unit")
    # 添加金额类型字段
    moneyType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(1)>label:nth-child(3)>span>input")
    # 添加日期类型字段
    dateType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(1)>label:nth-child(4)>span>input")
    # 添加开关类型字段
    switchType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(2)>label:nth-child(1)>span>input")
    # 添加部门类型字段
    departmentType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(2)>label:nth-child(3)>span>input")
    # 附件
    # 添加员工类型字段
    staffType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(2)>label:nth-child(4)>span>input")
    # 添加城市类型字段
    cityType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(2)>label:nth-child(5)>span>input")
    # 添加枚举类型字段
    enumerationType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(3)>label:nth-child(1)>span>input")
    # 引用枚举、档案
    referEnumeration = (By.CSS_SELECTOR, ".ant-select-selection__placeholder")
    # 航班舱型
    flight = (By.CSS_SELECTOR, ".ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child(1)")
    # 火车席别
    train = (By.CSS_SELECTOR, ".ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child(2)")
    # 轮船舱型
    steamer = (By.CSS_SELECTOR, ".ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child(3)")
    # 添加自定义档案字段
    archivesType = (By.CSS_SELECTOR, ".ant-radio-group.type-radio>div:nth-child(3)>label:nth-child(3)>span>input")
    # 项目
    project = (By.CSS_SELECTOR, ".ant-select-dropdown-menu.ant-select-dropdown-menu-vertical.ant-select-dropdown-menu-root>li:nth-child(1)")
    # 字段名称
    fieldName = (By.ID, "label")
    # 搜索
    searchField = (By.CSS_SELECTOR, "input[placeholder='搜索字段名称']")
    # 搜索无结果
    no_Result = (By.CSS_SELECTOR, ".no-result")
