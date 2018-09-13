#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.ParseConfig import parseConfig
from Utils.Logger import logger
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import sys

exception_screenshot = parseConfig.exception_screenshot()
fail_rerun = parseConfig.testcase_fail_rerun()


def logger_caller(cls):
    """装饰类，添加日志，记录调用的方法"""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, attr):
            logger.debug('Call: {0} >> {1}'.format(cls.__name__, attr))
            method = getattr(self.wrapped, attr)
            return method
    return Wrapper


def logger_browser():
    """
    装饰Browser类中的实例方法，添加日志，记录调用的方法和调用的结果
    如果是指定异常，则不抛出错误只记录日志，否则抛出
    无法装饰静态方法和类方法，因为类名是从*args中取的第一个参数
    """
    def wrapper(func):
        def on_call(*args, **kwargs):
            _cls_name = args[0].__class__.__name__
            _met_name = func.__name__
            try:
                result = func(*args, **kwargs)
                if result is not None:
                    logger.debug('[Call]: {0} >> {1} [Return]: {2}'.format(_cls_name, _met_name, result))
                else:
                    logger.debug('[Call]: {0} >> {1}'.format(_cls_name, _met_name))
                return result
            except WebDriverException as e:
                exc_type, _, _ = sys.exc_info()
                logger.error('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
                raise
            except Exception:
                logger.exception('[UnwantedException]:')
                raise
        return on_call
    return wrapper


def logger_wait():
    """专门用来装饰Src中的Wait类"""
    def wrapper(func):
        def on_call(*args, **kwargs):
            _cls_name = args[0].__class__.__name__
            _met_name = func.__name__
            try:
                result = func(*args, **kwargs)
                _result = True if result else False
                logger.debug('[Call]: {0} >> {1} [Return]: {2}'.format(_cls_name, _met_name, _result))
                return result
            except TimeoutException as e:
                logger.warning('[TimeoutException]: {0}'.format(e).rstrip())
            except WebDriverException as e:
                exc_type, _, _ = sys.exc_info()
                logger.error('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
                raise
            except Exception:
                logger.exception('[UnwantedException]:')
                raise
        return on_call
    return wrapper


def logger_element():
    """专门用来装饰Src中的Element类"""
    def wrapper(func):
        def on_call(*args, **kwargs):
            _cls_name = args[0].__class__.__name__
            _met_name = func.__name__
            _element_name = args[0].name
            try:
                result = func(*args, **kwargs)
                if result is not None:
                    logger.debug('[Call]: {0} >> {1} >> {2} [Return]: {3}'.format(_cls_name, _met_name, _element_name, result))
                else:
                    logger.debug('[Call]: {0} >> {1} >> {2}'.format(_cls_name, _met_name, _element_name))
                return result
            except NoSuchElementException:
                logger.error('[NoSuchElementException]: Fail to locate element {0}'.format(_element_name))
            except WebDriverException as e:
                exc_type, _, _ = sys.exc_info()
                logger.error('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
                raise
            except Exception:
                logger.exception('[UnwantedException]:')
                raise
        return on_call
    return wrapper


def wrapped_unittest_assertion(func):
    """用来装饰PUnittest类中所有的AssertXxx方法"""
    def wrapper(*args, **kwargs):
        try:
            logger.debug('[Assert]: {0} >> {1}'.format(func.__name__, format(args[1:])))
            return func(*args, **kwargs)
        except AssertionError as e:
            args[0].Exc_Stack.append(e)
    return wrapper


def wrapped_testcase(screenshot=exception_screenshot, rerun=fail_rerun):
    """用来装饰所有的测试用例，提供失败后截图和失败后重跑功能"""
    def wrapper(func):
        def on_call(*args, **kwargs):
            # 失败重跑次数
            if rerun is False:
                rerun_time = 1
            elif isinstance(rerun, int):
                rerun_time = rerun
            else:
                rerun_time = 3
            # _browser是获取测试用例实例的browser属性，因为跨越了xxxPage属性层，所以用到了循环
            _testcase_name = args[0]._testMethodName
            _testclass_name = args[0].__class__.__name__
            _browser = None
            for attr in dir(args[0]):
                if hasattr(getattr(args[0], attr), 'browser'):
                    _browser = getattr(getattr(args[0], attr), 'browser')
                    break
            # 循环执行测试用例
            _rerun_time = rerun_time
            while rerun_time > 0:
                try:
                    logger.info((' TestRunNo: >> {0} '.format(_rerun_time - rerun_time + 1)).center(100, '-'))
                    result = func(*args, **kwargs)
                    # 用例执行完毕抛出所有可能存在的AssertionError异常
                    args[0].raise_exc()
                    logger.info(' TestResult: '.center(100, '-'))
                    logger.info('[TestSuccess]: {0} >> {1} '.format(_testclass_name, _testcase_name))
                    return result
                except Exception:
                    if screenshot:
                        _filename = 'Error_' + _testcase_name
                        _browser.take_screenshot(_filename)
                    rerun_time -= 1
                    if rerun_time == 0:
                        exc_type, exc_msg, _ = sys.exc_info()
                        logger.info(' TestResult: '.center(100, '-'))
                        logger.error('[TestFail]: {0}: {1}'.format(exc_type.__name__, exc_msg))
                        raise
        return on_call
    return wrapper


if __name__ == '__main__':
    pass
