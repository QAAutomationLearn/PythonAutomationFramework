#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# ROOT DIR
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CONFIG DIR
CONFIG_DIR = os.path.join(ROOT_DIR, "Config")
FRAME_CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, 'FrameConfig.ini')
ELEMENT_LOCATOR_FILE_PATH = os.path.join(CONFIG_DIR, 'ElementLocator.json')
TESTCASE_LIST_FILE_PATH = os.path.join(CONFIG_DIR, 'TestCaseList.py')
TEST_DATA_FILE_PATH = os.path.join(CONFIG_DIR, 'TestData.csv')

# BACKUP DIR
BACKUP_DIR = os.path.join(ROOT_DIR, "Backup")

# RESULTS DIR
RESULTS_DIR = os.path.join(ROOT_DIR, "Results")
RESULTS_LOGS_DIR= os.path.join(RESULTS_DIR, "Logs")
RESULTS_REPORTS_DIR = os.path.join(RESULTS_DIR, "Reports")
RESULTS_SCREENSHOTS_DIR = os.path.join(RESULTS_DIR, "Screenshots")

# TESTSUIT DIR
TESTSUIT_DIR = os.path.join(ROOT_DIR, "TestSuite")

# DRIVER DIR
DRIVER_DIR = os.path.join(ROOT_DIR, "Drivers")
CHROME_DRIVER_PATH = os.path.join(DRIVER_DIR, "Chrome", "chromedriver.exe")
FIREFOX_DRIVER_PATH = os.path.join(DRIVER_DIR, "Firefox", "geckodriver.exe")
IE_DRIVER_PATH = os.path.join(DRIVER_DIR, "IE", "IEDriverServer.exe")


if __name__ == "__main__":
    print('root_path = {0}'.format(str(os.path.exists(ROOT_DIR))))
    print('config_path = {0}'.format(str(os.path.exists(CONFIG_DIR))))
    print('results_path = {0}'.format(str(os.path.exists(RESULTS_DIR))))
    print('log_file_path = {0}'.format(str(os.path.exists(RESULTS_LOGS_DIR))))
    print('report_file_path = {0}'.format(str(os.path.exists(RESULTS_REPORTS_DIR))))
    print('screenshots_path = {0}'.format(str(os.path.exists(RESULTS_SCREENSHOTS_DIR))))
    print('driver_path = {0}'.format(str(os.path.exists(DRIVER_DIR))))
    print('chrome_driver_path = {0}'.format(str(os.path.exists(CHROME_DRIVER_PATH))))
    print('firefox_driver_path = {0}'.format(str(os.path.exists(FIREFOX_DRIVER_PATH))))
    print('ie_driver_path = {0}'.format(str(os.path.exists(IE_DRIVER_PATH))))
    print('backup_path = {0}'.format(str(os.path.exists(BACKUP_DIR))))
