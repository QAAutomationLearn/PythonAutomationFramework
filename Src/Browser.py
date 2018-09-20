#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Decorator import logger_browser
from Utils.ParseConfig import WAIT_UNTIL_TIMEOUT, WAIT_FREQUENCY
from Utils.Paths import RESULTS_SCREENSHOTS_DIR
from selenium.webdriver.support.wait import WebDriverWait
import time
import os


class MetaDecorator(type):
    def __new__(mcs, cls_name, supers, cls_dict):
        for attr, val in cls_dict.items():
            if val.__class__.__name__ == 'function':
                # 列表中方法的日志不在这里记录，所以为了避免重复记日志，将其排除
                if attr not in ['__init__', '_get_element', '_get_elements']:
                    cls_dict[attr] = logger_browser()(val)
        return type.__new__(mcs, cls_name, supers, cls_dict)


class Browser(metaclass=MetaDecorator):
    """封装了selenium的WebDriver类"""
    def __init__(self, driver):
        self.driver = driver

    def _get_element(self, locator):
        """该方法专门给Element封装用，所以写作私有方法，平时不需要调用"""
        return self.driver.find_element(by=locator[0], value=locator[1])

    def _get_elements(self, locator):
        """该方法专门给Element封装用，所以写作私有方法，平时不需要调用"""
        return self.driver.find_elements(by=locator[0], value=locator[1])

    def get_element(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        """
        通过定位器获取页面元素，每一段时间尝试获取一次，获取成功后返回获取的页面元素，获取失败后抛出 NoSuchElement 异常
        locator: 定位器，包含定位方式和定位表达式的元组，如("id", "username")
        timeout: 超时时间，默认为30秒
        frequency: 获取频率，默认为0.5秒
        """
        # 之所以使用lambda表达式是因为util接收的参数是method而不是element，所以不能显式调用find_element方法，
        # 而是将find_element方法作为参数传给until。同时method的参数是driver，所以这里lambda表达式接收的参数也是driver。
        # until 也可以使用expected_conditions，EC所有的类都是期望场景，实例方法__call__里接收参数driver。
        element = WebDriverWait(self.driver, timeout, frequency).until(
            lambda _driver: _driver.find_element(by=locator[0], value=locator[1]), str(locator))
        return element

    def get_elements(self, locator, timeout=WAIT_UNTIL_TIMEOUT, frequency=WAIT_FREQUENCY):
        elements = WebDriverWait(self.driver, timeout, frequency).until(
            lambda _driver: _driver.find_elements(by=locator[0], value=locator[1]), str(locator))
        return elements

    def get_source(self):
        return self.driver.page_source

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_driver(self):
        return self.driver

    def navigate_to(self, url):
        self.driver.get(url)

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()
        time.sleep(2)  # Chrome issue, have to wait sometime after switching frame

    def switch_to_default_frame(self):
        self.driver.switch_to.default_content()
        time.sleep(2)  # Chrome issue, have to wait sometime after switching frame

    def get_alert_text(self):
        text = self.driver.switch_to.alert.text
        return text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def send_alert_keys(self, value):
        self.driver.switch_to.alert.send_keys(value)

    def set_window_size(self, x, y):
        self.driver.set_window_size(x, y)

    def maximize_window(self):
        self.driver.maximize_window()

    def minimize_window(self):
        self.driver.minimize_window()

    def new_window(self, url):
        js = 'window.open("{0}");'.format(url)
        self.driver.execute_script(js)

    def switch_to_first_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    def switch_to_last_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def switch_to_specific_window(self, window_index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[window_index-1])

    def get_cookies(self):
        self.driver.get_cookies()

    def get_cookie(self, cookie_name):
        self.driver.get_cookie(cookie_name)

    def delete_cookies(self):
        self.driver.delete_all_cookies()

    def delete_cookie(self, name, option_string):
        self.driver.delete_cookie(name, option_string)

    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def take_screenshot(self, filename):
        now_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        _filename = '{0}_{1}.png'.format(now_time, filename)
        if not os.path.exists(RESULTS_SCREENSHOTS_DIR):
            os.makedirs(RESULTS_SCREENSHOTS_DIR)
        filepath = os.path.join(RESULTS_SCREENSHOTS_DIR, _filename)
        self.driver.get_screenshot_as_file(filepath)
