#!/usr/bin/env python3
'''
this module contains the sum_mixed_list function
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    function
    '''
    return [(i, len(i)) for i in lst]
