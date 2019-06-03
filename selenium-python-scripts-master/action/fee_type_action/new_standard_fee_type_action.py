# -*- coding: utf-8 -*-
from time import sleep
from common.common_menu_page import CommonMenus
from page.fee_type_page.new_feetype_page import NewFeeTypePage
import config.global_variable as gv


class NewStandardFeeTypeAction:

    def new_flight_fee(self, driver):
        common_menu = CommonMenus(driver)
        new_fee_type = NewFeeTypePage(driver)
        common_menu.find_element(CommonMenus.enterpriseManagement).click()
        common_menu.find_element(CommonMenus.costType).click()
        sleep(2)
        # 创建费用标准中的费用类型，包括飞机、住宿、火车、差旅、巴士。
        list_add_element = [u'航班', u'起止日期', u'火车', u'轮船', u'起止日期']
        for i in range(len(list_add_element)):
            fee = gv.fee_type_name3[i]
            # 首先清空搜索框的值
            new_fee_type.find_element(NewFeeTypePage.searchFeeType).clear()
            new_fee_type.find_element(NewFeeTypePage.searchFeeType).send_keys(fee)
            sleep(2)

            new_fee_type.find_element(NewFeeTypePage.ensureSearchFeeTypeTwo).click()
            if fee == gv.fee_type_name3[0] or fee == gv.fee_type_name3[1]:
                # 报销字段页面增加字段
                new_fee_type.find_element(NewFeeTypePage.requisition).click()
                new_fee_type.find_element(NewFeeTypePage.expense).click()
                new_fee_type.find_element(NewFeeTypePage.addField).click()
                new_fee_type.find_element(NewFeeTypePage.searchField).send_keys(list_add_element[i])
                new_fee_type.find_element(NewFeeTypePage.ensureSearchField).click()
                new_fee_type.find_element(NewFeeTypePage.ensureBut).click()
                sleep(1)
                # 保存费用类型
                new_fee_type.find_element(NewFeeTypePage.save).click()
                sleep(2)
            elif fee == gv.fee_type_name3[2] or fee == gv.fee_type_name3[3]:
                # 申请字段页面增加字段
                new_fee_type.find_element(NewFeeTypePage.expense).click()
                new_fee_type.find_element(NewFeeTypePage.requisition).click()
                new_fee_type.find_element(NewFeeTypePage.addFieldTwo).click()
                new_fee_type.find_element(NewFeeTypePage.searchField).send_keys(list_add_element[i])
                new_fee_type.find_element(NewFeeTypePage.ensureSearchField).click()
                new_fee_type.find_element(NewFeeTypePage.ensureBut).click()
                sleep(1)
                # 保存费用类型
                new_fee_type.find_element(NewFeeTypePage.saveTwo).click()
                sleep(2)

            else:
                # 报销字段页面增加字段
                new_fee_type.find_element(NewFeeTypePage.requisition).click()
                new_fee_type.find_element(NewFeeTypePage.expense).click()
                new_fee_type.find_element(NewFeeTypePage.addField).click()
                new_fee_type.find_element(NewFeeTypePage.searchField).send_keys(list_add_element[i])
                new_fee_type.find_element(NewFeeTypePage.ensureSearchField).click()
                new_fee_type.find_element(NewFeeTypePage.ensureBut).click()
                sleep(1)
                # 保存费用类型
                new_fee_type.find_element(NewFeeTypePage.save).click()
                sleep(2)
                # 申请字段页面增加字段
                new_fee_type.find_element(NewFeeTypePage.expense).click()
                new_fee_type.find_element(NewFeeTypePage.requisition).click()
                new_fee_type.find_element(NewFeeTypePage.addFieldTwo).click()
                new_fee_type.find_element(NewFeeTypePage.searchField).send_keys(list_add_element[i])
                new_fee_type.find_element(NewFeeTypePage.ensureSearchField).click()
                new_fee_type.find_element(NewFeeTypePage.ensureBut).click()
                sleep(1)
                # 保存费用类型
                new_fee_type.find_element(NewFeeTypePage.saveTwo).click()
                sleep(2)







