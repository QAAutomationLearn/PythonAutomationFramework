#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Paths import ELEMENT_LOCATOR_FILE_PATH
import json


class ParseLocator:

    def __init__(self):
        self.element_locator = None
        with open(ELEMENT_LOCATOR_FILE_PATH, "r", encoding="utf-8") as r:
            self.element_locator = json.load(r)

    @staticmethod
    def _get_value(dic, key_path):
        """
        根据key的路径，递归获取其在字典中的value。
        :param dic: 字典
        :param key_path: 以[key, subkey, sub2key] 形式显示的列表
        :return: 路径对应的value
        """
        def rec(r_dic, r_key_path, value):
            for key in r_key_path:
                if key not in r_dic.keys():
                    value = []
                elif len(r_key_path) > 1:
                    r_key_path.pop(0)
                    rec(r_dic[key], r_key_path, value)
                else:
                    value.append(r_dic[key])
            return value[0]
        return rec(dic, key_path, [])

    def get_locator(self, element_path):
        """
        根据元素路径在Json文件中查到其相应的值
        :param element_path: 页面资源在Json文件中的路径，key.subkey 形式的字符串
        :return: 资源的值
        """
        key_path = element_path.split(".")
        locator = ParseLocator._get_value(self.element_locator, key_path)
        return (locator[0], locator[1]) if isinstance(locator, list) and len(locator) == 2 else None

if __name__ == "__main__":
    parseLocator = ParseLocator()
    print(parseLocator.get_locator('NavigateBar.navigate_bar'))
