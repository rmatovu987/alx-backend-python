#!/usr/bin/env python3
"""
type-annotated function floor which takes a float n as argument and returns
the floor of the float
"""
import math


def floor(n: float) -> int:
    """return floor of argument"""
    res = math.floor(n)
    return res
