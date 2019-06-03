# -*- coding: utf-8 -*-


class Exist:
    def __init__(self, driver):
        self.driver = driver

    def is_element_exist(self, element):
        flag = True
        try:
            self.driver.find_element(*element)

            return flag
        except:
            flag = False
            return flag

    # def is_element_enable(self, element):
    #     state = self.driver.find_element(element).is_enabled()
    #     return state


