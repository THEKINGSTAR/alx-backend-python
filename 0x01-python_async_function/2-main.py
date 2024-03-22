#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
"""
bob@dylan:~$ ./2-main.py
1.759705400466919
"""
