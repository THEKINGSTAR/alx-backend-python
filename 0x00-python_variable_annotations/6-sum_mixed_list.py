#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list
which takes a list mxd_lst
of integers and floats
and
returns their sum as a float.
"""


from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list mxd_lst
    of integers and floats
    and
    returns their sum as a float.
    """
    list_sum = 0
    list_sum = float(list_sum)
    for i in mxd_lst:
        list_sum += i

    return list_sum
