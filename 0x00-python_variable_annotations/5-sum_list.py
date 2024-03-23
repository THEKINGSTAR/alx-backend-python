#!/usr/bin/env python3
"""
5. Complex types - list of floats
a type-annotated function sum_list
which takes a list input_list of floats
as argument
and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    takes a list input_list of floats
    as argument
    and returns their sum as a float.
    """
    list_sum = 0
    list_sum = float(list_sum)
    for i in input_list:
        list_sum += i

    return list_sum
