#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Page.NavigateBar import NavigateBar
from Page.HomePage import HomePage
from Utils.Paths import CHROME_DRIVER_PATH
from Utils.PUnittest import PUnittest
from Utils.Logger import logger
from Utils.Decorator import wrapped_testcase
from selenium import webdriver
import unittest
import time


class TestSubPageTitle(PUnittest):

    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    homePage = HomePage(driver)
    navigateBar = NavigateBar(driver)

    @classmethod
    def setUpClass(cls):
        cls.homePage.browser.navigate_to('https://www.utest.com/')

    @classmethod
    def tearDownClass(cls):
        cls.homePage.browser.quit()

    def setUp(self):
        logger.info(' {0} >> {1} '.format(self.__class__.__name__, self._testMethodName).center(100, '*'))

    def tearDown(self):
        logger.info('*' * 100 + '\n')

    @wrapped_testcase()
    def test_articles_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.articles_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'Software Testing Articles')

    @wrapped_testcase()
    def test_training_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.training_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'Software Testing Courses')

    @wrapped_testcase()
    def test_forums_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.forums_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'xxxxxxxxxxxxxxxx')

    @wrapped_testcase()
    def test_tools_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.tools_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'Software Testing Tool Reviews')

    @wrapped_testcase()
    def test_projects_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.projects_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'xxxxxxxxxxxxxxxxxxx')


if __name__ == '__main__':
    unittest.main()
