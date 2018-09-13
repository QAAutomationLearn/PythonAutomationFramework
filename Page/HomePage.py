#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Page.BasePage import BasePage


class HomePage(BasePage):

    def expand_navigate_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def title_label(self, get_locator=False):
        return self._define_element(get_locator=get_locator)


if __name__ == '__main__':
    pass
