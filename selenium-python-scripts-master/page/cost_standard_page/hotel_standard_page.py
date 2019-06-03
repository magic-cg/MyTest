# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewHotelStandard(BasePage):
    def __init__(self, driver):
        self.driver = driver
    # 酒店金额标准
    hotelMoneySta = (By.CSS_SELECTOR, ".number_wrap>div>div:nth-child(2)>input")
    # dict = {'hotelMoneySta': hotelMoneySta,
    #              }
