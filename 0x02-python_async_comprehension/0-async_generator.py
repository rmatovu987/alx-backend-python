#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments
coroutine will loop 10 times, each time asynchronously wait 1 second, then
yield a random number between 0 and 10
use the random module
"""
import asyncio
import random
from typing import Generator
# from typing import Optional


# async def async_generator(arg: Optional[int] = None) -> float:
async def async_generator() -> Generator[float, None, None]:
    """returns random number between 0 and 10"""
    for i in range(10):
        yield (random.uniform(0, 10))
        await asyncio.sleep(1)
