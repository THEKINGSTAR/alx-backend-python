#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code and apply any necessary changes.

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
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


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Use mypy to validate the following piece of code
    and
    apply any necessary changes.
    """
    zoomed_in: Tuple = [
    item for item in lst
    for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
