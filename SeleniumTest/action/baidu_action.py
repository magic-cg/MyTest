# -*- coding: utf-8 -*-
from page.baidu_page import BaiduPage

class NewBaiDu:

    def baidu_search1(self,driver):
        driver = BaiduPage(driver)
        driver.find_element(BaiduPage.kw).send_keys("111")
        driver.find_element(BaiduPage.su).click()
        print("成功")


    def baidu_search2(self, driver):
        driver = BaiduPage(driver)
        driver.find_element(BaiduPage.kw).clear()
        driver.find_element(BaiduPage.kw).send_keys("python")
        driver.find_element(BaiduPage.su).click()
        print("成功")

    # def baidu_search3(self, driver,name):
    #     driver = BaiduPage(driver)
    #     driver.find_element(BaiduPage.kw).send_keys(name)
    #     driver.find_element(BaiduPage.su).click()
    #     print("成功")