#!/usr/bin/env python3
"""
0. The basics of async
asynchronous coroutine takes in an integer argument
and eventually returns it.
"""


import asyncio
import random


async def wait_random(max_delay=10):
    """
    asynchronous coroutine that takes in an integer argument
    """

    await asyncio.sleep(random.uniform(0, max_delay))
    return (round(random.uniform(0, max_delay), 15))
