#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
"""
bob@dylan:~$ ./9-main.py 
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
"""