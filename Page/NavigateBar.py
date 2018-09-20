#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Page.BasePage import BasePage


class NavigateBar(BasePage):

    def navigate_bar(self, get_locator=False):
        # 这里不能用 navigate_bar 本身的定位器来定位，因为即使导航栏不可见了，但是依然在DOM中，只能通过body里的.nav-menu-open来判断
        return self._define_element(get_locator=get_locator)

    def utest_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def user_name_link(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def articles_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def training_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def forums_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def tools_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def projects_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def sign_out_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)


if __name__ == '__main__':
    driver = None
    navigateBar = NavigateBar(driver)
    print(navigateBar.navigate_bar())
    print(navigateBar.navigate_bar(get_locator=True))
