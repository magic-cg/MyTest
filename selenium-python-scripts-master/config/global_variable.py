# -*- coding: utf-8 -*-

# 截图路径
filename = '/Users/wei/Downloads/hhh.png'

# ----------节点名称--------
nodename = [u'节点一', u'节点二', u'节点三']

# ---------审批流------------
# 审批流名称
flow_name1 = u'简单流1'

# 审批流可见范围
list_name = [u'曹玉静', u'孙静']
# --------单据模板----------
# 报销单模板名称
exp_model_name1 = u'曹玉静的报销单模板八'
# 借款单模板名称
loan_model_name1 = u'曹玉静的借款单模板八'
# 申请单模板名称
requisition_model_name1 = u'曹玉静的申请单模板八'
requisition_model_name2 = u'曹玉静的申请单模板九'
requisition_model_name3 = u'报销金额≥申请金额时自动关闭'
requisition_model_name4 = u'达到报销次数自动关闭'

# 差旅申请单模板名称
trip_requisition_model_name1 = u'王沁怡的差旅申请单模板啦'


# --------新建单据----------
# 报销单标题
exp_title = u'外出报销'
# 费用金额
expense_amount = u'30.00'
# 带核销的报销单的费用金额
expense_amount1 = 3
# 借款单标题
loan_title = u'外出借款'
# 借款金额
loan_amount = 40
# 申请单标题
requisition_title = u'出差申请'
# 申请金额
requisition_amount = 100
# 出发地
requisition_tripFromCity = u'南京市'
# 目的地
requisition_tripToCity = u'北京市'
# 报销单中带有核销
expense_title = u'我的核销报销单'
# 审批人

approver = u'曹玉静'

# 出纳
teller = u'静静'
# 同意--审批意见
approve_remark = u'同意啦'
# 驳回--驳回意见
refused_remark = u'重新填写'
# 修改审批流程中的审批人
modify_approver = u'曹玉静'
# --------费用类型-----------
# 创建普通费用类型
fee_type_name = [u'暖壶1', u'钢笔1', u'水杯1']
# 创建带有自动计算的费用类型

fee_type_name1 = u'冰柜46'

# 带有费用分摊的费用类型
fee_type_name2 = u''
# 费用分摊时搜索的部门
dep = [u'市场部', u'综合部']
# 分摊比例
scale = [u'30', u'70']
project = [u'天津项目1', u'广东项目1']
# 带有费用标准的费用类型
fee_type_name3 = [u'小小飞机5', u'小小住宿5', u'小小火车5', u'小小差旅5', u'小小巴士5']

# 创建自定义字段时创建的费用类型

fee_type_name4 = u'诗品12'

# ---------项目名称--------
project_name = [u'广东项目29', u'广西项目27', u'台湾项目16', u'山西项目16']
project_name3 = [u'广州项目24']
# 项目可见范围
list_select_person = [u'曹玉静']

# --------行程类型-----------
# 创建行程类型
trip_type_name = [u'wqy交通行程类型8', u'wqy住宿行程类型11', u'wqy住宿行程类型12']

# ------------费用标准------------
ticket_sta_name = u'曹玉静的机票费用标准1'
hotel_sta_name = u'曹玉静的酒店费用标准1'
train_sta_name = u'曹玉静的火车费用标准1'
ship_sta_name = u'曹玉静的轮船费用标准1'
subsidy_sta_name = u'曹玉静的补助费用标准1'


# 酒店金额标准
hotel_money = [u'100', u'200']
# 补助金额标准
subsidy_money = [u'100', u'200']

# ---------新建角色------------
# 角色组：管理岗
role_group_name1 = u'管理岗位岗位'
# 角色：测试经理
role_name1 = u'测试测试'

# -------设置管理权限--------
list_person = [u'曹玉静', u'孙静']

# ---------支付账户--------------
pay_code = [u'161', u'140', u'117']
pay_name = [u'线下支付', u'在线支付账户', u'ERP付款账户']
account_name = [u'王沁怡', u'王沁怡']
bank_card_no = [u'123456424458', u'45675890284']

# ----------收款信息------------
collect_name = u'王沁怡'
collect_no = 4567589028
