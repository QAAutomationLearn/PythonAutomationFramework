#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.ParseTestSet import get_test_set
from Src.Engine import ENGINE
import unittest

try:
    ENGINE.launch_local_browser()
    test_set = get_test_set()
    runner = unittest.TextTestRunner()
    runner.run(test_set)
finally:
    ENGINE.quit_browser()
