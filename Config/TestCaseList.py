#!/usr/bin/env python3
# -*- coding: utf-8 -*-

TEST_CASES_LIST = [
    # 测试分页面跳转是否正确
    ("P0", "TestSubPageTitle", "TestSubPageTitle", "test_articles_title"),
    ("P3", "TestSubPageTitle", "TestSubPageTitle", "test_training_title"),
    ("P1", "TestSubPageTitle", "TestSubPageTitle", "test_forums_title"),
    ("P2", "TestSubPageTitle", "TestSubPageTitle", "test_tools_title"),
    ("P0", "TestSubPageTitle", "TestSubPageTitle", "test_projects_title"),

    # 待开发的测试用例
    ("P0", "TestDemo", "TestDemo01", "test_articles_title"),
    ("P1", "TestDemo", "TestDemo01", "test02"),

    # 待开发的测试用例
    ("P1", "TestDemo", "TestDemo02", "test_articles_title"),
    ("P1", "TestDemo", "TestDemo02", "test_training_title"),
]
