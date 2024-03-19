#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

"""
bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
"""
