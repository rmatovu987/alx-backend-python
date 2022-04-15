#!/usr/bin/env python3
"""
Annotate the function’s parameters and return values with the appropriate types
"""
from typing import Sequence, List, Tuple, Iterable


typeAlias = List[Tuple[Sequence, int]]


def element_length(lst: Iterable[Sequence]) -> typeAlias:
    """returns values with appropriate types"""
    return [(i, len(i)) for i in lst]
