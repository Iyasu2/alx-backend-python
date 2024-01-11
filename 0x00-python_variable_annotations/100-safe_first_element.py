#!/usr/bin/env python3
'''
this module contains the sum_mixed_list function
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    function
    '''
    if lst:
        return lst[0]
    else:
        return None
