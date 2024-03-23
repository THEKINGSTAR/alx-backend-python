#!/usr/bin/env python3
"""
Annotate the below function’s parameters
and
return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""


from typing import Callable
from typing import overload
from typing import Tuple
from typing import Union
from typing import Iterable
from typing import Sequence
from typing import List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the function’s parameters
    and
    return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
