#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 jack <jack@vps01-e1>
#
# Distributed under terms of the MIT license.

"""
This example shows how to write tests in unittest style with test suite.
"""

import unittest

from .test_my_unit import TestMy


def suite():
    suite = unittest.TestSuite()
    suite.add(TestMy('test_my_square'))
    suite.add(TestMy('test_another'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
