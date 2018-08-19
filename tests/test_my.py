#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 jack <jack@vps01-e1>
#
# Distributed under terms of the MIT license.

"""
test my
"""

from my import my_square

def test_my_square():
    assert my_square(1) == 1
    assert my_square(2) == 4
    assert my_square(3) == 9

