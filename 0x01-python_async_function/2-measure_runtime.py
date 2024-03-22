#!/usr/bin/env python3
"""
a measure_time function with integers n and max_delay
as arguments that measures the total execution time
for wait_n(n, max_delay), and returns total_time / n.
Your function should return a float.
Use the time module to measure an approximate elapsed time.
"""


import asyncio
import random
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function with integers
    n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    Your function should return a float.
    """
    start_time = time.time()
    wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n
