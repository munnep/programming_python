from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """Return the index of the first occurrence of value in lst, or return -1 if value is not in lst.
        >>> linear_search([2, 5, 1, -3], 5)
        1
        >>> linear_search([2, 4, 2], 2)
        0
        >>> linear_search([2, 5, 1, -3], 4)
        -1
        >>> linear_search([], 5)
        -1
    """
    i = len(lst) - 1 #
    
    # Keep going until we reach the end of lst or until we find value.
    while i != 0 and lst[i] != value: 
        print(i)
        i=i-1
    
    # If we fell off the end of the list, we didn't find value.
    if i == -1: 
        return -1
    else:
        return i

print(linear_search([2, 5, 1, -3], 2))    