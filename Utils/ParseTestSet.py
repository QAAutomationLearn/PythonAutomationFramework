#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Config.TestCaseList import TEST_CASES_LIST
from Utils.Logger import logger
from importlib import import_module
import unittest
import argparse


# 解析命令行参数
parser = argparse.ArgumentParser(description='Organize Test Suite')

parser.add_argument(dest='args', metavar='args', nargs='*')
parser.add_argument('-cl', '--test_class_name', metavar='TestClassName',
                    dest='class_name', action='append',
                    help='Indicate test class name')
parser.add_argument('-ca', '--test_case_name', metavar='TestCaseName',
                    dest='case_name', action='append',
                    help='Indicate test case name')
parser.add_argument('-p', '--test_case_priority', metavar='TestCasePriority',
                    dest='priority', action='store',
                    help='Indicate test case priority')
args = parser.parse_args()

testClassName = args.class_name
testCaseName = args.case_name
testCasePriority = args.priority


def get_test_set(test_class=testClassName, test_case=testCaseName, priority=testCasePriority):
    # 过滤出想要的测试用例列表
    _test_case_list = TEST_CASES_LIST
    if test_class:
        _test_case_list = filter(lambda x: x[2] in testClassName, _test_case_list)
    if test_case:
        _test_case_list = filter(lambda x: x[3] in testCaseName, _test_case_list)
    if priority:
        _test_case_list = filter(lambda x: x[0] == testCasePriority, _test_case_list)
    _test_case_list = list(_test_case_list)

    try:
        test_set = unittest.TestSuite()
        for case in _test_case_list:
            # 根据文件名字符串导入相应的包
            package = import_module('TestSuite.{0}'.format(case[1]))
            # 根据包生成相应的类对象
            class_obj = getattr(package, case[2])
            # 根据类对象获取相应的测试用例
            _case = class_obj(case[3])
            # 将测试用例添加入测试套件
            test_set.addTest(_case)
        return test_set
    except Exception as e:
        logger.error("[Exception]: Make Test Suite Error: {0}".format(e))
        raise e


if __name__ == '__main__':
    pass
