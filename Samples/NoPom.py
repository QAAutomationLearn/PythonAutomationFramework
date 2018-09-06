#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Paths import CHROME_DRIVER_PATH
from Utils.Logger import logger
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

logger.info('测试开始')

# 实例浏览器对象，并打开浏览器
logger.info('初始化浏览器')
driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.implicitly_wait(5)

try:
    # logger.info('最大化浏览器')
    # driver.maximize_window()
    logger.info('前往 https://www.utest.com/articles')
    driver.get('https://www.utest.com/articles')
    time.sleep(2)

    # 这里有个问题，网页会根据浏览器当前尺寸而决定左侧导航栏是否展开。为了兼容展开和不展开2种情况，
    # 必须要在代码里做判断：判断依据是body里面的class属性如果navigator是关闭的，body的class属性值
    # 是loading-indicator-enabled，否则是loading-indicator-enabled nav-menu-open。所以用
    #  try...except...语句来判断是可行的

    logger.info('验证导航栏是否展开')
    try:
        driver.find_element_by_css_selector('.nav-menu-open')
    # 这里需要指定异常类型，不然如果捕获到别的异常，会影响判断结果
    except NoSuchElementException:
        logger.info('导航栏没有展开，搜索并定义左侧导航栏展开按钮')
        element_navigator_expand_button = driver.find_element_by_class_name('hamburger')
        time.sleep(2)
        logger.info('点击按钮，展开导航栏')
        element_navigator_expand_button.click()
        time.sleep(2)

    logger.info('搜索并定义左侧导航栏的分页面按钮')
    element_articles_button = driver.find_element_by_partial_link_text('Articles')
    element_training_button = driver.find_element_by_partial_link_text('Training')
    element_forums_button = driver.find_element_by_partial_link_text('Forums')
    element_tools_button = driver.find_element_by_partial_link_text('Tools')
    element_projects_button = driver.find_element_by_partial_link_text('Projects')

    element_button_text = {
        element_articles_button: 'Software Testing Articles',
        element_training_button: 'Software Testing Courses',
        element_forums_button: 'Software Testing Forums',
        element_tools_button: 'Software Testing Tool Reviews',
        element_projects_button: 'Project Board'
    }

    for element_button, text in element_button_text.items():
        logger.info('-' * 80)
        logger.info('验证导航栏是否展开')
        try:
            driver.find_element_by_css_selector('.nav-menu-open')
        except NoSuchElementException:
            logger.info('导航栏没有展开，搜索并定义左侧导航栏展开按钮')
            element_navigator_expand_button = driver.find_element_by_class_name('hamburger')
            time.sleep(2)
            logger.info('点击按钮，展开导航栏')
            element_navigator_expand_button.click()
            time.sleep(2)
        logger.info('点击左侧导航栏上的子页面按钮')
        element_button.click()
        time.sleep(2)
        logger.info('搜索并定义子页面的title标签')
        element_title_label = driver.find_element_by_class_name('section-title')
        logger.info('验证Title标签中的文本{}是否正确'.format(element_title_label.text))
        assert element_title_label.text == text
        time.sleep(2)

        logger.info('测试通过')

except Exception:
    raise

finally:
    logger.info('关闭浏览器')
    driver.quit()
    logger.info('测试结束')
