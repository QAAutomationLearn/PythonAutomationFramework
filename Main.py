#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Src.Browser import Browser
from Src.Element import Element
from Src.Wait import Wait
from selenium import webdriver
from Utils.Paths import CHROME_DRIVER_PATH
from Utils.Logger import logger


try:
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    browser = Browser(driver)
    browser.navigate_to('https://www.zhihu.com')
    browser.maximize_window()
    title = browser.get_title()

    locator = ('xpath', "//input[@placeholder='手机号']")
    Element(driver, 'mobilephone_textbox', locator).click()
    Element(driver, 'mobilephone_textbox', locator).send_keys('123456798')
    Element(driver, 'mobilephone_textbox', locator).clear()

    locator = ('xpath', "//input[@placeholder='123']")
    Wait(driver).element_not_visible(locator)
    Element(driver, 'mobilephone_textbox', locator).click()

except Exception as e:
    logger.error(e)
finally:
    browser.quit()
