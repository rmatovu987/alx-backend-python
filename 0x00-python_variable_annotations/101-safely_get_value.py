#!/usr/bin/env python3
"""
Given the parameters and the return values, add type annotations to function

Hint: look into TypeVar
"""
from typing import TypeVar, Any, Union, Mapping


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """return key if key is in dict else default"""
    if key in dct:
        return dct[key]
    else:
        return default
