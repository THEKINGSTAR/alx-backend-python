#!/usr/bin/env python3
"""
1. Async Comprehensions
"""


import asyncio
from typing import List


generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine will collect 10 random numbers
    using an async comprehensing
    over async_generator,
    then return the 10 random numbers.
    """
    tasks = [generator() async for _ in range(10)]
    result = await asyncio.gather(*tasks)
    return result
