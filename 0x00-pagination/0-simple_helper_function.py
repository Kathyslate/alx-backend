#!/usr/bin/env python3
"""
Defines the function `index_range` """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index"""
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
