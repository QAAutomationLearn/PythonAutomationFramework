#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Src.PUnittest import PUnittest


class TestDemo01(PUnittest):

    def test_articles_title(self):
        self.assertTrue(1 != 2)

    def test02(self):
        self.assertEqual(1, 2)


class TestDemo02(PUnittest):

    def test_training_title(self):
        [].index(2)
        self.assertTrue(1 != 2)

    def test_articles_title(self):
        self.assertEqual(1, 2)
        self.assertEqual(2, 3)
        self.assertEqual(1, 1)
