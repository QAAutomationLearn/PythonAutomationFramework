#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Page.BasePage import BasePage


class NavigateBar(BasePage):

    def navigate_bar(self):
        # 这里不能用 navigate_bar 本身的定位器来定位，因为即使导航栏不可见了，但是依然在DOM中，只能通过body里的.nav-menu-open来判断
        return self._define_element()

    def utest_button(self):
        return self._define_element()

    def articles_button(self):
        return self._define_element()

    def training_button(self):
        return self._define_element()

    def forums_button(self):
        return self._define_element()

    def tools_button(self):
        return self._define_element()

    def projects_button(self):
        return self._define_element()

if __name__ == '__main__':
    driver = None
    navigateBar = NavigateBar(driver)
    print(navigateBar.navigate_bar())
