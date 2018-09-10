#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Paths import FRAME_CONFIG_FILE_PATH
from Utils.Logger import logger
from configparser import ConfigParser


class ParseConfig:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(FRAME_CONFIG_FILE_PATH)

    def log_config(self, setting_name):
        try:
            return self.config.get('LogConfig', setting_name)
        except Exception as e:
            logger.exception('[Exception]:', exc_info=True)
            raise e

    def time_config(self, setting_name):
        try:
            value = self.config.get('TimeConfig', setting_name)
            return float(value)
        except Exception as e:
            logger.exception('[Exception]:', exc_info=True)
            raise e


parseConfig = ParseConfig()

if __name__ == '__main__':
    print(parseConfig.time_config('ImplicityWaitTime'))