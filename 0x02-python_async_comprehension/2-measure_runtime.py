#!/usr/bin/env python3
"""
Import async_comprehension from the previous file
and
write a measure_runtime coroutine that will
execute async_comprehension four times in parallel
using asyncio.gather.
measure_runtime should measure the total runtime
and
return it.
"""


import asyncio
import time
import random


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds,
    explain it to yourself.
    """
    start_time = time.time()
    await asyncio.gather(* (async_comprehension() for _ in range(4)))
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
