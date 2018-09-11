#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Page.NavigateBar import NavigateBar
from Page.HomePage import HomePage
from Utils.Paths import CHROME_DRIVER_PATH
from selenium import webdriver
import time


# 初始化driver，初始化各个页面类
driver = webdriver.Chrome(CHROME_DRIVER_PATH)
homePage = HomePage(driver)
navigateBar = NavigateBar(driver)

# 前往网站
homePage.browser.navigate_to('https://www.utest.com/articles')

# 检测左侧导航栏是否可见，如果不可见点击展开按钮将其展开
navigate_bar_visible = navigateBar.navigate_bar().is_displayed()
if not navigate_bar_visible:
    homePage.expand_navigate_button().click()

# 点击导航栏分页面按钮并验证分页面的显示是否正确
navigateBar.articles_button().click()
time.sleep(2)
title_label_text = homePage.title_label().get_text()
assert title_label_text == 'Software Testing Articles'

# 再依次操作其余4个按钮
navigate_bar_visible = navigateBar.navigate_bar().is_displayed()
if not navigate_bar_visible:
    homePage.expand_navigate_button().click()
navigateBar.training_button().click()
time.sleep(2)
title_label_text = homePage.title_label().get_text()
assert title_label_text == 'Software Testing Courses'

navigate_bar_visible = navigateBar.navigate_bar().is_displayed()
if not navigate_bar_visible:
    homePage.expand_navigate_button().click()
navigateBar.forums_button().click()
time.sleep(2)
title_label_text = homePage.title_label().get_text()
assert title_label_text == 'Software Testing Forums'

navigate_bar_visible = navigateBar.navigate_bar().is_displayed()
if not navigate_bar_visible:
    homePage.expand_navigate_button().click()
navigateBar.tools_button().click()
time.sleep(2)
title_label_text = homePage.title_label().get_text()
assert title_label_text == 'Software Testing Tool Reviews'

navigate_bar_visible = navigateBar.navigate_bar().is_displayed()
if not navigate_bar_visible:
    homePage.expand_navigate_button().click()
navigateBar.projects_button().click()
time.sleep(2)
title_label_text = homePage.title_label().get_text()
assert title_label_text == 'Project Board'

# 退出浏览器
homePage.browser.quit()
