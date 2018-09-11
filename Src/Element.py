#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Src.Browser import Browser
from Src.Wait import Wait
from Utils.Decorator import logger_element
from Utils.ParseConfig import parseConfig
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

WAIT_UNTIL_TIMEOUT = parseConfig.time_config('WaitUntilTimeout')
WAIT_FREQUENCY = parseConfig.time_config('WaitFrequency')


class MetaDecorator(type):
    def __new__(mcs, cls_name, supers, cls_dict):
        for attr, val in cls_dict.items():
            if val.__class__.__name__ == 'function':
                if attr not in ['__init__']:
                    cls_dict[attr] = logger_element()(val)
        return type.__new__(mcs, cls_name, supers, cls_dict)


class Element(metaclass=MetaDecorator):

    def __init__(self, driver, name, locator):
        self.locator = locator
        self.name = name
        self.driver = driver

    def click(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        Browser(self.driver)._get_element(self.locator).click()

    def clear(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        Browser(self.driver)._get_element(self.locator).clear()

    def send_keys(self, value, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        Browser(self.driver)._get_element(self.locator).send_keys(value)

    def submit(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        Browser(self.driver)._get_element(self.locator).submit()

    def get_text(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_visible(self.locator, timeout, frequency)
        text = Browser(self.driver)._get_element(self.locator).text
        return text

    def get_size(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_clickable(self.locator, timeout, frequency)
        size = Browser(self.driver)._get_element(self.locator).size
        return size

    def get_attribute(self, attribute, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        Wait(self.driver).element_present(self.locator, timeout, frequency)
        value = Browser(self.driver)._get_element(self.locator).get_attribute(attribute)
        return value

    def is_displayed(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        try:
            Wait(self.driver).element_visible(self.locator, timeout, frequency)
            Browser(self.driver)._get_element(self.locator).is_displayed()
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_enabled(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        try:
            Wait(self.driver).element_visible(self.locator, timeout, frequency)
            Browser(self.driver)._get_element(self.locator).is_enabled()
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_selected(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        try:
            Wait(self.driver).element_visible(self.locator, timeout, frequency)
            Browser(self.driver)._get_element(self.locator).is_selected()
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def switch_to_frame(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = Wait(self.driver).frame_switchable(self.locator, timeout, frequency)
        time.sleep(2)  # Chrome issue, have to wait sometime after switching frame
        return result
