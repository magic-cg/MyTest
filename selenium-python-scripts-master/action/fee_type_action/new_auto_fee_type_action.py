# -*- coding: utf-8 -*-
from time import sleep
from common.common_menu_page import CommonMenus
from page.fee_type_page.new_feetype_page import NewFeeTypePage


class NewFeeTypeWithAuoAction:

    def new_basic_fee(self, driver, fee_type_name):
        common_menu = CommonMenus(driver)
        new_fee_type = NewFeeTypePage(driver)
        # 新建费用类型
        common_menu.find_element(CommonMenus.enterpriseManagement).click()
        common_menu.find_element(CommonMenus.costType).click()
        new_fee_type.find_element(NewFeeTypePage.addFee).click()
        new_fee_type.find_element(NewFeeTypePage.feeTypeName).send_keys(fee_type_name)
        # 保存基本设置
        new_fee_type.find_element(NewFeeTypePage.saveFeeType).click()
        sleep(2)
        new_fee_type.find_element(NewFeeTypePage.saveBasicSetting).click()
        sleep(2)

    def new_expense_fee(self, driver):
        new_fee_type = NewFeeTypePage(driver)
        # 报销字段
        new_fee_type.find_element(NewFeeTypePage.expense).click()
        # 添加单价和数量，用于自动计算
        list_add = [u'单价', u'数量']
        for i in range(len(list_add)):
            new_fee_type.find_element(NewFeeTypePage.addField).click()
            new_fee_type.find_element(NewFeeTypePage.searchField).send_keys(list_add[i])
            new_fee_type.find_element(NewFeeTypePage.ensureSearchField).click()
            new_fee_type.find_element(NewFeeTypePage.ensureBut).click()
            sleep(2)

        # 添加说明文本
        new_fee_type.find_element(NewFeeTypePage.explanatoryText).click()
        # 添加自动计算公式
        new_fee_type.find_element(NewFeeTypePage.presetMoney).click()
        new_fee_type.find_element(NewFeeTypePage.autCalculation).click()
        new_fee_type.find_element(NewFeeTypePage.clickAutCalculation).click()
        sleep(1)
        new_fee_type.find_element(NewFeeTypePage.clickNum).click()
        new_fee_type.find_element(NewFeeTypePage.xSymbol).click()
        new_fee_type.find_element(NewFeeTypePage.clickMoney).click()
        new_fee_type.find_element(NewFeeTypePage.formulaEnsure).click()
        sleep(2)
        # 保存
        new_fee_type.find_element(NewFeeTypePage.save).click()
        sleep(1)
        driver.refresh()
        sleep(2)

    def new_requisition_fee(self, driver):
        new_fee_type = NewFeeTypePage(driver)
        # 申请字段
        new_fee_type.find_element(NewFeeTypePage.requisition).click()
        # 添加单价和数量，用于自动计算
        list_add = [u'发票张数', u'单价', u'数量']
        for i in range(len(list_add)):
            new_fee_type.find_element(NewFeeTypePage.addField).click()
            new_fee_type.find_element(NewFeeTypePage.searchField).send_keys(list_add[i])
            new_fee_type.find_element(NewFeeTypePage.ensureSearchField).click()
            new_fee_type.find_element(NewFeeTypePage.ensureBut).click()
            sleep(2)

        # 添加说明文本
        new_fee_type.find_element(NewFeeTypePage.explanatoryText).click()
        # 添加自动计算公式
        new_fee_type.find_element(NewFeeTypePage.presetMoney).click()
        new_fee_type.find_element(NewFeeTypePage.autCalculation).click()
        new_fee_type.find_element(NewFeeTypePage.clickAutCalculation).click()
        sleep(1)
        new_fee_type.find_element(NewFeeTypePage.clickNum).click()
        new_fee_type.find_element(NewFeeTypePage.plusSign).click()
        new_fee_type.find_element(NewFeeTypePage.clickMoney).click()
        new_fee_type.find_element(NewFeeTypePage.formulaEnsure).click()
        sleep(6)
        # 保存
        new_fee_type.find_element(NewFeeTypePage.saveTwo).click()
        sleep(2)
        driver.refresh()
        sleep(2)

    def serch_fee_type(self, driver, fee_type):
        # 搜索费用类型
        new_fee_type = NewFeeTypePage(driver)
        new_fee_type.find_element(NewFeeTypePage.searchFeeType).send_keys(fee_type)
        new_fee_type.find_element(NewFeeTypePage.ensureSearchFeeTypeOne).click()
        sleep(1)




