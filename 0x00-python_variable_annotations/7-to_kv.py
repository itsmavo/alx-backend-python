#!/usr/bin/python3
''' Task 7 '''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' takes key & value to a tuple of the key and value squared '''
    return (k, float(v**2))
