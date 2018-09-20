#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Logger import logger
from Utils.Decorator import logger_browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException
import sys
import re


class KeyActions:
    """封装键盘动作，主要处理一些特殊的键区"""
    def __init__(self, driver):
        self.driver = driver

    def send_specific_keys(self, *args):
        keys_set = set()
        redundant_keys = ['BACK_SPACE', 'LEFT_SHIFT', 'LEFT_CONTROL', 'LEFT_ALT',
                          'ARROW_LEFT', 'ARROW_UP', 'ARROW_RIGHT', 'ARROW_DOWN']
        try:
            keys_mapping = dict(filter(lambda d: d[0] not in redundant_keys, Keys.__dict__.items()))
            for arg in args:
                pattern = re.compile(arg, re.IGNORECASE)
                for attr in keys_mapping:
                    result = re.search(pattern, attr)
                    if result:
                        keys_set.add(attr)
            if keys_set:
                self.driver.send_keys(*keys_set)
                logger.debug('[Call]: KeyActions >> send_specific_keys >> {0}'.format(' + '.join(keys_set)))
            else:
                self.driver.send_keys('')
                logger.warning('[Call]: KeyActions >> send_specific_keys >> empty content')
        except WebDriverException as e:
            exc_type, _, _ = sys.exc_info()
            logger.error('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
            raise
        except Exception:
            logger.exception('[UnwantedException]:')
            raise


class MetaDecorator(type):
    def __new__(mcs, cls_name, supers, cls_dict):
        for attr, val in cls_dict.items():
            if val.__class__.__name__ == 'function':
                if attr not in ['__init__']:
                    cls_dict[attr] = logger_browser()(val)
        return type.__new__(mcs, cls_name, supers, cls_dict)


class MouseActions(metaclass=MetaDecorator):
    """封装鼠标动作"""
    def __init__(self, driver):
        self.driver = driver
        self._actions = ActionChains(self.driver)

    def right_click(self, element=None):
        self._actions.context_click(on_element=element).perform()

    def double_click(self, element=None):
        self._actions.double_click(on_element=element).perform()

    def move_to_element(self, element):
        self._actions.move_to_element(to_element=element).perform()

    def move_by_offset(self, xoffset, yoffset):
        self._actions.move_by_offset(xoffset=xoffset, yoffset=yoffset).perform()

    def click_and_hold(self, element=None):
        self._actions.click_and_hold(on_element=element).perform()

    def drag_and_drop(self, source, target):
        self._actions.drag_and_drop(source=source, target=target).perform()


if __name__ == '__main__':
    k = KeyActions('')
    k.send_specific_keys('control', 'pad2', 'pad1')
    k.send_specific_keys('asd')
