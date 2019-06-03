# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewTicketStandard(BasePage):
    def __init__(self, driver):
        self.driver = driver
        # 新建
    new = (By.CSS_SELECTOR, ".standard-top-view>button:nth-child(3)")
    # 机票标准
    ticketSta = (By.CSS_SELECTOR, ".ant-dropdown.ant-dropdown-placement-bottomRight>ul>li:nth-child(1)")
    # 酒店标准
    hotelSta = (By.CSS_SELECTOR, ".ant-dropdown.ant-dropdown-placement-bottomRight>ul>li:nth-child(2)")
    # 火车标准
    trainSta = (By.CSS_SELECTOR, ".ant-dropdown.ant-dropdown-placement-bottomRight>ul>li:nth-child(3)")
    # 轮船标准
    steamerSta = (By.CSS_SELECTOR, ".ant-dropdown.ant-dropdown-placement-bottomRight>ul>li:nth-child(4)")
    # 补助标准
    subsidizationSta = (By.CSS_SELECTOR, ".ant-dropdown.ant-dropdown-placement-bottomRight>ul>li:nth-child(5)")
    # 标准名称
    standardName = (By.ID, "name")
    # 控制费用类型
    controlFeeType = (By.CSS_SELECTOR, ".ant-select-selection__rendered")
    # 选择费用类型
    selectFeeType = (By.CSS_SELECTOR, ".ant-select-search__field__wrap>input")
    # 确定选择的费用类型(一级)
    ensureLevelOneFeeType = (By.CSS_SELECTOR, ".ant-select-tree-title>div>span:nth-child(2)>div")
    # 确定选择的费用类型(二级)
    ensureLevelTwoFeeType = (By.CSS_SELECTOR, ".ant-select-tree-node-content-wrapper.ant-select-tree-node-content-wrapper-normal>span>div")
    # 控制单据类型
    # 点击报销单
    controlExpense = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.form-wrap>div:nth-child(3)>div:nth-child(2)>div>span>div>label:nth-child(1)>span:nth-child(1)>input")
    # 点击申请单
    controlRequisition = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal.form-wrap>div:nth-child(3)>div:nth-child(2)>div>span>div>label:nth-child(2)>span:nth-child(2)")
    # 当超标时，采用默认
    # 指定字段
    specifiedField = (By.CSS_SELECTOR, ".ant-table-thead>tr>th:nth-child(2)>span>div>span")
    # 添加字段
    addField = (By.CSS_SELECTOR, ".notice-text>div>button:nth-child(2)")
    # 默认进入报销字段，切换至申请字段
    switch = (By.CSS_SELECTOR, ".ant-tabs-nav.ant-tabs-nav-animated>div:nth-child(3)")
    # 点击指定字段：航班、日期范围、火车席别
    clickSpecified = (By.CSS_SELECTOR, ".react-grid-layout.ekb-list-layout>div:nth-child(9)>div>div>div>div")
    clickSpecifiedTwo = (By.CSS_SELECTOR, ".react-grid-layout.ekb-list-layout>div:nth-child(6)>div>div>div>div")

    # 针对轮船标准中的费用类型；差旅，定位比较特殊。
    clickSpecifiedTwo = (By.CSS_SELECTOR, ".react-grid-layout.ekb-list-layout>div:nth-child(6)>div>div>div>div")

    # 当报销字段跟申请字段都存在时，切换至申请字段时，指定字段
    clickRequSpecified = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-no-animated>div:nth-child(2)>div>div>div>div>div>div>div>div>div>div>div:nth-child(9)>div>div>div>div")
    clickRequSpecifiedTwo = (By.CSS_SELECTOR, ".ant-tabs-content.ant-tabs-content-no-animated>div:nth-child(2)>div>div>div>div>div>div>div>div>div>div>div:nth-child(6)>div>div>div>div")

    # 保存指定字段页面
    saveSpecifiedPage = (By.CSS_SELECTOR, ".modal-footer>button:nth-child(3)")
    # 选择适用人员
    selectSuitPerson = (By.CSS_SELECTOR, ".selectPerson>div")
    # 确定选用的人员
    ensureSelect = (By.CSS_SELECTOR, ".ant-modal-footer>div>button:nth-child(2)")
    # 勾选商务舱
    selectBusiness = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(2)>span:nth-child(2)")
    # 勾选头等舱
    selectFirstClass = (By.CSS_SELECTOR, ".table-enum-col-parent___LnzXA>div>label:nth-child(3)>span:nth-child(2)")
    # 保存机票标准
    saveTicketSta = (By.CSS_SELECTOR, ".bottom-view-style>button:nth-child(2)")
    # 搜索
    search = (By.CSS_SELECTOR, "input[placeholder='搜索费用标准名称']")
    # 获取费用标准的名称
    searchStandardName = (By.CSS_SELECTOR, ".standard-item-title")

