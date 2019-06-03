# -*- coding: utf-8 -*-
from time import sleep
from common.common_menu_page import CommonMenus
from page.trip_type_page.new_triptype_page import NewTripTypePage


class NewTripTypeAction:

    def new_trip(self, driver, trip_type_name1, trip_type_name2, trip_type_name3):
        common_menu = CommonMenus(driver)
        new_trip = NewTripTypePage(driver)
        list_exp_add = [u'同行']
        # 进入行程类型页面
        common_menu.find_element(CommonMenus.enterpriseManagement).click()
        common_menu.find_element(CommonMenus.tripType).click()
        # 新建交通行程类型
        new_trip.find_element(NewTripTypePage.add).click()
        new_trip.find_element(NewTripTypePage.addTra).click()
        new_trip.find_element(NewTripTypePage.tripTypeName).send_keys(trip_type_name1)
        # 保存行程类型的名字
        new_trip.find_element(NewTripTypePage.saveTripType).click()
        sleep(2)

        # 新建住宿行程类型
        new_trip.find_element(NewTripTypePage.add).click()
        sleep(0.5)
        new_trip.find_element(NewTripTypePage.addHos).click()
        new_trip.find_element(NewTripTypePage.tripTypeName).send_keys(trip_type_name2)
        # 保存行程类型的名字
        new_trip.find_element(NewTripTypePage.saveTripType).click()
        sleep(1)
        # 打开基本配置
        new_trip.find_element(NewTripTypePage.fieldSetting).click()
        # 添加字段
        new_trip.find_element(NewTripTypePage.addField).click()
        new_trip.find_element(NewTripTypePage.searchField).send_keys(list_exp_add)
        new_trip.find_element(NewTripTypePage.ensureSearchField).click()
        new_trip.find_element(NewTripTypePage.ensureBut).click()
        sleep(1)
        # 添加说明文本
        new_trip.find_element(NewTripTypePage.explanatoryText).click()
        # 保存基本设置
        new_trip.find_element(NewTripTypePage.saveSetting).click()
        sleep(2)

        # 新建住宿行程类型
        new_trip.find_element(NewTripTypePage.add).click()
        sleep(0.5)
        new_trip.find_element(NewTripTypePage.addHos).click()
        new_trip.find_element(NewTripTypePage.tripTypeName).send_keys(trip_type_name3)
        # 保存行程类型的名字
        new_trip.find_element(NewTripTypePage.saveTripType).click()
        sleep(1)

        # 停用住宿行程类型
        new_trip.find_element(NewTripTypePage.searchTripType).send_keys(trip_type_name2)
        new_trip.find_element(NewTripTypePage.ensureSearchTypeTypeOne).click()
        new_trip.find_element(NewTripTypePage.disableSetting).click()
        sleep(1)
        new_trip.find_element(NewTripTypePage.ensureDisable).click()
        sleep(1)
        new_trip.find_element(NewTripTypePage.searchTripType).clear()
