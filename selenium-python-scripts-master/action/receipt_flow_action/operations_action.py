# -*- coding: utf-8 -*-
from common.common_flow_page import FlowPage
from common.common_menu_page import CommonMenus
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from action.attachment_action import AttachmentFile
from page.loan_page.create_loan_page import CreateLoanPage
from page.expense_page.create_expense_page import NewExpensePage
from common.exist import Exist
import config.global_variable as gv
from time import sleep


class OperationButAction:

    # 待审批
    def pending(self, driver):

        common_menus = CommonMenus(driver)
        # 由首页进入待审批页面
        common_menus.find_element(CommonMenus.toDo).click()
        common_menus.find_element(CommonMenus.pending).click()

    # 待支付
    def tobepaid(self, driver):

        common_menus = CommonMenus(driver)
        # 由首页进入待支付页面
        common_menus.find_element(CommonMenus.toDo).click()
        common_menus.find_element(CommonMenus.toBePaid).click()
        sleep(1)

    # 审批人同意
    def agree(self, driver, num):
        flow = FlowPage(driver)
        common_menus = CommonMenus(driver)
        # 由首页进入待审批页面
        common_menus.find_element(CommonMenus.toDo).click()
        common_menus.find_element(CommonMenus.pending).click()
        sleep(1)
        flow.find_element(FlowPage.searchTitle).send_keys(num)
        flow.find_element(FlowPage.searchTitle).send_keys(Keys.ENTER)
        sleep(5)
        ActionChains(driver).move_to_element(flow.find_element(FlowPage.moveToAgree)).perform()
        sleep(1)
        flow.find_element(FlowPage.agreeBut).click()
        sleep(2)

    # 申请单最后一个审批人审批同意
    def requi_last_agree(self, driver, num, comment):
        flow = FlowPage(driver)
        common_menus = CommonMenus(driver)
        # 由首页进入待审批页面
        driver.refresh()
        sleep(2)
        common_menus.find_element(CommonMenus.toDo).click()
        common_menus.find_element(CommonMenus.pending).click()
        flow.find_element(FlowPage.searchTitle).send_keys(num )
        flow.find_element(FlowPage.searchTitle).send_keys(Keys.ENTER)
        sleep(2)
        ActionChains(driver).move_to_element(flow.find_element(FlowPage.moveToAgree)).perform()
        sleep(1)
        flow.find_element(FlowPage.agreeBut).click()
        # 无须支付，审批即完成
        flow.find_element(FlowPage.remark).send_keys(comment)
        flow.find_element(FlowPage.requisitionLastBut).click()
        sleep(2)

    # 审批人驳回
    def reject(self, driver, num):
        flow = FlowPage(driver)
        common_menus = CommonMenus(driver)
        atta = AttachmentFile()

        # 由首页进入待审批页面
        common_menus.find_element(CommonMenus.toDo).click()
        common_menus.find_element(CommonMenus.pending).click()
        flow.find_element(FlowPage.searchTitle).send_keys(num)
        flow.find_element(FlowPage.searchTitle).send_keys(Keys.ENTER)
        sleep(1)
        ActionChains(driver).move_to_element(flow.find_element(FlowPage.moveToReject)).perform()
        sleep(1)
        flow.find_element(FlowPage.rejectBut).click()
        sleep(1)
        # 填写驳回原因
        flow.find_element(FlowPage.rejectReason).send_keys(u'驳回，请重新填写')
        # 确定
        flow.find_element(FlowPage.confirmReject).click()
        # 上传附件
        # atta.upload_attachment(driver)
        sleep(2)

    # 提交单据
    def submit(self, driver):

        # 获取提交按钮
        buttons = driver.find_element_by_css_selector(".button_group_wrapper___3M-uZ")
        allOption = buttons.find_elements_by_tag_name("button")
        for option in allOption:
            if u'提交送审' in option.text:
                option.click()
                break
        sleep(2)

    # 借款未核销是否继续
    def loan_not_add(self, driver):

        new_exp = NewExpensePage(driver)
        exist = Exist(driver)
        # 判断有无借款未核销的提示，来判断是否处理这个提示
        loan_remain = exist.is_element_exist(NewExpensePage.loanText)

        if loan_remain:
            new_exp.find_element(NewExpensePage.continueOrNot).click()
            sleep(1)
        else:
            pass

    # 费用超标是否继续
    def fee_more_except(self, driver):

        new_exp = NewExpensePage(driver)
        exist = Exist(driver)
        # 判断有无费用超标的提示，来判断是否处理这个提示
        fee_remind = exist.is_element_exist(NewExpensePage.freeExceed)

        if fee_remind:
            new_exp.find_element(NewExpensePage.continueOrNot).click()
            sleep(1)
        else:
            pass

    # 审批时是否超预算
    def budget_excess(self, driver):

        new_exp = NewExpensePage(driver)
        exist = Exist(driver)
        # 判断有无预算超预算的提示，来判断是否处理这个提示
        budget_text = exist.is_element_exist(NewExpensePage.budget)
        if budget_text:
            new_exp.find_element(NewExpensePage.continueOrNot).click()
            sleep(1)
        else:
            pass

    # 获取到当前单据的单号
    def get_num(self, driver):
        flow = FlowPage(driver)
        receipt_num = flow.find_element(FlowPage.num).text
        print receipt_num
        return receipt_num

    def get_paid_money(self, driver):
        flow = FlowPage(driver)
        receipt_money = flow.find_element(FlowPage.paidMoney).text
        return receipt_money

    # 提交人提交借款单或申请单时选择审批人（第一个节点不是会签节点）
    def select_first_person(self, driver, person):
        flow = FlowPage(driver)
        flow.find_element(FlowPage.selectFirstPerson).click()
        flow.find_element(FlowPage.searchPerson).send_keys(person)
        flow.find_element(FlowPage.getPerson).click()
        flow.find_element(FlowPage.makeSureBut).click()
        flow.find_element(FlowPage.selectFirstPersonBut).click()
        sleep(2)

    # 同意后选择下一审批人
    def select_next_person(self, driver, next_person, remark):
        flow = FlowPage(driver)
        flow.find_element(FlowPage.selectPerson).click()
        flow.find_element(FlowPage.searchPerson).send_keys(next_person)
        sleep(1)
        flow.find_element(FlowPage.getPerson).click()
        sleep(1)
        flow.find_element(FlowPage.makeSureBut).click()
        flow.find_element(FlowPage.remark).send_keys(remark)
        flow.find_element(FlowPage.sendToNext).click()
        sleep(2)

    # 直接跳转入选人组件
    def select(self, driver, person):
        flow = FlowPage(driver)
        flow.find_element(FlowPage.searchPerson).send_keys(person)
        sleep(1)
        flow.find_element(FlowPage.getPerson).click()
        sleep(1)
        flow.find_element(FlowPage.makeSureBut).click()
        sleep(2)

    # 支付
    def paid(self, driver, num):

        # 由首页进入待支付页面
        common_menus = CommonMenus(driver)
        flow = FlowPage(driver)
        common_menus.find_element(CommonMenus.toDo).click()
        sleep(1)
        common_menus.find_element(CommonMenus.toBePaid).click()
        sleep(1)
        flow.find_element(FlowPage.searchTitle).send_keys(num)
        flow.find_element(FlowPage.searchTitle).send_keys(Keys.ENTER)
        sleep(1)
        ActionChains(driver).move_to_element(flow.find_element(FlowPage.moveToPaid)).perform()
        sleep(1)
        flow.find_element(FlowPage.paid).click()
        sleep(2)

    # 支付金额为0
    def paid_zero(self, driver):

        flow = FlowPage(driver)
        flow.find_element(FlowPage.paidZero).click()
        sleep(2)

    # 选择线下支付
    def offline_payment(self, driver):

        flow = FlowPage(driver)
        exist = Exist(driver)
        flow.find_element(FlowPage.offlinePay).click()
        flow.find_element(FlowPage.bankAccount).click()
        # 判断是否有影像签名
        exist_sign = exist.is_element_exist(FlowPage.sign)
        if exist_sign:
            # 影像签名开关关闭
            flow.find_element(FlowPage.signSwitch).click()
            # 选择支付方式后点击确定
            flow.find_element(FlowPage.bankAccountBut).click()
        else:
            flow.find_element(FlowPage.bankAccountButTwo).click()
        # 确认支付
        flow.find_element(FlowPage.confirmBut).click()
        sleep(2)

    # 首页搜索
    def search(self, driver, num):
        common_menus = CommonMenus(driver)
        flow = FlowPage(driver)
        # 返回到首页
        common_menus.find_element(CommonMenus.firstPage).click()
        sleep(3)
        flow.find_element(FlowPage.searchBut).click()
        flow.find_element(FlowPage.numSearch).send_keys(num)
        # 回车
        flow.find_element(FlowPage.numSearch).send_keys(Keys.ENTER)
        sleep(1)
        # 选中此单据
        flow.find_element(FlowPage.clickReceipt).click()
        sleep(1)

    # 提交人撤回
    def revoke(self, driver):
        flow = FlowPage(driver)
        # 获取撤回按钮
        buttons = driver.find_element_by_css_selector(".button_group_wrapper___3M-uZ")
        allOption = buttons.find_elements_by_tag_name("button")
        for option in allOption:
            if u'撤 回' in option.text:
                option.click()
                break
        sleep(1)
        # 确认撤回
        flow.find_element(FlowPage.confirmBut).click()
        sleep(2)

    # 评论
    def comment(self, driver):
        flow = FlowPage(driver)
        atta = AttachmentFile()
        buttons = driver.find_element_by_css_selector(".button_group_wrapper___3M-uZ")
        allOption = buttons.find_elements_by_tag_name("button")
        for option in allOption:
            if u'评 论' in option.text:
                option.click()
                break
        sleep(1)
        flow.find_element(FlowPage.commentTextClick).click()
        sleep(1)
        flow.find_element(FlowPage.commentText).send_keys(u'这是测试评论功能')
        flow.find_element(FlowPage.commentText).send_keys(Keys.SPACE)
        flow.find_element(FlowPage.commentText).send_keys(Keys.SHIFT, '2')
        sleep(1)
        flow.find_element(FlowPage.commentText).send_keys(u'孙静')
        flow.find_element(FlowPage.commentText).send_keys(Keys.ENTER)
        sleep(1)
        # 添加附件
        atta.upload_attachment(driver)
        # 评论完成，点击确认按钮
        flow.find_element(FlowPage.commentConfirmBut).click()
        sleep(2)

    # 搜索待办--待审批页面中某一单据，选中并查看其详情
    def look_over_details(self, driver, num):
        flow = FlowPage(driver)
        common_menus = CommonMenus(driver)
        # 由首页进入待审批页面
        common_menus.find_element(CommonMenus.toDo).click()
        common_menus.find_element(CommonMenus.pending).click()
        flow.find_element(FlowPage.searchTitle).send_keys(num)
        flow.find_element(FlowPage.searchTitle).send_keys(Keys.ENTER)
        sleep(5)
        # 首先点开单据详情
        flow.find_element(FlowPage.receiptDetail).click()
        sleep(5)

    # 查看某一单据的审批流程
    def look_over_process(self, driver):
        flow = FlowPage(driver)
        flow.find_element(FlowPage.approvalProcess).click()

    # 从单据流程页面修改单据的审批人
    def modify_approver_two(self, driver):
        flow = FlowPage(driver)
        # 修改第二个审批人，如果第二个审批人是曹玉静，则不做任何操作，若不是，则修改审批人

        name = flow.find_element(FlowPage.modifyApprovalTwo).text
        print name
        if name == gv.modify_approver:
            pass
        else:
            flow.find_element(FlowPage.modifyApprovalTwo).click()
            # 进入到选人组件
            self.select(driver, gv.modify_approver)

    def modify_approver_three(self, driver):
        flow = FlowPage(driver)
        # 修改第二个审批人，如果第二个审批人是曹玉静，则不做任何操作，若不是，则修改审批人

        name = flow.find_element(FlowPage.modifyApprovalThree).text
        if name == gv.modify_approver:
            pass
        else:
            flow.find_element(FlowPage.modifyApprovalThree).click()
            # 进入到选人组件
            self.select(driver, gv.modify_approver)

    # 审批人修改借款单
    def modify(self, driver):
        buttons = driver.find_element_by_css_selector(".button_group_wrapper___3M-uZ")
        allOption = buttons.find_elements_by_tag_name("button")
        for option in allOption:
            if u'修 改' in option.text:
                option.click()
                break
        sleep(0.5)

    # 修改借款单字段
    def modify_loan(self, driver):
        create_loan = CreateLoanPage(driver)

        create_loan.find_element(CreateLoanPage.loanTitle).clear()
        # 修改借款的标题和金额
        create_loan.find_element(CreateLoanPage.loanTitle).send_keys(u'借款单测试修改功能')
        # 清空之前的借款金额
        create_loan.find_element(CreateLoanPage.loanMoney).clear()
        create_loan.find_element(CreateLoanPage.loanMoney).send_keys(u'100')

    def modify_expense_title(self, driver):
        expense = NewExpensePage(driver)
        buttons = driver.find_element_by_css_selector(".button_group_wrapper___3M-uZ")
        allOption = buttons.find_elements_by_tag_name("button")
        for option in allOption:
            if u'修 改' in option.text:
                option.click()
                break
        expense.find_element(NewExpensePage.expenseTitle).send_keys(u'Sunday')

    # def modify_fee(self, driver):
    #     expense = NewExpensePage(driver)
    #     expense.find_element(NewExpensePage.feeItemFirst).click()



    def modify_save(self, driver, reason):
        flow = FlowPage(driver)
        # 保存
        flow.find_element(FlowPage.modifySave).click()
        # 填写修改原因
        flow.find_element(FlowPage.modifyReason).send_keys(reason)
        # 确定
        flow.find_element(FlowPage.modifyReasonBut).click()
        sleep(2)

    # 审批人批量同意
    def batch_check(self, driver, num):
        flow = FlowPage(driver)

        flow.find_element(FlowPage.searchTitle).send_keys(num)
        flow.find_element(FlowPage.searchTitle).send_keys(Keys.ENTER)
        sleep(5)
        # 勾选查询出来的单据
        flow.find_element(FlowPage.checkAll).click()
        # 清空搜索框
        flow.find_element(FlowPage.searchTitle).clear()

    def batch_agree(self, driver):
        flow = FlowPage(driver)

        # 批量同意
        flow.find_element(FlowPage.batchAgree).click()
        sleep(0.5)
        # 填写同意原因
        flow.find_element(FlowPage.agreeReason).send_keys(u'批量同意')
        # 确认
        flow.find_element(FlowPage.batchEnsureBut).click()
        sleep(2)

    # 审批人批量驳回
    def batch_reject(self, driver):
        flow = FlowPage(driver)
        # 批量驳回
        flow.find_element(FlowPage.batchReject).click()
        sleep(1)
        # 填写驳回原因
        flow.find_element(FlowPage.rejectReason).send_keys(u'驳回，请重新填写')
        # 确定
        flow.find_element(FlowPage.confirmReject).click()
        sleep(2)

    # 出纳批量支付
    def batch_paid(self, driver):
        flow = FlowPage(driver)

        # 批量支付
        flow.find_element(FlowPage.batchPaid).click()
        sleep(2)

    # 获取审批成功或失败的吐丝
    def message_reminder(self, driver):
        flow = FlowPage(driver)
        message_text = flow.find_element(FlowPage.message).text
        return message_text

    # 开启费用分摊按钮
    def open_share(self, driver):
        expense = NewExpensePage(driver)
        # 开启费用分摊
        expense.find_element(NewExpensePage.expenseShareBut).click()
        share_state = 1
        return share_state

    # 费用分摊，按部门分摊
    def expense_share_dep(self, driver, state):
        expense = NewExpensePage(driver)
        exist = Exist(driver)

        # 按部门分摊
        expense.find_element(NewExpensePage.shareWay).click()
        # 查找下拉列表中的报销部门
        buttons = driver.find_element_by_css_selector("#ekbc-modal-select-custom_z>div:nth-child(2)>div>div>div>ul")
        allOption = buttons.find_elements_by_tag_name("li")
        sleep(1)
        for option in allOption:
            if u'报销部门分摊' == option.text:
                option.click()
                sleep(1)
                break
        sleep(1)

        # 判断有无确认修改费用分摊方式的提示，来判断是否处理这个提示
        share_way_remind = exist.is_element_exist(NewExpensePage.shareText)

        if share_way_remind:
            expense.find_element(NewExpensePage.continueOrNot).click()
            sleep(1)
        else:
            pass

        for i in range(0, 3):

            expense.find_element(NewExpensePage.shareDep).click()
            sleep(2)
            expense.find_element1(NewExpensePage.searchDep).clear()
            expense.find_element1(NewExpensePage.searchDep).send_keys(gv.dep[i])
            expense.find_element(NewExpensePage.ensureSearchDep).click()
            sleep(1)
            expense.find_element(NewExpensePage.shareScale).clear()
            sleep(1)
            expense.find_element(NewExpensePage.shareScale).send_keys(gv.scale[i])
            # 保存
            expense.find_element(NewExpensePage.saveShare).click()
            # 根据是批量分摊还是单个分摊来判断分摊已达100%
            if state == 1:

                # 判断目前分摊金额是否为此费用类型的金额
                totle_money = expense.find_element(NewExpensePage.shareTotle).text
                if totle_money == gv.expense_amount:
                    break
                else:
                    # 添加分摊
                    expense.find_element(NewExpensePage.addShare).click()
                    sleep(1)
            elif state == 2:
                # 根据当前分摊比例来判断
                total_scale = expense.find_element(NewExpensePage.totalScale).text
                if total_scale == u'总计: 100%':
                    break
                else:
                    # 添加分摊
                    expense.find_element(NewExpensePage.addShare).click()
                    sleep(1)
            else:
                print '当前无分摊'

    # 费用分摊，按项目分摊
    def expense_share_project(self, driver):
        expense = NewExpensePage(driver)
        exist = Exist(driver)

        # 按项目分摊
        expense.find_element(NewExpensePage.shareWay).click()
        sleep(4)
        # 选择项目分摊
        buttons = driver.find_element_by_css_selector("#ekbc-modal-select-custom_z>div:nth-child(2)>div>div>div>ul")
        allOption = buttons.find_elements_by_tag_name("li")
        sleep(1)

        for option in allOption:
            if u'项目分摊' == option.text:
                option.click()
                sleep(1)
                break
        sleep(1)
        # 判断有无确认修改费用分摊方式的提示，来判断是否处理这个提示
        share_way_remind = exist.is_element_exist(NewExpensePage.shareText)

        if share_way_remind:
            expense.find_element(NewExpensePage.continueOrNot).click()
            sleep(1)
        else:
            pass

        sleep(1)
        # 添加项目
        for i in range(0, 2):
            # 按项目分摊
            expense.find_element(NewExpensePage.shareDep).click()
            expense.find_element1(NewExpensePage.searchDep).clear()
            expense.find_element1(NewExpensePage.searchDep).send_keys(gv.project[i])
            expense.find_element(NewExpensePage.ensureSearchDep).click()
            sleep(1)
            expense.find_element(NewExpensePage.shareScale).clear()
            sleep(1)
            expense.find_element(NewExpensePage.shareScale).send_keys(gv.scale[i])
            # 保存
            expense.find_element(NewExpensePage.saveShare).click()
            sleep(1)
            # 判断目前分摊金额是否为此费用类型的金额
            totle_money = expense.find_element(NewExpensePage.shareTotle).text
            if totle_money == gv.expense_amount:
                break
            else:
                # 添加分摊
                expense.find_element(NewExpensePage.addShare).click()
                sleep(1)

    # 费用分摊，按部门和项目分摊
    def expense_share_dep_project(self, driver):
        expense = NewExpensePage(driver)
        exist = Exist(driver)

        # 按项目和部门分摊
        expense.find_element(NewExpensePage.shareWay).click()
        # 选择部门、项目分摊
        buttons = driver.find_element_by_css_selector("#ekbc-modal-select-custom_z>div:nth-child(2)>div>div>div>ul")
        allOption = buttons.find_elements_by_tag_name("li")
        sleep(1)

        for option in allOption:
            if u'报销部门&项目分摊' == option.text:
                option.click()
                break
        sleep(1)
        # 判断有无确认修改费用分摊方式的提示，来判断是否处理这个提示
        share_way_remind = exist.is_element_exist(NewExpensePage.shareText)

        if share_way_remind:
            expense.find_element(NewExpensePage.continueOrNot).click()
            sleep(1)
        else:
            pass

        sleep(1)
        # 按部门、项目分摊

        for i in range(0, 2):
            # 先选择报销部门
            expense.find_element(NewExpensePage.shareDep).click()
            expense.find_element1(NewExpensePage.searchDep).clear()
            expense.find_element1(NewExpensePage.searchDep).send_keys(gv.dep[i])
            expense.find_element(NewExpensePage.ensureSearchDep).click()
            sleep(1)

            # 再选择项目
            expense.find_element(NewExpensePage.sharePro).click()
            sleep(1)
            expense.find_element(NewExpensePage.searchPro).clear()
            expense.find_element(NewExpensePage.searchPro).send_keys(gv.project[i])
            sleep(2)
            expense.find_element(NewExpensePage.ensureSearchPro).click()
            sleep(1)
            expense.find_element(NewExpensePage.shareScale).clear()
            sleep(1)
            expense.find_element(NewExpensePage.shareScale).send_keys(gv.scale[i])
            # 保存
            expense.find_element(NewExpensePage.saveShare).click()
            sleep(1)
            # 判断目前分摊金额是否为此费用类型的金额
            totle_money = expense.find_element(NewExpensePage.shareTotle).text
            if totle_money == gv.expense_amount:
                break
            else:
                # 添加分摊
                expense.find_element(NewExpensePage.addShare).click()
                sleep(1)

    # 批量分摊
    def expense_batch_share(self, driver):
        # 对所有费用明细进行批量分摊
        expense = NewExpensePage(driver)
        # 勾选全部按钮
        expense.find_element(NewExpensePage.checkAllBut).click()
        expense.find_element(NewExpensePage.batchShare).click()
        share_state = 2
        return share_state

    # 保存费用分摊
    def expense_batch_share_save(self, driver):
        expense = NewExpensePage(driver)
        expense.find_element(NewExpensePage.saveShareBut).click()
        sleep(1)

    # 添加申请单
    def add_requisition(self, driver):
        expense = NewExpensePage(driver)
        expense.find_element(NewExpensePage.addRequisition).click()
        sleep(5)
        # 从下拉框中选择出要关联的申请单
        buttons = driver.find_element_by_css_selector("#expense-link-select>div:nth-child(2)>div>div>div>ul")
        allOption = buttons.find_elements_by_tag_name("li")
        for option in allOption:
            print option.text

            if option.text == u'出差申请':
                option.click()
                sleep(1)
                break
            else:
                # 选择第一个申请单吧
                driver.find_element_by_css_selector("#expense-link-select>div:nth-child(2)>div>div>div>ul>li:nth-child(1)").click()
                sleep(5)

    # 遍历出所有的借款单
    def get_loan_count(self, driver):
        expense = NewExpensePage(driver)
        expense.find_element(NewExpensePage.addVerificationBut).click()
        sleep(2)
        # 遍历出可核销的借款有多少
        ul = driver.find_element_by_css_selector(".writtenoff-list-content___rhb8E>div:nth-child(1)>ul")
        lis = ul.find_elements_by_tag_name("li")
        return len(lis)

    # 选择要核销的借款单
    def add_verification(self, driver, loan_nums):
        expense = NewExpensePage(driver)

        for i in range(loan_nums):
            i = i+1
            click_state = driver.find_element_by_xpath("//div[@class = 'writtenoff-list']/ul/li[%s]/div[1]/label/span[1]/input" % i).is_enabled()
            if click_state:
                driver.find_element_by_xpath("//div[@class = 'writtenoff-list']/ul/li[%s]/div[1]/label/span[1]/input" % i).click()
                break
            while i == loan_nums:
                if not click_state:
                    print u'无可核销借款'

        expense.find_element(NewExpensePage.ensureLoan).click()
        sleep(1)






    # 导入发票可以在新建时写方法，这个不会在好多地方用