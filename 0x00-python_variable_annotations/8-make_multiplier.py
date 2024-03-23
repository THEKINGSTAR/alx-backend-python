#!/usr/bin/env python3
"""
a type-annotated function make_multiplier
that takes a float multiplier as argument

and

returns a function
that multiplies a float by multiplier.
"""


from typing import Callable
from typing import overload
from typing import Tuple
from typing import Union


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument
    and
    returns a function
    that multiplies a float by multiplier.
    """
    def multiply(x: float) -> float:
        return (x * multiplier)

    return multiply
