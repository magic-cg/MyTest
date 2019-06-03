# -*- coding: utf-8 -*-
from time import sleep
from page.requisition_page.create_requisition_page import CreateRequisitionPage
from common.common_flow_page import FlowPage
import config.global_variable as gv
from selenium.webdriver.common.keys import Keys
from common.exist import Exist


class NewTripRequisitionAction:

    def add_trip(self, driver):

        create_requisition = CreateRequisitionPage(driver)
        # 添加行程
        create_requisition.find_element(CreateRequisitionPage.addTrip).click()

    def new_requisition(self, driver, trip_requisition_title):

        create_requisition = CreateRequisitionPage(driver)
        create_requisition.find_element(CreateRequisitionPage.newRequisition).click()
        # 选择申请单模板
        create_requisition.find_element(CreateRequisitionPage.selectModel).click()
        sleep(2)
        selectModel = driver.find_element_by_css_selector("ul[role = 'menu']")
        allOption = selectModel.find_elements_by_tag_name("li")
        for option in allOption:
            if gv.trip_requisition_model_name1 in option.text:
                option.click()
                break
        # 填写申请单标题
        create_requisition.find_element(CreateRequisitionPage.requisitionTitle).send_keys(trip_requisition_title)
        # 输入申请单金额
        create_requisition.find_element(CreateRequisitionPage.requisitionMoney).send_keys(input_requisition_amount)

    def traffic_trip(self, driver, requisition_tripFromCity, requisition_tripToCity):
        create_requisition = CreateRequisitionPage(driver)

        # 选择出行方式
        create_requisition.find_element(CreateRequisitionPage.tripType).click()
        create_requisition.find_element(CreateRequisitionPage.selecttripType).send_keys(gv.trip_type_name[0])
        sleep(1)
        # 回车
        create_requisition.find_element(CreateRequisitionPage.selecttripType).send_keys(Keys.ENTER)
        sleep(1)
        # 选择出发地
        create_requisition.find_element(CreateRequisitionPage.tripFromCity).click()
        create_requisition.find_element(CreateRequisitionPage.selecttripFrom).send_keys(requisition_tripFromCity)
        sleep(2)
        # 回车
        create_requisition.find_element(CreateRequisitionPage.selecttripFrom).send_keys(Keys.ENTER)
        # 选择目的地
        create_requisition.find_element(CreateRequisitionPage.tripToCity).click()
        create_requisition.find_element(CreateRequisitionPage.selecttripTo).send_keys(requisition_tripToCity)
        sleep(2)
        # 回车
        create_requisition.find_element(CreateRequisitionPage.selecttripTo).send_keys(Keys.ENTER)

    def trip_again(self, driver):
        create_requisition = CreateRequisitionPage(driver)

        # 添加第2程
        create_requisition.find_element(CreateRequisitionPage.addTripAgain).click()

    def accommodation_trip(self, driver, requisition_tripToCity):
        create_requisition = CreateRequisitionPage(driver)
        # 选择出行方式
        create_requisition.find_element(CreateRequisitionPage.tripType2).click()
        create_requisition.find_element(CreateRequisitionPage.selecttripType2).send_keys(gv.trip_type_name[1])
        sleep(2)
        # 回车
        create_requisition.find_element(CreateRequisitionPage.selecttripType2).send_keys(Keys.ENTER)
        # 选择住宿时间
        create_requisition.find_element(CreateRequisitionPage.tripDatePeriod).click()
        create_requisition.find_element(CreateRequisitionPage.selecttripStartDate).clear()
        create_requisition.find_element(CreateRequisitionPage.selecttripStartDate).send_keys("2018-04-01")
        sleep(1)
        create_requisition.find_element(CreateRequisitionPage.tripDatePeriod).click()
        create_requisition.find_element(CreateRequisitionPage.selecttripEndDate).clear()
        create_requisition.find_element(CreateRequisitionPage.selecttripEndDate).send_keys("2018-04-03")
        sleep(1)

        # 选择住宿地
        create_requisition.find_element(CreateRequisitionPage.tripCity).click()
        create_requisition.find_element(CreateRequisitionPage.selecttripCity).send_keys(requisition_tripToCity)
        sleep(2)
        # 回车
        create_requisition.find_element(CreateRequisitionPage.selecttripCity).send_keys(Keys.ENTER)

    def save(self, driver):
        create_requisition = CreateRequisitionPage(driver)
        # 保存行程
        create_requisition.find_element(CreateRequisitionPage.saveTrip).click()
        sleep(1)

    # 提交申请单成功后，弹出关注易快报微信服务号
    def remind(self, driver):
        create_requisition = CreateRequisitionPage(driver)
        exist = Exist(driver)
        remind_text = exist.is_element_exist(CreateRequisitionPage.noRemindText)
        # 根据是否弹出提示框来判断要不要进行下列操作
        if remind_text:
            create_requisition.find_element(CreateRequisitionPage.noRemind).click()
            sleep(1)
            # 确定
            create_requisition.find_element(CreateRequisitionPage.remindEnsure).click()
            sleep(0.5)
        else:
            pass







