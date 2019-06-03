# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from common.basepage import BasePage


class FlowPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    # 搜索单据单号
    searchTitle = (By.CSS_SELECTOR, "input[placeholder='搜索标题、单号或提交人']")
    # 由于页面原因，导致同意按钮遮盖，故先定位到同意按钮
    moveToAgree = (By.CSS_SELECTOR, ".ant-table-tbody>tr>td:nth-child(8)>div>a:nth-child(1)")
    # 同意按钮
    agreeBut = (By.LINK_TEXT, "同意")
    # 驳回
    moveToReject = (By.CSS_SELECTOR, ".ant-table-tbody>tr>td:nth-child(8)>div>a:nth-child(2)")
    # 驳回按钮
    rejectBut = (By.LINK_TEXT, "驳回")
    # 驳回原因
    rejectReason = (By.ID, "comment")
    # 确认驳回
    confirmReject = (By.CSS_SELECTOR, ".flow-allow-modal-footer>button:nth-child(2)")
    # 打印提醒
    printReminder = (By.CSS_SELECTOR, ".ant-table-tbody>tr>td:nth-child(8)>div>a:nth-child(2)")
    # 评论
    review = (By.CSS_SELECTOR, ".button_group_wrapper___3M-uZ>button:nth-child(2)")
    # 撤回
    revocation = (By.CSS_SELECTOR, "")
    # 修改
    modify = (By.CSS_SELECTOR, ".button_group_wrapper___3M-uZ>button:nth-child(4)")

    # 选择第一级审批人
    selectFirstPerson = (By.CSS_SELECTOR, ".flow-config-modal___1xGaj>div:nth-child(2)>form>div>div:nth-child(1)>div:nth-child(2)>div>span>div>input[placeholder='选择审批人']")
    # 确定第一级审批人
    selectFirstPersonBut = (By.CSS_SELECTOR, ".modal-footer>button:nth-child(2)")
    # 选择二级以后审批人或出纳
    selectPerson = (By.CSS_SELECTOR, ".select-approve>div:nth-child(2)>div>div>span>div>input")
    # 搜索审批人或出纳
    searchPerson = (By.CSS_SELECTOR, "input[placeholder='搜索员工']")
    # 勾选审批人或出纳
    getPerson = (By.CLASS_NAME, "ant-radio-input")
    # 确定审批人或出纳
    makeSureBut = (By.CSS_SELECTOR, ".ant-modal-footer>div>button:nth-child(2)")
    # 添加备注
    remark = (By.ID, "comment")
    # 审批人送审给下一个节点
    sendToNext = (By.CSS_SELECTOR, ".modal-footer-button>button:nth-child(2)")
    # 找到支付按钮
    moveToPaid = (By.CSS_SELECTOR, ".ant-table-tbody>tr>td:nth-child(8)>div>a:nth-child(1)")
    # 支付按钮
    paid = (By.LINK_TEXT, "支付")
    # 支付为0时确认按钮
    paidZero = (By.CSS_SELECTOR, ".info-modal>div:nth-child(2)>button:nth-child(2)")
    # 选择线下支付
    offlinePay = (By.CLASS_NAME, "ant-select-selection__placeholder")
    # 选择默认银行账户
    bankAccount = (By.CSS_SELECTOR, "div[style='overflow: auto;']>ul>li:nth-child(1)")
    # 确认选择默认银行账户.因为此处有了影像签名，所以确定按钮的位置有变化
    bankAccountBut = (By.CSS_SELECTOR, ".flow-allow-modal-footer>button:nth-child(3)")
    # 当没有影像签名时
    bankAccountButTwo = (By.CSS_SELECTOR, ".flow-allow-modal-footer>button:nth-child(2)")

    # 影像签名
    sign = (By.CSS_SELECTOR, ".signature-container>div:nth-child(1)")
    # 影像签名的开关关闭
    signSwitch = (By.CSS_SELECTOR, ".signature-container>span:nth-child(2)")
    # 关闭，进入支付中
    # 确认支付、确认撤回等
    confirmBut = (By.CSS_SELECTOR, ".ant-confirm-btns>button:nth-child(2)")
    # 申请单最后一个审批节点的确定按钮
    requisitionLastBut = (By.CSS_SELECTOR, ".modal-footer-button>button:nth-child(2)")
    # 多选框选人
    multipleChoice = (By.CSS_SELECTOR, ".list-view>div>div>label>span>input")
    # 多选框中的确定按钮
    # 因审批流选人组件中，此元素存在较多个
    ensureSelectPerson = (By.CSS_SELECTOR, ".ant-modal-wrap.vertical-center-modal.select-member-modal>div>div>div:nth-child(4)>div>button:nth-child(2)")
    # 权限选人组件中，此元素页面唯一
    ensureSelectPersonTwo = (By.CSS_SELECTOR, ".ant-modal-footer>div>button:nth-child(2)")
    # 首页搜索按钮
    searchBut = (By.CSS_SELECTOR, ".anticon.anticon-search")
    # 输入搜索内容
    numSearch = (By.CSS_SELECTOR, ".ant-input-search.ant-input-affix-wrapper>input")
    # 点击搜索出的单据
    clickReceipt = (By.CSS_SELECTOR, ".title-part")
    # 获取当前单据的单号
    num = (By.CSS_SELECTOR, ".bill_id___2og4I")
    # 获取当前单据的支付金额
    paidMoney = (By.CSS_SELECTOR, ".amount-wrapper>div:nth-child(3)>span:nth-child(2)>div>span:nth-child(2)")
    # 评论内容
    commentTextClick = (By.CSS_SELECTOR, ".ant-mention-editor-wrapper")
    commentText = (By.CSS_SELECTOR, ".notranslate.public-DraftEditor-content")
    # 评论确认按钮
    commentConfirmBut = (By.CSS_SELECTOR, ".modal-footer-button>button:nth-child(2)")
    # 待办中搜索单据后，点击打开详情
    receiptDetail = (By.CSS_SELECTOR, ".ant-table-row.table-line-tr.ant-table-row-level-0>td:nth-child(2)")
    # 修改后保存
    modifySave = (By.CSS_SELECTOR, ".button_group_wrapper___3M-uZ>button:nth-child(2)")
    # 修改原因
    modifyReason = (By.ID, "editReason")
    # 修改原因确定按钮
    modifyReasonBut = (By.CSS_SELECTOR, ".flow-allow-modal-footer>button:nth-child(1)")
    # 批量同意
    batchAgree = (By.NAME, "agree")
    # 批量驳回
    batchReject = (By.NAME, "reject")
    # 批量支付
    batchPaid = (By.NAME, "pay")
    # 全选按钮
    checkAll = (By.CSS_SELECTOR, ".ant-table-thead>tr>th:nth-child(1)>span>div>label>span>input")
    # 获取审批成功或失败的吐丝
    message = (By.CSS_SELECTOR, ".ant-message>span>div>div>div>span")
    # 同意原因
    agreeReason = (By.ID, "comment")
    # 批量同意后确定按钮
    batchEnsureBut = (By.CSS_SELECTOR, ".flow-allow-modal-footer>button:nth-child(2)")
    # 在单据详情中点击审批流程
    approvalProcess = (By.CSS_SELECTOR, ".dis-f.flex-1.ovr-y-h>div>div:nth-child(1)>div>div:nth-child(3)>div>div>div:nth-child(3)")
    # 在流程实例图中修改第二个节点的审批人
    modifyApprovalTwo = (By.CSS_SELECTOR, ".flow-config-con>div:nth-child(2)>a:nth-child(3)")
    # 在流程实例图中修改第二个节点的审批人
    modifyApprovalThree = (By.CSS_SELECTOR, ".flow-config-con>div:nth-child(3)>a:nth-child(3)")
    # 批量转交审批
    batchApproveTransfer = (By.NAME, "approve_transfer")
    # 选择转交人
    selectTransfer = (By.CSS_SELECTOR, ".modal-content>div:nth-child(3)>input[placeholder='请选择审批人（单选）']")
    # 选择转交理由-转交
    selectTransferReason1 = (By.CSS_SELECTOR, ".ant-radio-group.radio-group>label:nth-child(1)")
    # 选择转交理由-前加签
    selectTransferReason2 = (By.CSS_SELECTOR, ".ant-radio-group.radio-group>label:nth-child(2)")
    # 选择转交理由-后加签
    selectTransferReason3 = (By.CSS_SELECTOR, ".ant-radio-group.radio-group>label:nth-child(3)")
    getPerson1 = (By.CSS_SELECTOR, ".list-view>div>div>label>span")

    # 转交审批-确认
    transferConfirmBut = (By.CSS_SELECTOR, ".content>button")

    #加急开关
    urgentSwitch = (By.CSS_SELECTOR, ".switch>span:nth-child(2)")
    #加急原因
    urgentReason = (By.CSS_SELECTOR, ".ant-modal-wrap.vertical-center-modal>div>div>div:nth-child(2)>div>div:nth-child(2)>form>div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>div>span>div:nth-child(2)>div>div>div>span>input")



