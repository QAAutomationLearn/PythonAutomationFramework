#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Src.Browser import Browser
from selenium import webdriver
from Utils.Paths import CHROME_DRIVER_PATH
from Utils.Logger import logger


try:
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    browser = Browser(driver)
    browser.navigate_to('https://www.zhihu.com')
    browser.maximize_window()
    title = browser.get_title()
    el = browser.get_element(('class name', "SignFlowHomepage1"))
    el.click()
except Exception as e:
    logger.error(e)
finally:
    browser.quit()
