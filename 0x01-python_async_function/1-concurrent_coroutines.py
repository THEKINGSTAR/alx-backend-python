#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
Import wait_random from the previous python file
write an async routine called wait_n that
takes in 2 int arguments
(in this order): n and max_delay.
spawn wait_random n times with the specified max_delay.
"""


import asyncio
import random
import time


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency.
    """
    delay_list = []
    # delay_list = [await wait_random(max_delay) for _ in range(n)]
    for i in range(n):
        corotine = await wait_random(max_delay)
        delay_list.append(corotine)
    return sorted(delay_list)
