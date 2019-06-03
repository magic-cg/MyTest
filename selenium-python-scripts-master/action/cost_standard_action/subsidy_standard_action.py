# -*- coding: utf-8 -*-
from page.cost_standard_page.ticket_standard_page import NewTicketStandard
from page.cost_standard_page.subsidy_standard_page import NewSubsidyStandard
from common.common_menu_page import CommonMenus
import config.global_variable as gv
from common.common_flow_page import FlowPage
from time import sleep


class NewSubsidyStandardAction:

    def new_subsidy_standard(self, driver):
        new_ticket_sta = NewTicketStandard(driver)
        common_menu = CommonMenus(driver)

        # 进入费用标准页面
        common_menu.find_element(CommonMenus.enterpriseManagement).click()
        common_menu.find_element(CommonMenus.chargeStandard).click()
        # 新建补助标准
        new_ticket_sta.find_element(NewTicketStandard.new).click()
        new_ticket_sta.find_element(NewTicketStandard.subsidizationSta).click()

    def basic_setting(self, driver, cost_sta_name, fee_type):

        # 补助标准的基本设置
        new_ticket_sta = NewTicketStandard(driver)

        # 标准名称
        new_ticket_sta.find_element(NewTicketStandard.standardName).clear()
        new_ticket_sta.find_element(NewTicketStandard.standardName).send_keys(cost_sta_name)
        new_ticket_sta.find_element(NewTicketStandard.controlFeeType).click()
        new_ticket_sta.find_element(NewTicketStandard.selectFeeType).send_keys(fee_type)
        new_ticket_sta.find_element(NewTicketStandard.ensureLevelTwoFeeType).click()
        # 控制单据类型包括申请单和报销单：默认均勾选

    def standard_setting(self, driver, subsidy_money):
        new_ticket_sta = NewTicketStandard(driver)
        new_subsidy_sta = NewSubsidyStandard(driver)
        flow = FlowPage(driver)

        # 点击指定字段
        new_ticket_sta.find_element(NewTicketStandard.specifiedField).click()
        # 点击指定的日期范围。因为控制了申请单和报销单，所以两者均要指定
        new_ticket_sta.find_element(NewTicketStandard.clickSpecified).click()

        # 进入申请页签
        new_ticket_sta.find_element(NewTicketStandard.switch).click()
        new_ticket_sta.find_element(NewTicketStandard.clickRequSpecifiedTwo).click()
        sleep(2)
        # 保存
        new_ticket_sta.find_element(NewTicketStandard.saveSpecifiedPage).click()
        # 填写补助金额
        new_subsidy_sta.find_element(NewSubsidyStandard.subsidyMoney).clear()
        sleep(1)
        new_subsidy_sta.find_element(NewSubsidyStandard.subsidyMoney).send_keys(subsidy_money)
        # 选择适用范围
        new_ticket_sta.find_element(NewTicketStandard.selectSuitPerson).click()

        for i in range(len(gv.list_name)):

            flow.find_element(FlowPage.searchPerson).send_keys(gv.list_name[i])
            flow.find_element(FlowPage.multipleChoice).click()
            sleep(1)
            flow.find_element(FlowPage.searchPerson).clear()
            sleep(1)
        # 确定选择的人员
        new_ticket_sta.find_element(NewTicketStandard.ensureSelect).click()
        # 保存费用标准
        new_ticket_sta.find_element(NewTicketStandard.saveTicketSta).click()
        sleep(2)
