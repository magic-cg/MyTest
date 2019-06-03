# -*- coding: utf-8 -*-


from page.trip_type_page.new_triptype_page import NewTripTypePage
from selenium.webdriver.common.keys import Keys
from time import sleep


class GetTripType:

    def get_trip_type_name(self, driver, trip_type_name):
        new_trip_type= NewTripTypePage(driver)
        # 清空搜索框内容
        new_trip_type.find_element(NewTripTypePage.searchTripType).clear()

        # 输入模板名称
        new_trip_type.find_element(NewTripTypePage.searchTripType).send_keys(trip_type_name)
        # 回车
        new_trip_type.find_element(NewTripTypePage.searchTripType).send_keys(Keys.ENTER)
        sleep(1)
        # 获取搜索到模板名称
        trip_trip_name_text = new_trip_type.find_element(NewTripTypePage.getTripType).text
        sleep(1)
        return trip_trip_name_text
