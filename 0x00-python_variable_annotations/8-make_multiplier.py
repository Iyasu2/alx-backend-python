#!/usr/bin/env python3
'''
this module contains the sum_mixed_list function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    first function
    '''
    def multiplier_function(number: float) -> float:
        '''
        second function
        '''
        return number * multiplier
    return multiplier_function
