#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 jack <jack@vps01-e1>
#
# Distributed under terms of the MIT license.

"""
This example shows how to write integration test.

Run `pytest -m integ` to run integration test(s) only.
"""

import pytest

from my import my_square


@pytest.fixture
def data():
    return range(3)


@pytest.mark.integ
def test_integ_my(data):
    """An integration test

    Actually this is not an integration test; just an example instead.
    """
    assert sorted(map(my_square, data)) == sorted([0, 1, 4])
