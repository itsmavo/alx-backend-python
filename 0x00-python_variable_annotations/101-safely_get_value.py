#!/usr/bin/env python3
''' Task 11 '''

from typing import Any, Mapping, Union, TypeVar


t = TypeVar('T')
Res = Union[Any, t]
Def = Union[t, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    ''' receives value from dict using a given key '''
    if key in dct:
        return dct[key]
    else:
        return default
