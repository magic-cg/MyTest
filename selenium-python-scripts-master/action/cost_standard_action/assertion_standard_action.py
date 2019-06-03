# -*- coding: utf-8 -*-


from page.cost_standard_page.ticket_standard_page import NewTicketStandard
from selenium.webdriver.common.keys import Keys
from time import sleep


class GetStandard:

    def get_standard_name(self, driver, formwork_name):
        new_standard = NewTicketStandard(driver)
        # 输入标准名称
        new_standard.find_element(NewTicketStandard.search).send_keys(formwork_name)
        # 回车
        new_standard.find_element(NewTicketStandard.search).send_keys(Keys.ENTER)
        sleep(1)
        # 获取搜索到标准的名称
        standard_name_text = new_standard.find_element(NewTicketStandard.searchStandardName).text
        sleep(1)
        return standard_name_text