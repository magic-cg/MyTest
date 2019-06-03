# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewExpensePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    # 新建报销
    newExpense = (By.CLASS_NAME, "expense-hover")
    # 选择模板
    chooseModel = (By.CSS_SELECTOR, "div[style = 'display: block; opacity: 1;']")
    # 报销单标题
    expenseTitle = (By.CSS_SELECTOR, "input[placeholder='请输入标题']")
    # 描述
    describe = (By.CSS_SELECTOR, "input[placeholder='请输入描述']")
    # 项目
    project = (By.CSS_SELECTOR, ".flex-1.ovr-y-a>div>div:nth-child(3)>div:nth-child(10)>div:nth-child(2)>div>span>div>span>span>span>span")
    # 选择某一项目
    selectProject = (By.CSS_SELECTOR, ".flex-1.ovr-y-a>div>div:nth-child(3)>div:nth-child(10)>div:nth-child(2)>div>span>div>div>div>div>div>span>span>input")
    # 确定选择的项目
    ensureProject = (By.CSS_SELECTOR, ".highlight")
    # 自定义的字段，枚举类型
    enumeration = (By.CSS_SELECTOR, ".flex-1.ovr-y-a>div>div:nth-child(3)>div:nth-child(11)>div:nth-child(2)>div>div>div>div>div")
    # 选择经济舱
    selectEnumeration = (By.CSS_SELECTOR, "div[style='overflow: auto;']>ul>li:nth-child(1)")
    # 添加费用明细
    costDetail = (By.CLASS_NAME, "import-detail")
    # 费用类型
    feeType = (By.CSS_SELECTOR, ".feeType_select_wrap___7deVR>span>span>span:nth-child(2)")
    # 搜索费用类型
    selectFeeType = (By.CSS_SELECTOR, ".ant-select-dropdown-search>span:nth-child(1)>input:nth-child(1)")
    # 确定选择的费用类型
    ensureFeeType = (By.CSS_SELECTOR, ".ant-select-tree-title>div>span>div")
    # 金额
    # expenseAmount = (By.CSS_SELECTOR, "input[placeholder='请输入金额']")
    expenseAmount = (By.CSS_SELECTOR, ".fee-detail-edit___1gxeE>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>span>div>div>div>input:nth-child(2)")
    # 自动计算的金额
    autExpenseAmount = (By.CSS_SELECTOR, ".fee-detail-edit___1gxeE>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>div>input")
    # 再记一笔
    writeAgain = (By.CSS_SELECTOR, ".ant-modal-body>div>div:nth-child(3)>button:nth-child(2)")
    # 单价
    unitPrice = (By.CSS_SELECTOR, ".fee-detail-edit___1gxeE>div:nth-child(2)>div:nth-child(9)>div:nth-child(2)>div>div>div>div>input:nth-child(2)")
    # 数量
    quantity = (By.CSS_SELECTOR, "input[placeholder='请输入数量']")
    # 保存消费明细
    saveCostDetail = (By.CSS_SELECTOR, ".ant-modal-body>div>div:nth-child(3)>button:nth-child(3)")
    # 借款未核销文本title
    loanText = (By.CSS_SELECTOR, ".ant-confirm-title")
    # 费用超标提醒的文本
    freeExceed = (By.CSS_SELECTOR, ".ant-confirm-content")
    # 提交单据时各种确认提示:借款未核销、费用超标、预算超标、修改费用分摊方式
    continueOrNot = (By.CSS_SELECTOR, ".ant-confirm-btns>button:nth-child(2)")
    # 提交送审
    submitExpense = (By.CSS_SELECTOR, ".button_group_wrapper___3M-uZ>button:nth-child(3)")
    # 剩余借款
    remainLoan = (By.CSS_SELECTOR, ".amount.apply-txt")
    # 我的借款
    myLoan = (By.CSS_SELECTOR, ".amount.rest-amount")
    # 预算超标的文本
    budget = (By.CSS_SELECTOR, ".ant-confirm-content")
    # 修改报销单的费用明细的第一条
    feeItemFirst = (By.CSS_SELECTOR, ".item-main>div:nth-child(1)")
    # 开启费用分摊按钮
    expenseShareBut = (By.CSS_SELECTOR, ".ant-col-offset-5.apportion-header___YPvhl>label:nth-child(1)>span:nth-child(1)>input")
    # 分摊部门
    shareDep = (By.CSS_SELECTOR, ".apportion-edit-card___32uOF>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>span>div>span>span>span:nth-child(1)")
    # 搜索部门、项目
    searchDep = (By.CSS_SELECTOR, ".pl-24.pr-24>div>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>span>div>div>div>div>div>span>span>input")
    # 确定搜索部门、项目
    ensureSearchDep = (By.CSS_SELECTOR, ".highlight")
    # 分摊比例
    shareScale = (By.CSS_SELECTOR, "input[placeholder='请输入分摊比例']")
    # 保存分摊比例
    saveShare = (By.CSS_SELECTOR, ".apportion-edit-card___32uOF>div:nth-child(3)>div:nth-child(1)>button")
    # 添加分摊
    addShare = (By.CSS_SELECTOR, "#apportion-action>div:nth-child(1)>div:nth-child(2)")
    # 分摊总金额
    shareTotle = (By.CSS_SELECTOR, ".apportion-total___arVwD>div>div>div>span:nth-child(2)")
    # 分摊方式
    shareWay = (By.CSS_SELECTOR, "#ekbc-modal-select-custom_z>div:nth-child(1)>div:nth-child(2)>div>div>div>div:nth-child(1)")
    # 在分摊时选择部门、项目时的分摊项目选项
    sharePro = (By.CSS_SELECTOR, ".apportion-edit-card___32uOF>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>div>span>span>span:nth-child(1)>span")
    # 在分摊时选择部门、项目时的分摊项目的搜索
    searchPro = (By.CSS_SELECTOR, ".pl-24.pr-24>div>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>span:nth-child(1)>span>input")
    # 在分摊时选择部门、项目时的分摊项目的搜索的确定操作
    ensureSearchPro = (By.CSS_SELECTOR, ".apportion-edit-card___32uOF>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>ul:nth-child(2)>li>span:nth-child(2)>span>span>span>mark:nth-child(1)")
    # 费用明细全选按钮
    checkAllBut = (By.CSS_SELECTOR, ".header-wrapper___1D3HG>div:nth-child(2)>label:nth-child(1)>span>input")
    # 批量费用分摊
    batchShare = (By.CSS_SELECTOR, ".header-wrapper___1D3HG>div:nth-child(2)>span:nth-child(6)")
    # 批量分摊下的分摊比例和
    totalScale = (By.CSS_SELECTOR, ".apportion-total___arVwD>div")
    # 保存批量费用分摊
    saveShareBut = (By.CSS_SELECTOR, ".batch-apportion-modal___3bBEv>div:nth-child(3)>button:nth-child(2)")
    # 添加分摊
    addVerificationBut = (By.CSS_SELECTOR, ".empty-btn")
    # 修改分摊方式的文案
    shareText = (By.CSS_SELECTOR, ".ant-confirm-title")
    # 确认选择的核销借款
    ensureLoan = (By.CSS_SELECTOR, ".footer-writtenOff>button")
    # 关联申请单
    addRequisition = (By.CSS_SELECTOR, ".import-select>div>div>div:nth-child(1)")
    # 导入电子发票
    exportInvoice = (By.CSS_SELECTOR, ".import.ml-8.ant-dropdown-trigger")
    # 费用类型中的费用标准字段：航班
    flightSta = (By.CSS_SELECTOR, ".fee-detail-edit___1gxeE>div:nth-child(2)>div:nth-child(9)>div:nth-child(2)>div>span>div>div>div:nth-child(1)>div")
    # 酒店标准下的起止日期
    startEnd = (By.CSS_SELECTOR, ".fee-detail-edit___1gxeE>div:nth-child(2)>div:nth-child(9)>div:nth-child(2)>div>span>div>span>span>input:nth-child(1)")
    # 开始时间
    startTime = (By.CSS_SELECTOR, ".ant-calendar-date-panel>div:nth-child(1)>div:nth-child(1)>div>input")
    # 结束时间
    endTime = (By.CSS_SELECTOR, ".ant-calendar-date-panel>div:nth-child(3)>div:nth-child(1)>div>input")
