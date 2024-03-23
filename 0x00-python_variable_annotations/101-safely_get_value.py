#!/usr/bin/env python3
"""
Given the parameters and the return values,
add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""


from typing import Callable
from typing import overload
from typing import Tuple
from typing import Union
from typing import Iterable
from typing import Sequence
from typing import List
from typing import Any
from typing import NewType
from typing import Mapping
from typing import TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Augment the following code
    with the correct duck-typed annotations:
    # The types of the elements of the input are not knows
    """
    if key in dct:
        return dct[key]
    else:
        return default
