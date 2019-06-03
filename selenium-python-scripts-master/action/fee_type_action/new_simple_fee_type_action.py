# -*- coding: utf-8 -*-
from time import sleep
from common.common_menu_page import CommonMenus
from page.fee_type_page.new_feetype_page import NewFeeTypePage
import config.global_variable as gv


class NewFeeTypeSimpleAction:

    def new_basic_fee(self, driver, fee_type_name):
        common_menu = CommonMenus(driver)
        new_fee_type = NewFeeTypePage(driver)
        # 新建费用类型
        common_menu.find_element(CommonMenus.enterpriseManagement).click()
        common_menu.find_element(CommonMenus.costType).click()
        sleep(2)
        for i in range(len(fee_type_name)):

            new_fee_type.find_element(NewFeeTypePage.addFee).click()
            new_fee_type.find_element(NewFeeTypePage.feeTypeName).send_keys(fee_type_name[i])
            sleep(1)
            new_fee_type.find_element(NewFeeTypePage.saveFeeType).click()
            sleep(1)
            new_fee_type.find_element(NewFeeTypePage.saveBasicSetting).click()
            # 保存基本设置
            sleep(2)
            driver.refresh()
            sleep(2)







