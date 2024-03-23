#!/usr/bin/env python3
"""
Basic annotations - concat
a type-annotated function concat that takes
a string
str1 and
a string
str2
as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    concat that takes a string
    str1 and a string str2
    as arguments
    and returns a concatenated string
    """
    concat_str = ''
    concat_str = str1 + str2
    return concat_str
