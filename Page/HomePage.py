#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Src.Engine import ENGINE
from Page.BasePage import BasePage
from Page.NavigateBar import NavigateBar

driver = ENGINE.get_driver()
navigateBar = NavigateBar(driver)


class HomePage(BasePage):

    def expand_navigate_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def title_label(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def sign_in_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    # 不管导航栏是否展开，都确保其展开
    def ExpandNavigateBar(self):
        navigate_bar_visible = navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.expand_navigate_button().click()
        self.wait.sleep()

    # 打开导航栏，并注销
    def Logout(self):
        self.ExpandNavigateBar()
        sign_out_button_visible = navigateBar.sign_out_button().is_displayed()
        if sign_out_button_visible:
            navigateBar.sign_out_button().click()
            return True
        else:
            return True

if __name__ == '__main__':
    pass
