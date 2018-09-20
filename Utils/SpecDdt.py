#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ddt


def mk_test_name_(name, value, index=0):
    index = "{0:0{1}}".format(index + 1, ddt.index_len)
    if not ddt.is_trivial(value):
        return "{0}_{1}".format(name, index)
    test_name = "{0}_{1}_{2}".format(name, index, value[0])
    return ddt.re.sub(r'\W|^(?=\d)', '_', test_name)
