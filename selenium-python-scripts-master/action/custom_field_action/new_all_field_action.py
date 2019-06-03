# -*- coding: utf-8 -*-
from time import sleep
from common.common_menu_page import CommonMenus
from page.fee_type_page.new_feetype_page import NewFeeTypePage
from common.common_custom_field_page import CustomFieldPage
from selenium.webdriver.common.action_chains import ActionChains
from common.exist import Exist


class NewAllFieldAction:

    def entry_fee_type(self, driver, fee_type_name):
        common_menu = CommonMenus(driver)
        entry_fee_type = NewFeeTypePage(driver)
        # 新建费用类型
        common_menu.find_element(CommonMenus.enterpriseManagement).click()
        common_menu.find_element(CommonMenus.costType).click()
        entry_fee_type.find_element(NewFeeTypePage.addFee).click()
        entry_fee_type.find_element(NewFeeTypePage.feeTypeName).send_keys(fee_type_name)
        # 保存
        entry_fee_type.find_element(NewFeeTypePage.saveFeeType).click()
        sleep(2)

    def entry_field(self, driver):
        new_fee_type = NewFeeTypePage(driver)
        custom_field = CustomFieldPage(driver)
        # 报销字段
        new_fee_type.find_element(NewFeeTypePage.expense).click()
        ActionChains(driver).move_to_element(custom_field.find_element(CustomFieldPage.addField)).perform()
        custom_field.find_element(CustomFieldPage.addField).click()
        sleep(2)

    def new_field(self, driver):
        custom_field = CustomFieldPage(driver)
        exist = Exist(driver)
        # 使用循环，添加字段，除去枚举和自定义字段
        list_field = [CustomFieldPage.addTextType, CustomFieldPage.addNumType,
                      CustomFieldPage.moneyType, CustomFieldPage.dateType,
                      CustomFieldPage.switchType, CustomFieldPage.departmentType,
                      CustomFieldPage.staffType, CustomFieldPage.cityType]
        list_type_name = [u'说明文本1', u'数量1', u'单价1', u'出差日期1', u'是否同意1',
                          u'同行部门1', u'出差人员1', u'出差城市1']

        for i in range(len(list_field)):
            # 先进行搜索，看想添加的字段是否已存在
            custom_field.find_element(CustomFieldPage.searchField).send_keys(list_type_name[i])
            sleep(1)
            # 判断是否已存在所搜索的字段
            result = exist.is_element_exist(CustomFieldPage.no_Result)

            if result:

                custom_field.find_element(CustomFieldPage.addCustomField).click()
                sleep(2)
                # 添加各类型字段
                custom_field.find_element(list_field[i]).click()
                custom_field.find_element(CustomFieldPage.fieldName).send_keys(list_type_name[i])
                custom_field.find_element(CustomFieldPage.ensureBut).click()
                sleep(2)
            else:
                custom_field.find_element(CustomFieldPage.searchField).clear()
                sleep(1)

        sleep(2)

    def enumeration_field(self, driver):
        custom_field = CustomFieldPage(driver)
        exist = Exist(driver)

        # 添加枚举字段:航班舱型、火车席别、轮船舱型
        list_enumeration_type = [CustomFieldPage.flight, CustomFieldPage.train, CustomFieldPage.steamer]
        list_enumeration_name = [u'航班1', u'火车1', u'轮船1']
        for i in range(len(list_enumeration_type)):
            custom_field.find_element(CustomFieldPage.searchField).send_keys(list_enumeration_name[i])
            sleep(1)
            # 判断是否已存在所搜索的字段
            no_result = exist.is_element_exist(CustomFieldPage.no_Result)
            if no_result:
                custom_field.find_element(CustomFieldPage.addCustomField).click()
                sleep(2)
                custom_field.find_element(CustomFieldPage.enumerationType).click()
                custom_field.find_element(CustomFieldPage.fieldName).send_keys(list_enumeration_name[i])
                custom_field.find_element(CustomFieldPage.referEnumeration).click()
                custom_field.find_element(list_enumeration_type[i]).click()
                custom_field.find_element(CustomFieldPage.ensureBut).click()
                sleep(2)
            else:
                custom_field.find_element(CustomFieldPage.searchField).clear()
                sleep(1)

        sleep(2)

    def archives_field(self, driver):
        custom_field = CustomFieldPage(driver)
        exist = Exist(driver)

        custom_field.find_element(CustomFieldPage.searchField).send_keys(u'项目')
        sleep(1)
        # 判断是否已存在所搜索的字段
        no_result = exist.is_element_exist(CustomFieldPage.no_Result)
        if no_result:
            # 添加自定义档案字段
            custom_field.find_element(CustomFieldPage.addCustomField).click()
            custom_field.find_element(CustomFieldPage.archivesType).click()
            custom_field.find_element(CustomFieldPage.fieldName).send_keys(u'项目')
            custom_field.find_element(CustomFieldPage.referEnumeration).click()
            custom_field.find_element(CustomFieldPage.project).click()
            custom_field.find_element(CustomFieldPage.ensureBut).click()
            sleep(2)
        else:
            custom_field.find_element(CustomFieldPage.searchField).clear()
            sleep(1)

        custom_field.find_element(CustomFieldPage.cancelBut).click()
        sleep(2)



