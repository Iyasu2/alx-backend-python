#!/usr/bin/env python3
'''
this module
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    async function
    '''
    loop = asyncio.get_running_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
