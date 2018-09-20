#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Src.Engine import ENGINE
from Page.BasePage import BasePage
from Page.HomePage import HomePage
from Page.NavigateBar import NavigateBar
from Utils.ParseTestData import ParseTestData

driver = ENGINE.get_driver()
homePage = HomePage(driver)
navigateBar = NavigateBar(driver)

login_success_data = ParseTestData().get_test_data('login_success')
login_success_username = login_success_data[0][1] if login_success_data else 'Helloworld@gmail.com'
login_success_password = login_success_data[0][2] if login_success_data else 'Python3.6!'


class LoginPage(BasePage):

    def username_textbox(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def username_empty_prompt(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def password_textbox(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def password_empty_prompt(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def access_account_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def wrong_credential_label(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def LoginWebsite(self, username=login_success_username, password=login_success_password):
        """
        登录网站
        :param username: 用户名
        :param password: 密码
        :return: 二元组，login_status代表登录状态，result代表验证状态
        """
        self.username_textbox().clear()
        self.username_textbox().send_keys(username)
        self.password_textbox().clear()
        self.password_textbox().send_keys(password)
        self.access_account_button().click()
        if username == login_success_username and password == login_success_password:
            homePage.ExpandNavigateBar()
            assert_result = navigateBar.user_name_link().is_displayed()
            login_status = True
        elif username == '':
            assert_result = self.username_empty_prompt().is_displayed()
            login_status = False
        elif password == '':
            assert_result = self.password_empty_prompt().is_displayed()
            login_status = False
        else:
            assert_result = self.wrong_credential_label().is_displayed()
            login_status = False
        return login_status, assert_result


if __name__ == '__main__':
    print(login_success_data)
