#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Paths import TEST_DATA_FILE_PATH
from Utils.Logger import logger
import csv
import re

class ParseTestData:
    def __init__(self):
        try:
            with open(TEST_DATA_FILE_PATH, 'r', encoding='utf-8') as f:
                self.data = list(csv.reader(f))
        except Exception as e:
            logger.error('Fail to parse TestData: {0}'.format(e))
            raise e

    def get_test_data(self, pattern):
        try:
            pat = re.compile(pattern, re.IGNORECASE)
            data_list = list(filter(lambda li: re.search(pat, li[0]) is not None, self.data))
            return data_list
        except Exception:
            return []


if __name__ == '__main__':
    a = ParseTestData()
    print(a.get_test_data('sucCe'))
