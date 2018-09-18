#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Decorator import wrapped_unittest_assertion
import unittest


class MetaDecorator(type):
    def __new__(mcs, cls_name, supers, cls_dict):
        for attr, val in cls_dict.items():
            if val.__class__.__name__ == 'function':
                if attr.startswith('assert'):
                    cls_dict[attr] = wrapped_unittest_assertion(val)
        return type.__new__(mcs, cls_name, supers, cls_dict)


class PUnittest(unittest.TestCase, metaclass=MetaDecorator):

    Exc_Stack = []

    def raise_exc(self):
        if self.Exc_Stack:
            exc_text = ', AssertionError: '.join(str(x) for x in self.Exc_Stack)
            self.Exc_Stack.clear()
            raise AssertionError(exc_text)

    def assertEqual(self, first, second, msg=None):
        super(PUnittest, self).assertEqual(first, second, msg=msg)

    def assertAlmostEqual(self, first, second, places=None, msg=None, delta=None):
        super(PUnittest, self).assertAlmostEqual(first, second, places=places, msg=msg, delta=delta)

    def assertDictEqual(self, d1, d2, msg=None):
        super(PUnittest, self).assertDictEqual(d1=d1, d2=d2, msg=msg)

    def assertFalse(self, expr, msg=None):
        super(PUnittest, self).assertFalse(expr, msg=msg)

    def assertTrue(self, expr, msg=None):
        super(PUnittest, self).assertTrue(expr, msg=msg)

    def assertIn(self, member, container, msg=None):
        super(PUnittest, self).assertIn(member, container, msg=msg)

    def assertIs(self, expr1, expr2, msg=None):
        super(PUnittest, self).assertIs(expr1, expr2, msg=msg)

    def assertIsInstance(self, obj, cls, msg=None):
        super(PUnittest, self).assertIsInstance(obj, cls, msg=msg)

    def assertIsNone(self, obj, msg=None):
        super(PUnittest, self).assertIsNone(obj, msg=msg)

    def assertNotIn(self, member, container, msg=None):
        super(PUnittest, self).assertNotIn(member, container, msg=msg)

    def assertNotEqual(self, first, second, msg=None):
        super(PUnittest, self).assertNotEqual(first, second, msg=msg)

    def assertGreater(self, a, b, msg=None):
        super(PUnittest, self).assertGreater(a, b, msg=msg)

    def assertLess(self, a, b, msg=None):
        super(PUnittest, self).assertLess(a, b, msg=msg)


if __name__ == '__main__':

    class MyTest(PUnittest):

        def test_equal(self):
            self.assertEqual(1, 2)
            self.assertEqual(1, 1)
            self.assertEqual(3, 1)
            self.assertEqual('s', 's')
            self.raise_exc()

        def test_in(self):
            self.assertIn(1, [1])
            self.assertIn(1, [2])
            self.assertIn('a', {'a': 1})
            self.assertIn('b', {'a': 1})
            self.raise_exc()

    unittest.main()
