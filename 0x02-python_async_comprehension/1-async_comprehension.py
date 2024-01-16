#!/usr/bin/env python3
'''
the module
'''
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''
    the function
    '''
    return [i async for i in async_generator()]
