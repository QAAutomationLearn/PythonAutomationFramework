#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.ParseConfig import parseConfig
from Utils.Decorator import logger_wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

WAIT_IMPLICITY_TIMEOUT = parseConfig.time_config('ImplicityWaitTime')
WAIT_UNTIL_TIMEOUT = parseConfig.time_config('WaitUntilTimeout')
WAIT_UNTIL_NOT_TIMEOUT = parseConfig.time_config('WaitUntilNotTimeout')
WAIT_FREQUENCY = parseConfig.time_config('WaitFrequency')


class MetaDecorator(type):
    def __new__(mcs, cls_name, supers, cls_dict):
        for attr, val in cls_dict.items():
            if val.__class__.__name__ == 'function':
                if attr not in ['__init__']:
                    cls_dict[attr] = logger_wait()(val)
        return type.__new__(mcs, cls_name, supers, cls_dict)


class Wait(metaclass=MetaDecorator):
    """封装了selenium的WebDriverWait类"""
    def __init__(self, driver):
        self.driver = driver

    def set_implicitly_wait(self, timeout=WAIT_IMPLICITY_TIMEOUT):
        self.driver.implicitly_wait(timeout)

    def title_is(self, title, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.title_is(title), 'Wait title is {0}'.format(title))
        return result

    def title_is_not(self, title, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.title_is(title), 'Wait title is not {0}'.format(title))
        return result

    def title_contains(self, title, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.title_contains(title), 'Wait title contains {0}'.format(title))
        return result

    def title_not_contains(self, title, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.title_contains(title), 'Wait title not contains {0}'.format(title))
        return result

    def element_present(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.presence_of_element_located(locator), 'Wait element {0} presents'.format(locator))
        return result

    def element_not_present(self, locator, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.presence_of_element_located(locator), 'Wait element {0} not presents'.format(locator))
        return result

    def element_clickable(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.element_to_be_clickable(locator), 'Wait element {0} clickable'.format(locator))
        return result

    def element_not_clickable(self, locator, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.element_to_be_clickable(locator), 'Wait element {0} not clickable'.format(locator))
        return result

    def element_visible(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.visibility_of_element_located(locator), 'Wait element {0} visible'.format(locator))
        return result

    def element_not_visible(self, locator, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.visibility_of_element_located(locator), 'Wait element {0} not visible'.format(locator))
        return result

    def frame_switchable(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(
            ec.frame_to_be_available_and_switch_to_it(locator), 'Wait frame {0} switchable'.format(locator))
        return result

    def frame_not_switchable(self, locator, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(
            ec.frame_to_be_available_and_switch_to_it(locator), 'Wait frame {0} not switchable'.format(locator))
        return result

    def alert_present(self, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until(ec.alert_is_present(), 'Wait alert visible')
        return result

    def alert_not_present(self, timeout=WAIT_UNTIL_NOT_TIMEOUT, frequency=WAIT_FREQUENCY):
        result = WebDriverWait(self.driver, timeout, frequency).until_not(ec.alert_is_present(), 'Wait alert not visible')
        return result
