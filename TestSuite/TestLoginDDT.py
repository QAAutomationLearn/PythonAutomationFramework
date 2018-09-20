#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Page.NavigateBar import NavigateBar
from Page.HomePage import HomePage
from Page.LoginPage import LoginPage
from Src.PUnittest import PUnittest
from Src.Engine import ENGINE
from Utils.ParseTestData import ParseTestData
from Utils.Logger import logger
import ddt


@ddt.ddt
class TestLoginDDT(PUnittest):

    driver = ENGINE.get_driver()
    homePage = HomePage(driver)
    navigateBar = NavigateBar(driver)
    loginPage = LoginPage(driver)
    login_test_data = ParseTestData().get_test_data('login')

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        logger.info(' {0} >> {1} '.format(self.__class__.__name__, self._testMethodName).center(100, '*'))
        self.homePage.browser.navigate_to('https://www.utest.com/')
        self.homePage.sign_in_button().click()

    def tearDown(self):
        logger.info('*' * 100 + '\n')

    @ddt.data(*login_test_data)
    @ddt.unpack
    def test_login(self, condition, username, password):
        login_status, check_result = self.loginPage.LoginWebsite(username, password)
        self.assertTrue(check_result)
        if 'success' in condition:
            self.assertTrue(login_status)
            self.homePage.Logout()
        elif 'fail' in condition:
            self.assertFalse(login_status)
        self.homePage.key_actions.send_specific_keys('numlock')
        self.homePage.mouse_actions.double_click(self.homePage.sign_in_button())


if __name__ == '__main__':
    pass
