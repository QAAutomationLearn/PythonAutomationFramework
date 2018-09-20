#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Paths import FRAME_CONFIG_FILE_PATH
from Utils.Logger import logger
from configparser import ConfigParser


def wrapped_parse_config(func):
    """用来装饰ParseConfig类中所有的解析方法，添加异常日志"""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger.debug('Parse "{0}", get config value "{1}"'.format(func.__name__, result))
            return result
        except Exception as e:
            logger.error('Fail to parse "{0}": {1}'.format(func.__name__, e))
            raise e
    return wrapper


class MetaDecorator(type):
    def __new__(mcs, cls_name, supers, cls_dict):
        for attr, val in cls_dict.items():
            if val.__class__.__name__ == 'function':
                if attr not in ['__init__']:
                    cls_dict[attr] = wrapped_parse_config(val)
        return type.__new__(mcs, cls_name, supers, cls_dict)


class ParseConfig(metaclass=MetaDecorator):
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(FRAME_CONFIG_FILE_PATH)

    # ******************************* LogConfig *******************************
    def console_log_switch(self):
        value = self.config.get('LogConfig', 'ConsoleSwitch')
        value = True if value != 'False' else False
        return value

    def file_log_switch(self):
        value = self.config.get('LogConfig', 'FileSwitch')
        value = True if value != 'False' else False
        return value

    def console_log_level(self):
        value = self.config.get('LogConfig', 'ConsoleLevel')
        return value

    def file_log_level(self):
        value = self.config.get('LogConfig', 'FileLevel')
        return value

    # ******************************** TimeConfig *******************************
    def implicity_wait_time(self):
        value = self.config.get('TimeConfig', 'ImplicityWaitTime')
        return float(value)

    def wait_until_timeout(self):
        value = self.config.get('TimeConfig', 'WaitUntilTimeout')
        return float(value)

    def wait_until_not_timeout(self):
        value = self.config.get('TimeConfig', 'WaitUntilNotTimeout')
        return float(value)

    def wait_frequency(self):
        value = self.config.get('TimeConfig', 'WaitFrequency')
        return float(value)

    # **************************** TestFrameworkConfig ***************************
    def exception_screenshot(self):
        value = self.config.get('TestFramework', 'ExceptionScreenshot')
        value = True if value != 'False' else False
        return value

    def testcase_fail_rerun(self):
        value = self.config.get('TestFramework', 'TestcaseFailRerun')
        value = eval(value)
        if not isinstance(value, bool) and not isinstance(value, int):
            value = False
        elif value is True:
            value = 3
        return value

    # **************************** BrowserRunnerConfig ****************************
    def browser_name(self):
        value = self.config.get('BrowserRunner', 'BrowserName')
        return value

    def browser_window_size(self):
        value = self.config.get('BrowserRunner', 'BrowserWindowSize')
        return value

    # ******************************* TestInfoConfig ******************************
    def html_report_switch(self):
        value = self.config.get('TestInfo', 'HtmlReportSwitch')
        value = True if value != 'False' else False
        return value

    def html_report_title(self):
        value = self.config.get('TestInfo', 'HtmlReportTitle')
        return value

    def html_report_description(self):
        value = self.config.get('TestInfo', 'HtmlReportDescription')
        return value

    def html_report_tester(self):
        value = self.config.get('TestInfo', 'HtmlReportTester')
        return value


parseConfig = ParseConfig()

CONSOLE_LOG_SWITCH = parseConfig.console_log_switch()
CONSOLE_LOG_LEVEL = parseConfig.console_log_level()
FILE_LOG_SWITCH = parseConfig.file_log_switch()
FILE_LOG_LEVEL = parseConfig.file_log_level()

IMPLICITY_WAIT_TIME = parseConfig.implicity_wait_time()
WAIT_UNTIL_TIMEOUT = parseConfig.wait_until_timeout()
WAIT_UNTIL_NOT_TIMEOUT = parseConfig.wait_until_not_timeout()
WAIT_FREQUENCY = parseConfig.wait_frequency()

EXCEPTION_SCREENSHOT = parseConfig.exception_screenshot()
TEST_CASE_FAIL_RERUN = parseConfig.testcase_fail_rerun()

BROWSER_NAME = parseConfig.browser_name()
BROWSER_WINDOW_SIZE = parseConfig.browser_window_size()

HTML_REPORT_SWITCH = parseConfig.html_report_switch()
HTML_REPORT_TITLE = parseConfig.html_report_title()
HTML_REPORT_DESCRIPTION = parseConfig.html_report_description()
HTML_REPORT_TESTER = parseConfig.html_report_tester()


if __name__ == '__main__':
    pass
