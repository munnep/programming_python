from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.
    >>> items = [2,2,3,6,7,9]
    >>> find_two_smallest(items)
    (0, 2)
    >>> items == [2,2,3,6,7,9]
    True
    """
    # Set min1 and min2 to the indices of the smallest and next-smallest # values at the beginning of L
    if L[0] < L[1]:
        min1, min2 = 0, 1 
    else:
        min1, min2 = 1, 0
    # Examine each value in the list in order
    for i in range(2, len(L)):
    # L[i] is smaller than both min1 and min2, in between, or # larger than both
            # New smallest?
        if L[i] < L[min1]: 
            min2 = min1
            min1 = i
    
        # New second smallest?
        elif L[i] < L[min2]: 
            min2 = i
    
    return (min1, min2)

print(find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476]))

if __name__ == '__main__': 
    # print('doctest is being executed')
    import doctest
    doctest.testmod()