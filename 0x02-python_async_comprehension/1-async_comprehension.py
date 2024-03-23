#!/usr/bin/env python3
"""
1. Async Comprehensions
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers
    using an async comprehension
    over async_generator,
    then returns the 10 random numbers.
    """
    collected_numbers = []
    async for num in async_generator():
        collected_numbers.append(num)
        if len(collected_numbers) == 10:
            break
    return collected_numbers
