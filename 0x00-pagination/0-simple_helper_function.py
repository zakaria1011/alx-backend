#!/usr/bin/env python3
""" pagination"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ indexing item in page"""
    start_index = (page-1)*(page_size)
    end_index = start_index + page_size
    return (start_index, end_index)
