#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Paths import RESULTS_LOGS_DIR, FRAME_CONFIG_FILE_PATH
from logging.handlers import TimedRotatingFileHandler
from configparser import ConfigParser
import logging
import time
import os

try:
    config = ConfigParser()
    config.read(FRAME_CONFIG_FILE_PATH)
    _console_switch = config.get('LogConfig', 'ConsoleSwitch')
    ConsoleSwitch = True if _console_switch != 'False' else False
    _file_switch = config.get('LogConfig', 'FileSwitch')
    FileSwitch = True if _file_switch != 'False' else False
    ConsoleLevel = config.get('LogConfig', 'ConsoleLevel')
    FileLevel = config.get('LogConfig', 'FileLevel')
except Exception as e:
    print('[FrameConfig.ini] read error: {0}'.format(e))
    ConsoleSwitch = True
    FileSwitch = True
    ConsoleLevel = 'INFO'
    FileLevel = 'DEBUG'


class Logger:
    def __init__(self, logger_name=__name__):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        now_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        self.log_file_name = '{0}.log'.format(now_time)
        if not os.path.exists(RESULTS_LOGS_DIR):
            os.makedirs(RESULTS_LOGS_DIR)
        self.log_file_path = os.path.join(RESULTS_LOGS_DIR, self.log_file_name)
        self.formatter = logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s')
        self.console_output_level = ConsoleLevel
        self.file_output_level = FileLevel
        self.backup_count = 20

    def get_logger(self, console_switch=ConsoleSwitch, file_switch=FileSwitch):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:
            if console_switch:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(self.console_output_level)
                console_handler.setFormatter(self.formatter)
                self.logger.addHandler(console_handler)
            if file_switch:
                file_handler = TimedRotatingFileHandler(filename=self.log_file_path, when='D', interval=1,
                                                        backupCount=self.backup_count, delay=True, encoding='utf-8')
                file_handler.setLevel(self.file_output_level)
                file_handler.setFormatter(self.formatter)
                self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()


if __name__ == '__main__':
    logger.info('hello world')
