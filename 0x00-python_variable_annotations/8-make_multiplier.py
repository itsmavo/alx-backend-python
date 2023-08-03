#!/usr/bin/python3

''' Task 8 '''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Multiplier function '''
    return lambda x: x * multiplier