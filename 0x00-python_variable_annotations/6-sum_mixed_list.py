#!/usr/bin/env python3
''' Task 6 '''

from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    ''' sum of list of ints and floating-point numbers '''
    return float(sum(mxd_list))
