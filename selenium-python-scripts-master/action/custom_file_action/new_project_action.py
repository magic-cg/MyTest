# -*- coding: utf-8 -*-
from page.custom_file_page.new_project_page import NewProjectPage
from common.common_menu_page import CommonMenus
from common.common_flow_page import FlowPage
from time import sleep
import config.global_variable as gv


class NewProjectAction:

    def new_project(self, driver):
        new_pro = NewProjectPage(driver)

        common_menu = CommonMenus(driver)
        # 进入自定义档案页面
        common_menu.find_element(CommonMenus.enterpriseManagement).click()
        common_menu.find_element(CommonMenus.archives).click()
        new_pro.find_element(NewProjectPage.project).click()

    def father_project(self, driver, project):
        # 进入项目模块，新建父级项目
        new_pro = NewProjectPage(driver)
        # project = gv.project_name
        for i in range(len(project)):
            new_pro.find_element(NewProjectPage.new).click()
            new_pro.find_element(NewProjectPage.projectName).send_keys(project[i])
            new_pro.find_element(NewProjectPage.save).click()
            sleep(2)

    def child_project(self, driver, project_name3, project_name2):
        new_pro = NewProjectPage(driver)

        # 新建子级项目
        new_pro.find_element(NewProjectPage.new).click()
        new_pro.find_element(NewProjectPage.projectName).send_keys(project_name3)
        # 选择父级
        new_pro.find_element(NewProjectPage.superior).click()
        new_pro.find_element(NewProjectPage.selectSuperior).send_keys(project_name2)
        new_pro.find_element(NewProjectPage.ensureSuperior).click()

    def limit(self, driver):
        new_pro = NewProjectPage(driver)
        flow = FlowPage(driver)

        # 限制可见范围
        new_pro.find_element(NewProjectPage.limitPerson).click()
        new_pro.find_element(NewProjectPage.visiblePerson).click()
        sleep(2)

        for i in range(len(gv.list_select_person)):
            flow.find_element(FlowPage.searchPerson).send_keys(gv.list_select_person[i])
            flow.find_element(FlowPage.multipleChoice).click()
            flow.find_element(FlowPage.searchPerson).clear()
            sleep(1)

        flow.find_element(FlowPage.makeSureBut).click()
        new_pro.find_element(NewProjectPage.save).click()
        sleep(2)

    def disable_project(self, driver, project_name4):
        new_pro = NewProjectPage(driver)
        new_pro.find_element(NewProjectPage.search).send_keys(project_name4)
        new_pro.find_element(NewProjectPage.clickSearchProject).click()
        new_pro.find_element(NewProjectPage.disable).click()
        sleep(1)
        new_pro.find_element(NewProjectPage.ensureDisable).click()
        sleep(2)
