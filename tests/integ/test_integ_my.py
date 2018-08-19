#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 jack <jack@vps01-e1>
#
# Distributed under terms of the MIT license.

"""
integration test
"""

import pytest

from my import my_square


@pytest.fixture
def data():
    return range(3)


@pytest.mark.integ
def test_integ_my(data):
    """actually this is a unit test instead of an integration test"""
    assert sorted(map(my_square, data)) == sorted([0, 1, 4])
