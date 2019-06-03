# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class CreateRequisitionPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # 新建申请
    newRequisition = (By.CLASS_NAME, "requisition-hover")
    # 选择申请单模板
    selectModel = (By.CSS_SELECTOR, "div[style = 'display: block; opacity: 1;")
    # 申请单的标题
    requisitionTitle = (By.CSS_SELECTOR, "input[placeholder='请输入标题']")
    # 添加费用明细
    costDetail = (By.CLASS_NAME, "import-detail")
    # 费用类型
    feeType = (By.CSS_SELECTOR, ".feeType_select_wrap___7deVR>span>span>span:nth-child(1)>span>div>span:nth-child(2)>div")
    # 搜索费用类型
    selectFeeType = (By.CSS_SELECTOR, ".ant-select-search__field__wrap>input:nth-child(1)")
    # 确定选择的费用类型
    ensureFeeType = (By.CSS_SELECTOR, ".ant-select-tree-title>div>span:nth-child(2)>div")
    # 申请金额
    requisitionMoney = (By.CSS_SELECTOR, "input[placeholder='请输入金额']")
    # 再记一笔
    writeAgain = (By.CSS_SELECTOR, ".ant-modal-body>div>div:nth-child(3)>button:nth-child(2)")
    # 保存
    saveCostDetailBut = (By.CSS_SELECTOR, ".ant-modal-body>div>div:nth-child(3)>button:nth-child(3)")
    # 直接填写费用金额
    costDirectly = (By.CSS_SELECTOR, ".currency-money___1d6YR>div>input:nth-child(2)")
    # 添加差旅行程
    addTrip = (By.CLASS_NAME, "add-button")
    # 出行方式
    tripType = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(1)>section>div:nth-child(1)>div:nth-child(2)")
    # 搜索出行方式
    selecttripType = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(1)>section>div:nth-child(1)>div:nth-child(2)>div>div>div>div:nth-child(2)>div>input")
    # 确定出行方式
    ensuretripType = (By.CSS_SELECTOR, ".edit-trip___5iC5U")
    # 出发日期
    tripDate = (By.CSS_SELECTOR,".edit-trip___5iC5U>div:nth-child(1)>section>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div")
    # 输入出发日期
    selecttripDate = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(1)>section>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>span>div>input")
    # 出发地
    tripFromCity = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(1)>section>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>span>div")
    # 搜索出发地
    selecttripFrom = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(1)>section>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>span>div>div>div>div>div>div>input")
    # 确定选择的出发地
    ensuretrip = (By.CSS_SELECTOR, ".edit-trip___5iC5U")

    # 目的地
    tripToCity = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(1)>section>div:nth-child(2)>div:nth-child(3)>div:nth-child(2)>div>span>div")
    # 搜索目的地
    selecttripTo = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(1)>section>div:nth-child(2)>div:nth-child(3)>div:nth-child(2)>div>span>div>div>div>div>div>div>input")

    # 添加行程
    addTripAgain = (By.CSS_SELECTOR, ".edit-trip___5iC5U>button")

    # 出行方式
    tripType2 = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(2)>section>div:nth-child(1)>div:nth-child(2)")
    # 搜索出行方式
    selecttripType2 = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(2)>section>div:nth-child(1)>div:nth-child(2)>div>div>div>div:nth-child(2)>div>input")

    # 住宿时间
    tripDatePeriod = (By.CSS_SELECTOR,".edit-trip___5iC5U>div:nth-child(2)>section>div:nth-child(2)>div:nth-child(1)>div>div>span>div")
    # 住宿开始时间
    selecttripStartDate = (By.CSS_SELECTOR, ".ant-calendar-date-panel>div:nth-child(1)>div:nth-child(1)>div>input")
    # 住宿结束时间
    selecttripEndDate = (By.CSS_SELECTOR, ".ant-calendar-date-panel>div:nth-child(3)>div:nth-child(1)>div>input")

    # 住宿地
    tripCity = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(2)>section>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>span>div")
    # 搜索住宿地
    selecttripCity = (By.CSS_SELECTOR, ".edit-trip___5iC5U>div:nth-child(2)>section>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>span>div>div>div>div>div>div>input")

    #  同行人员部门
    # 保存
    saveTrip = (By.CSS_SELECTOR, ".modal-footer>button:nth-child(2)")

    # 提交送审
    submitRequisition = (By.CSS_SELECTOR, ".button_group_wrapper___3M-uZ>button:nth-child(3)")
    # 提醒文案
    noRemindText = (By.CSS_SELECTOR, ".followWeChat-modal-wrapper___18El8>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>p:nth-child(1)")
    # 不再提醒
    noRemind = (By.CSS_SELECTOR, ".followWeChat-modal-wrapper___18El8>div:nth-child(1)>div:nth-child(2)>label:nth-child(2)>span:nth-child(1)>input:nth-child(1)")
    # 确定
    remindEnsure = (By.CSS_SELECTOR, ".followWeChat-footer>button:nth-child(2)")



