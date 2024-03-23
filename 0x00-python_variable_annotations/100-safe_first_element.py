#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
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


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Augment the following code with the correct duck-typed annotations:
    # The types of the elements of the input are not knows
    """
    if lst:
        return lst[0]
    else:
        return None
