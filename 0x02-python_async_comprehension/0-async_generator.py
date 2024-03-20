#!/usr/bin/env python3
"""
0. Async Generator
"""


import asyncio
import random


async def async_generator():
    """
    coroutine will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    Using the random module
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
