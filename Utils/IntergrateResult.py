#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Logger import logger
from Utils.Paths import *
import time
import shutil
import os


now_date = time.strftime("%Y-%m-%d")
backup_date_path = os.path.join(BACKUP_DIR, now_date)
backup_logs_path = os.path.join(backup_date_path, "Logs")
backup_reports_path = os.path.join(backup_date_path, "Reports")
backup_screenshots_path = os.path.join(backup_date_path, "Screenshots")


def init_backup_folders():
    logger.info("Initialize Backup and inner folders")
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)
    if not os.path.exists(backup_date_path):
        os.mkdir(backup_date_path)
    if not os.path.exists(backup_logs_path):
        os.mkdir(backup_logs_path)
    if not os.path.exists(backup_reports_path):
        os.mkdir(backup_reports_path)
    if not os.path.exists(backup_screenshots_path):
        os.mkdir(backup_screenshots_path)


def init_results_folders():
    logger.info("Initialize Results and inner folders")
    if not os.path.exists(RESULTS_DIR):
        os.mkdir(RESULTS_DIR)
    if not os.path.exists(RESULTS_LOGS_DIR):
        os.mkdir(RESULTS_LOGS_DIR)
    if not os.path.exists(RESULTS_REPORTS_DIR):
        os.mkdir(RESULTS_REPORTS_DIR)
    if not os.path.exists(RESULTS_SCREENSHOTS_DIR):
        os.mkdir(RESULTS_SCREENSHOTS_DIR)


def backup_results(file_type, results_folder_path, target_folder_path):
    for root, dirs, files in os.walk(results_folder_path):
        for file in files:
            if file.split(".")[1] == file_type:
                file_path = os.path.join(results_folder_path, file)
                target_path = os.path.join(target_folder_path, file)
                # 如果有相同文件则覆盖
                if os.path.exists(target_path):
                    os.remove(target_path)
                shutil.copy(file_path, target_path)
    logger.info("Backup {0}".format(results_folder_path))
    shutil.rmtree(results_folder_path, ignore_errors=True)


def integrate_results():
    try:
        init_backup_folders()
        if os.path.exists(RESULTS_LOGS_DIR):
            backup_results("log", RESULTS_LOGS_DIR, backup_logs_path)
        if os.path.exists(RESULTS_REPORTS_DIR):
            backup_results("html", RESULTS_REPORTS_DIR, backup_reports_path)
        if os.path.exists(RESULTS_SCREENSHOTS_DIR):
            backup_results("png", RESULTS_SCREENSHOTS_DIR, backup_screenshots_path)
        init_results_folders()
    except Exception as e:
        logger.error("Fail to integrate former results: {0}".format(e))
        raise e


if __name__ == "__main__":
    integrate_results()
