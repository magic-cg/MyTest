# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class NewFlowPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    # 添加新审批流
    addFlow = (By.CSS_SELECTOR, ".ant-btn.btn")
    # 流程名字
    addName = (By.ID, "name")
    # 确定流程名字
    ensureBut = (By.CSS_SELECTOR, ".ant-modal-footer>div>button:nth-child(2)")
    # 编辑节点
    firstNode = (By.CLASS_NAME, "color-gray")
    # 节点名字
    firstNodeName = (By.CSS_SELECTOR, "input[placeholder='请输入节点名称,最多20个字']")
    # 节点生效条件：无条件
    firstNodeEffect = (By.CSS_SELECTOR, ".flow-form-main-detail-main>div:nth-child(2)>div:nth-child(2)>label>span>input")
    # 节点生效条件：报销/借款/申请金额大于设定值
    greaterThanSetValue = (By.CSS_SELECTOR, ".flow-form-main-detail-main>div:nth-child(2)>div:nth-child(2)>label:nth-child(2)>span:nth-child(1)>input")
    # 设定值
    settingValue = (By.CSS_SELECTOR, ".flow-form-main-detail-main>div:nth-child(2)>div:nth-child(2)>label:nth-child(2)>span:nth-child(2)>input")

    # 自动选择
    autoSelect = (By.CSS_SELECTOR, ".flow-form-main-detail-main>div:nth-child(4)>div:nth-child(2)>label:nth-child(4)>span:nth-child(1)>input")
    # 选择审批人：由提交人/选择人选择审批人，默认勾选
    # 限制可选范围
    limitRange = (By.CSS_SELECTOR, ".mt-10.mb-10>label>span>input")
    # 编辑可选范围的人
    editLimitPerson = (By.CSS_SELECTOR, ".ant-btn.btn.ant-btn-dashed.ant-btn-sm")
    # 确定选择审批的人员
    ensureSelectPerson = (By.CSS_SELECTOR, ".ant-modal-wrap.vertical-center-modal.select-member-modal>div>div>div:nth-child(4)>button:nth-child(2)")
    # 通过角色匹配人
    role = (By.CSS_SELECTOR, ".flow-form-main-detail-main>div:nth-child(4)>div:nth-child(2)>div:nth-child(3)>div:nth-child(1)>label:nth-child(3)>span:nth-child(1)>input")
    # 点击角色文本框
    clickRoleText = (By.CSS_SELECTOR, ".ant-input.ant-cascader-input")
    # 选择角色:财务主管
    selectRole = (By.CSS_SELECTOR, "li[title='财务主管']")
    # 节点配置,默认自动跳过
    # 无法提交
    # 审批人与提交人重复时，审批人自动同意
    automaticAgreeOne = (By.CSS_SELECTOR, ".flow-form-main-detail-main>div:nth-child(6)>div:nth-child(2)>div:nth-child(1)>label:nth-child(1)>span:nth-child(1)>input")
    # 审批人与前面其他节点的审批人重复时，审批人自动同意
    automaticAgreeTwo = (By.CSS_SELECTOR, ".flow-form-main-detail-main>div:nth-child(6)>div:nth-child(2)>div:nth-child(2)>label:nth-child(1)>span:nth-child(1)>input")
    # 允许提交人撤回
    revoke = (By.CSS_SELECTOR, ".flow-form-main-detail-main>div:nth-child(6)>div:nth-child(2)>label:nth-child(3)>span:nth-child(1)>input")
    # 允许审批人修改
    modify = (By.CSS_SELECTOR, ".flow-form-main-detail-main>div:nth-child(6)>div:nth-child(3)>div>label:nth-child(1)>span:nth-child(1)>input")
    # 创建
    create = (By.CSS_SELECTOR, ".layout-select-con-footer>button")
    # 保存
    save = (By.CSS_SELECTOR, ".layout-select-con-footer>button:nth-child(2)")
    # 删除
    delete = (By.CSS_SELECTOR, ".layout-select-con-footer>button:nth-child(1)")
    # 新增审批节点
    addNewNodeOne = (By.CSS_SELECTOR, ".flow-form-list-con>div:nth-child(2)>div>img")
    # 搜索
    search = (By.CSS_SELECTOR, "input[placeholder='输入名称进行搜索']")
    # 搜索结果
    searchResult = (By.CSS_SELECTOR, ".info-line>span>mark")

    # 编辑节点
    startNode = (By.CSS_SELECTOR, ".name.start-name")
    # 选择设置加急审批
    selectUrgent = (By.CSS_SELECTOR, ".m-con.flow-node-urgent___1W-vY>label>span:nth-child(1)")
    # 选择限制可使用加急审批的员工范围
    selectUrgentRole = (By.CSS_SELECTOR, ".m-con.dis-f.fd-c.ml-20>label>span")
    #选择限制的员工
    urgentRole = (By.CSS_SELECTOR, ".select_tags___b_mb4")
    #新增加急原因
    addReason = (By.CSS_SELECTOR, ".select-reason-tips>span:nth-child(2)")
    #输入加急原因’
    reason = (By.CSS_SELECTOR, ".approval-reason-list>div>p>input")
