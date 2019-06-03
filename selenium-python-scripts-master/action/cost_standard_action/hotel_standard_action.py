# -*- coding: utf-8 -*-

from page.cost_standard_page.hotel_standard_page import NewHotelStandard
from page.cost_standard_page.ticket_standard_page import NewTicketStandard
from common.common_menu_page import CommonMenus
import config.global_variable as gv
from common.common_flow_page import FlowPage
from time import sleep


class NewHotelStandardAction:

    def new_hotel_standard(self, driver):
        new_ticket_sta = NewTicketStandard(driver)
        common_menu = CommonMenus(driver)

        # 进入费用标准页面
        common_menu.find_element(CommonMenus.enterpriseManagement).click()
        common_menu.find_element(CommonMenus.chargeStandard).click()
        # 新建酒店标准
        new_ticket_sta.find_element(NewTicketStandard.new).click()
        new_ticket_sta.find_element(NewTicketStandard.hotelSta).click()

    def basic_setting(self, driver, cost_sta_name, fee_type):
        # 酒店标准的基本设置
        new_ticket_sta = NewTicketStandard(driver)

        # 标准名称
        new_ticket_sta.find_element(NewTicketStandard.standardName).clear()
        new_ticket_sta.find_element(NewTicketStandard.standardName).send_keys(cost_sta_name)
        # 单据控制费用类型
        new_ticket_sta.find_element(NewTicketStandard.controlFeeType).click()
        new_ticket_sta.find_element(NewTicketStandard.selectFeeType).send_keys(fee_type)
        sleep(2)
        new_ticket_sta.find_element(NewTicketStandard.ensureLevelOneFeeType).click()
        # 控制单据类型不包括申请单
        new_ticket_sta.find_element(NewTicketStandard.controlRequisition).click()
        # 费用超标时默认允许提交

    def standard_setting(self, driver, hotel_money):
        new_ticket_sta = NewTicketStandard(driver)
        new_hotel_sta = NewHotelStandard(driver)
        flow = FlowPage(driver)

        # 点击指定字段
        new_ticket_sta.find_element(NewTicketStandard.specifiedField).click()
        # 点击指定的日期范围
        new_ticket_sta.find_element(NewTicketStandard.clickSpecified).click()
        sleep(2)
        # 保存
        new_ticket_sta.find_element(NewTicketStandard.saveSpecifiedPage).click()
        # 填写酒店金额标准
        new_hotel_sta.find_element(NewHotelStandard.hotelMoneySta).clear()
        sleep(1)
        new_hotel_sta.find_element(NewHotelStandard.hotelMoneySta).send_keys(hotel_money)
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
