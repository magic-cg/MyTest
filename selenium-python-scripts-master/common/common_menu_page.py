# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage

# 列举出所有菜单栏项


class CommonMenus(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 首页
    firstPage = (By.CSS_SELECTOR, ".ekb-menu-top>li:nth-child(1)")
    # 待办
    toDo = (By.CSS_SELECTOR, ".ekb-menu-top>li:nth-child(2)")
    # 待审批
    pending = (By.CSS_SELECTOR, ".layout-menu-normal>ul>li:nth-child(1)>div:nth-child(1)")
    # 待支付
    toBePaid = (By.CSS_SELECTOR, ".layout-menu-normal>ul>li:nth-child(2)>div:nth-child(1)")
    # 开启系统管理员和财务管理字段，要不然定位会有问题
    # 企业管理
    enterpriseManagement = (By.CSS_SELECTOR, ".ekb-menu-top>li:nth-child(5)")
    # 功能授权
    functionAuthorization = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(2)>ul>li:nth-child(1)>div")
    # 角色管理
    roleManagement = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(2)>ul>li:nth-child(2)>div")
    # 权限管理
    rightsManagement = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(2)>ul>li:nth-child(3)>div")
    # 通讯录
    addressBook = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(2)>ul>li:nth-child(4)>div")
    # 单据类型
    documentType = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(1)>div")
    # 费用类型
    costType = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(2)>div")
    # 行程类型
    tripType = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(3)>div")
    # 审批流
    flow = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(4)>div")
    # 收款信息
    collInfo = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(5)>div")
    # 支付账户
    paymentAccount = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(6)>div")
    # 自定义档案
    archives = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(7)>div")
    # 费用标准
    chargeStandard = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(9)>div")
    # 城市等级
    cityLevel = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(10)>div")
    # 多币种
    multiCurrency = (By.CSS_SELECTOR, ".layout-menu-enterprise-manage>dl>dd:nth-child(4)>ul>li:nth-child(11)>div")

    # 财务管理，(权限不同，导致其菜单定位不同，所以赋予的权限有：报销单管理，借款单管理，申请单管理，预算控制)
    financeManagement = (By.CSS_SELECTOR, ".ekb-menu-top>li:nth-child(4)")
    # 报销单管理
    expenseManagement = (By.CSS_SELECTOR, ".layout-menu-normal>ul>li:nth-child(1)>div")
    # 借款管理
    loanManagement = (By.CSS_SELECTOR, ".layout-menu-normal>ul>li:nth-child(2)>div")
    # 申请管理
    applicationManagement = (By.CSS_SELECTOR, ".layout-menu-normal>ul>li:nth-child(3)>div")
    # 预算控制
    budgetManagement = (By.CSS_SELECTOR, ".layout-menu-normal>ul>li:nth-child(4)>div")

