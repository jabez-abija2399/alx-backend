#!/usr/bin/env python3
""" Simple helper function """
def index_range(page, page_size):
    """ return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters. """    
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size should be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index - 1  
