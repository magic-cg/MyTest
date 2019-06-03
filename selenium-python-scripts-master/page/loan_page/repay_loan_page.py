# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class RepaymentPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 此部分功能主要是发起还款的功能
    # 我的借款
    myLoan = (By.CSS_SELECTOR, ".amount.rest-amount")
    # myLoan = (By.XPATH, "//div[text()='我的借款']")
    # 剩余借款
    remainingLoan = (By.CSS_SELECTOR, ".amount.apply-txt")
    # remainingLoan = (By.XPATH, "//div[text()='剩余借款']")
    # 获取借款列表上的第一个借款单的标题
    loanListNameOne = (By.CSS_SELECTOR, '.myLoan-list>ul>li:nth-child(1)>div:nth-child(1)>div:nth-child(1)')
    # 借款列表第一个借款单,后期能不能遍历出所有的借款单，从中选择自己想要的呢？
    loanListOne = (By.CSS_SELECTOR, ".myLoan-list>ul>li:nth-child(1)")
    # 还款
    repayment = (By.CSS_SELECTOR, ".ant-btn.w-100.ant-btn-primary")
    # 输入还款金额
    amount = (By.ID, "amount")
    # 确定
    confirm = (By.CSS_SELECTOR, ".ant-btn.btn-ml.ant-btn-primary")
    # 返回借款列表
    returnList = (By.CSS_SELECTOR, ".ekb-breadcrumb-wrapper>div>span:nth-child(1)>a")
    # 还款申请
    repaymentApply = (By.CSS_SELECTOR, ".menu-bar___Ue0jZ>div:nth-child(1)")
    # 搜索借款单名称
    searchLoanTitle = (By.CSS_SELECTOR, "input[placeholder='搜索借款人或借款名称']")
    # 确认收款
    confirmColl = (By.CSS_SELECTOR, ".color-blue.cur-p")
    # 收款账户文本框
    paymentAccount = (By.CSS_SELECTOR, ".ant-select-selection__rendered>div")
    # 选择某一收款账户（目前还没实现拿到所有的收款信息列表）
    someoneAccount = (By.CSS_SELECTOR, "div[style='overflow: auto;']>ul>li:nth-child(1)")
    # 驳回
    refused = (By.CSS_SELECTOR, ".color-red.cur-p.ml-30")
    # 驳回原因
    refusedReason = (By.ID, "reason")
    # 确定按钮
    confirmBut = (By.CSS_SELECTOR, ".ant-btn.ant-btn-primary:nth-child(2)")
    # 关闭还款申请页面
    closePage = (By.CSS_SELECTOR, ".anticon.anticon-cross.cross-icon")
    # dict = {'remainingLoan': remainingLoan,
    #              'loanListName': loanListName,
    #              'loanList': loanList,
    #              'repayment': repayment,
    #              'amount': amount,
    #              'confirm': confirm,
    #              'repaymentApply': repaymentApply,
    #              'searchLoanTitle': searchLoanTitle,
    #              'confirmColl': confirmColl,
    #              'paymentAccount': paymentAccount,
    #              'someoneAccount': someoneAccount,
    #              'confused': refused,
    #              'refusedReason': refusedReason,
    #              'confirmBut': confirmBut
    #              }




