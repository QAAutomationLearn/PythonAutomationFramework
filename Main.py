#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.ParseConfig import HTML_REPORT_SWITCH, HTML_REPORT_TITLE
from Utils.ParseConfig import HTML_REPORT_DESCRIPTION, HTML_REPORT_TESTER
from Utils.ParseTestSet import get_test_set
from Utils.Paths import RESULTS_REPORTS_DIR
from Utils.HTMLTestRunner import HTMLTestRunner
from Utils.IntergrateResult import integrate_results
from Src.Engine import ENGINE
import unittest
import time
import os


def text_test_runner(test_suite):
    runner = unittest.TextTestRunner()
    runner.run(test_suite)


def html_test_runner(test_suite, report_title=HTML_REPORT_TITLE, report_description=HTML_REPORT_DESCRIPTION,
                     tester=HTML_REPORT_TESTER):
    now_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_name = "{0}_HtmlTestReport.html".format(now_time)
    full_report_name = os.path.join(RESULTS_REPORTS_DIR, report_name)
    with open(full_report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title=report_title, description=report_description, tester=tester)
        runner.run(test_suite)


def Main(html_report=HTML_REPORT_SWITCH):
    integrate_results()
    try:
        ENGINE.launch_local_browser()
        test_set = get_test_set()
        if html_report:
            html_test_runner(test_set)
        else:
            text_test_runner(test_set)
    finally:
        ENGINE.quit_browser()


if __name__ == '__main__':
    Main()
