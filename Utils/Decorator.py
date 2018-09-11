#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Logger import logger
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
import sys


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


def logger_browser(exc=WebDriverException):
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
            except exc as e:
                exc_type, _, _ = sys.exc_info()
                logger.warning('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
            except Exception:
                logger.exception('[UnwantedException]:')
                raise
        return on_call
    return wrapper


def logger_wait(exc=WebDriverException):
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
            except exc as e:
                exc_type, _, _ = sys.exc_info()
                logger.warning('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
            except Exception:
                logger.exception('[UnwantedException]:')
                raise
        return on_call
    return wrapper


def logger_element(exc=WebDriverException):
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
            except TimeoutException:
                logger.warning('[TimeoutException]: Fail to locate element {0}'.format(_element_name))
            except exc as e:
                exc_type, _, _ = sys.exc_info()
                logger.warning('[{0}]: {1}'.format(exc_type.__name__, e).rstrip())
            except Exception:
                logger.exception('[UnwantedException]:')
                raise
        return on_call
    return wrapper


if __name__ == '__main__':

    class TestClass:
        a = 'a'

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.deleg = Delegation()

        @property
        @logger_browser(exc=TypeError)
        def test_property(self):
            return self.a

        @classmethod
        @logger_browser(exc=TypeError)
        def test_class(cls, z):
            return cls.a * z

        @logger_browser(exc=TypeError)
        def test_method(self, z):
            return [z].index(2)

        @staticmethod
        @logger_browser(exc=(TypeError, ValueError))
        def test_static(x, y):
            return x * y


    class Delegation:

        @logger_browser(exc=(TypeError, ValueError))
        def delegation(self):
            return 'delegation'


    t = TestClass(1, 2)
    a = t.test_property
    t.test_static('a', 'b')
    t.deleg.delegation()
    t.test_class('a')
    t.test_method('a')