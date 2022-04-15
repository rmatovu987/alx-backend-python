#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a list input_list of floats as
argument and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of argument list elements"""
    total: float = 0.0
    for i in range(len(input_list)):
        total = total + input_list[i]
    return total
