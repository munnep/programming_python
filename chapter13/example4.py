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
    # Add the sentinel.
    lst.append(value)
    i=0
    # Keep going until we find value.
    while lst[i] != value: 
        i=i+1
    

    print('with value added: ', lst)
    # Remove the sentinel.
    lst.pop()    
    print('with value removed: ', lst)        
    # If we reached the end of the list we didn't find value.
    if i == len(lst): 
        return -1
    else:
        return i


print(linear_search([2, 5, 1, -3], 5))    