#!/usr/bin/env python3
'''
this module contains the sum_mixed_list function
'''
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''
    function
    '''
    return [(i, len(i)) for i in lst]
