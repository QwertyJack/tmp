#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 jack <jack@vps01-e1>
#
# Distributed under terms of the MIT license.

"""
This example shows how to write tests in unittest style.
"""

import unittest

from my import my_square


class TestMy(unittest.TestCase):

    def setUp(self):
        print('Run setup before every test')

    def tearDown(self):
        print('Run teardown after test')

    def test_my_square(self):
        self.assertEqual(my_square(1), 1)
        self.assertEqual(my_square(2), 4)
        self.assertEqual(my_square(3), 9)

    def test_another(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
