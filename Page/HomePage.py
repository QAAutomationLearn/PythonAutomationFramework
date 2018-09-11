#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Page.BasePage import BasePage


class HomePage(BasePage):

    def expand_navigate_button(self):
        return self._define_element()

    def title_label(self):
        return self._define_element()


if __name__ == '__main__':
    pass
