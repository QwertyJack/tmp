#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 jack <jack@vps01-e1>
#
# Distributed under terms of the MIT license.

"""
This example shows how to write tests in pytest style,
which is very flexible and convenient for function level test.
"""

from my import my_square


def test_my_square():
    """Simple test for function `my_square`"""
    assert my_square(1) == 1


def test_bool():
    """Test predicateds"""
    assert True


def test_null():
    """Test object is not None

    Because `[]` is False, thus `assert []` fails.
    """
    assert [my_square]
