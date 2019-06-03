# -*- coding: utf-8 -*-
from page.loan_page.repay_loan_page import RepaymentPage
from common.common_menu_page import CommonMenus
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class RepayLoanAction:

    def get_loan_list(self, driver):
        repay = RepaymentPage(driver)

        # 点击剩余借款
        repay.find_element(RepaymentPage.remainingLoan).click()
        sleep(1)
        # 获取当前借款列表中的金额是否不为0
        # 通过循环拿到所有的借款单
        ul = driver.find_element_by_css_selector(".myLoan-list>ul")
        lis = ul.find_elements_by_tag_name("li")
        return len(lis)

    def repay(self, driver, loan_list):
        # 此模块是做发起还款功能
        repay = RepaymentPage(driver)
        for i in range(loan_list):
            i = i+1
            value = driver.find_element_by_xpath("//div[@class='myLoan-list']/ul/li[%s]/div[2]/div/span[2]" % i).text
            # 首先判断此借款单是否还款金额为0
            if value != u'0.00':
                driver.find_element_by_xpath("//div[@class='myLoan-list']/ul/li[%s]/div[2]/div/span[2]" % i).click()
                # 再判断还款按钮是否可点击
                button_state = repay.find_element(RepaymentPage.repayment).is_enabled()
                if button_state:
                    repay.find_element(RepaymentPage.repayment).click()
                    # 输入还款金额
                    repay.find_element(RepaymentPage.amount).send_keys(1)
                    repay.find_element(RepaymentPage.confirm).click()
                    sleep(1)
                    break
                else:
                    # 返回借款列表下
                    repay.find_element(RepaymentPage.returnList).click()
                    sleep(1)
            while i == loan_list:
                if value == u'0.00':
                    print u'所有借款均在还款中'

        # 这个地方可以加断言，来判断是否发起还款正确
        driver.refresh()
        sleep(2)

    def cashier_reject(self, driver, refused_reason):

        common_menu = CommonMenus(driver)
        repay = RepaymentPage(driver)
        ActionChains(driver).move_to_element(common_menu.find_element(CommonMenus.financeManagement)).perform()
        common_menu.find_element(CommonMenus.loanManagement).click()
        repay.find_element(RepaymentPage.repaymentApply).click()
        # 出纳拒绝此次还款
        repay.find_element(RepaymentPage.refused).click()
        repay.find_element(RepaymentPage.refusedReason).send_keys(refused_reason)
        repay.find_element(RepaymentPage.confirmBut).click()
        sleep(2)
        # 回到首页去
        driver.refresh()
        sleep(2)
        common_menu.find_element(CommonMenus.firstPage).click()
        sleep(2)

    def cashier_agree(self, driver):
        common_menu = CommonMenus(driver)
        repay = RepaymentPage(driver)
        # 进入借款管理
        ActionChains(driver).move_to_element(common_menu.find_element(CommonMenus.financeManagement)).perform()
        common_menu.find_element(CommonMenus.loanManagement).click()

        repay.find_element(RepaymentPage.repaymentApply).click()

        # 出纳确认还款
        repay.find_element(RepaymentPage.confirmColl).click()
        # 选择收款方式
        repay.find_element1(RepaymentPage.paymentAccount).click()
        repay.find_element1(RepaymentPage.someoneAccount).click()
        repay.find_element(RepaymentPage.confirmBut).click()
        sleep(2)
        # 关闭还款申请页面
        repay.find_element(RepaymentPage.closePage).click()
        sleep(2)








