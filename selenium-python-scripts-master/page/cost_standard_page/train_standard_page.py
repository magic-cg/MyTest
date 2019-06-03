# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewTrainStandard(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 软座
    softSeat = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(2)>span:nth-child(2)")
    # 硬卧
    hardSeat = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(3)>span:nth-child(2)")
    # 软卧
    softSleeper = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(4)>span:nth-child(2)")
    # 高级软卧
    seniorSoftSleeper = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(5)>span:nth-child(2)")
    # 一等座
    firstClass = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(6)>span:nth-child(2)")
    # 二等座
    secondClass = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(7)>span:nth-child(2)")
    # 商务座
    business = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(8)>span:nth-child(2)")
    # 高铁动卧
    highSpeedRail = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(9)>span:nth-child(2)")
    # dict = {'softSeat': softSeat,
    #              'hardSeat': hardSeat,
    #              'softSleeper': softSleeper,
    #              'seniorSoftSleeper': seniorSoftSleeper,
    #              'firstClass': firstClass,
    #              'secondClass': secondClass,
    #              'business': business,
    #              'highSpeedRail': highSpeedRail
    #              }
