#!/usr/bin/env python3
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
"""
bob@dylan:~$ ./1-main.py
True
{'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
"""