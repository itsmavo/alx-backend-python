#!/usr/bin/env python3
''' Task 1 '''

from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    ''' Creates a list of 10 nums from generator '''
    return [num async for num in async_generator()]


