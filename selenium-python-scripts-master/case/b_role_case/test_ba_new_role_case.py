import unittest
import common.login
import config.global_variable as gv
from action.role_action.new_role_action import NewRoler
from time import sleep


class TestNewRole(unittest.TestCase):

    def setUp(self):
        self.driver = common.login.get_driver_cyj()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_new_role(self):
        new_role = NewRoler()
        new_role.new_group_role(self.driver, gv.role_group_name1)
        new_role.new_role(self.driver, gv.role_name1)
        new_role.select_roler(self.driver)
