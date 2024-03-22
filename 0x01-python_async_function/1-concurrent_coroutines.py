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


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Execute multiple coroutines concurrently.
    This function spawns `n` coroutines
    of `wait_random` with the specified `max_delay`.
    Args:
        n: The number of coroutines to spawn.
        max_delay: The maximum delay for each coroutine.
    Returns:
        A list of delays (float values) in ascending order.
    """

    """
    delay_list = []
    # delay_list = [await wait_random(max_delay) for _ in range(n)]
    for i in range(n):
        corotine = await wait_random(max_delay)
        delay_list.append(corotine)
    return sorted(delay_list)
    """
    delay_tasks = [wait_random(max_delay) for _ in range(n)]
    delay_list = await asyncio.gather(* delay_tasks)
    return sorted(delay_list)
