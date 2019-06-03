# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewShipStandard(BasePage):
    def __init__(self, driver):
        self.driver = driver
    # 一等舱
    firstShip = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(1)>span:nth-child(2)")
    # 二等舱
    secondShip = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(2)>span:nth-child(2)")
    # 三等舱
    thirdShip = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(3)>span:nth-child(2)")
    # dict = {'firstShip': firstShip,
    #              'secondShip': secondShip,
    #              'thirdShip': thirdShip
    #              }
    