# -*- coding: utf-8 -*-
from time import sleep
from page.attachment_page import AttachmentPage
from common.exist import Exist


class AttachmentFile:

    # 上传
    def upload_attachment(self, driver):
        atta = AttachmentPage(driver)
        atta.find_element(AttachmentPage.uploadAttachment).send_keys('/Users/wei/Downloads/zhi.pdf')
        sleep(2)

    # 下载
    def download_part(self, driver, reason):
        atta = AttachmentPage(driver)
        sleep(1)
        # 验证列表中是否有单据存在
        click_state = atta.find_element(AttachmentPage.selectCurrent).is_enabled()
        if click_state:
            # 选中当前第一页
            atta.find_element(AttachmentPage.selectCurrent).click()
            sleep(1)
            # 点击导出选中
            atta.find_element(AttachmentPage.exportSelect).click()
            sleep(2)
            # 导出
            atta.find_element(AttachmentPage.exportButOne).click()
            sleep(2)
        else:
            print reason

    def download_part_two(self, driver, reason):
        atta = AttachmentPage(driver)
        sleep(1)
        click_state = atta.find_element(AttachmentPage.selectCurrentTwo).is_enabled()
        if click_state:
            # 选中当前第一页
            atta.find_element(AttachmentPage.selectCurrentTwo).click()
            sleep(1)
            # 点击导出选中
            atta.find_element(AttachmentPage.exportSelectTwo).click()
            sleep(2)
            # 导出
            atta.find_element(AttachmentPage.exportButOne).click()
            sleep(2)
        else:
            print reason

    def download_part_three(self, driver, reason):
        atta = AttachmentPage(driver)
        sleep(1)

        click_state = atta.find_element(AttachmentPage.selectCurrentThree).is_enabled()
        if click_state:
            # 选中当前第一页
            atta.find_element(AttachmentPage.selectCurrentThree).click()
            sleep(1)
            # 点击导出选中
            atta.find_element(AttachmentPage.exportSelectThree).click()
            sleep(2)
            # 导出
            atta.find_element(AttachmentPage.exportButOne).click()
            sleep(2)
        else:
            print reason

    def download_all(self, driver, reason):
        atta = AttachmentPage(driver)
        # 因为报销单管理中的导出与其他页面中的导出全部功能不一致，故单独写导出全部
        flag_state = atta.find_element(AttachmentPage.exportAll).is_enabled()
        # flag_state = is_exist.is_element_exist(AttachmentPage.exportAll)

        if flag_state:
            atta.find_element(AttachmentPage.exportAll).click()
            sleep(1)
            # 导出
            atta.find_element(AttachmentPage.exportButOne).click()
            sleep(1)
        else:
            print reason

    def downlaod_all_one(self, driver, reason):
        atta = AttachmentPage(driver)
        # 拿借款管理举例，申请中页面导出全部
        is_exist = Exist(driver)
        flag_state = is_exist.is_element_exist(AttachmentPage.selectAllOne)
        if flag_state:

            atta.find_element(AttachmentPage.selectAllOne).click()
            sleep(2)
            atta.find_element(AttachmentPage.exportButTWo).click()
            sleep(1)
            atta.find_element(AttachmentPage.exportButOne).click()
            sleep(1)
        else:
            print reason

    def downlaod_all_two(self, driver, reason):
        atta = AttachmentPage(driver)
        # 拿借款管理举例，待还款页面导出全部
        is_exist = Exist(driver)
        flag_state = is_exist.is_element_exist(AttachmentPage.selectAllTwo)

        if flag_state:

            atta.find_element(AttachmentPage.selectAllTwo).click()
            sleep(2)
            atta.find_element(AttachmentPage.exportButTWo).click()
            sleep(1)
            atta.find_element(AttachmentPage.exportButOne).click()
            sleep(1)
        else:
            print reason

    def downlaod_all_three(self, driver, reason):
        atta = AttachmentPage(driver)
        # 拿借款管理举例，已完成页面导出全部
        is_exist = Exist(driver)
        flag_state = is_exist.is_element_exist(AttachmentPage.selectAllThree)
        if flag_state:
            atta.find_element(AttachmentPage.selectAllThree).click()
            sleep(2)
            atta.find_element(AttachmentPage.exportButTWo).click()
            sleep(1)
            atta.find_element(AttachmentPage.exportButOne).click()
            sleep(1)
        else:
            print reason
