#!/usr/bin/env python3
'''
this module contains the to_kv function
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    this is the to_kv function
    '''
    return k, float(v) ** 2
