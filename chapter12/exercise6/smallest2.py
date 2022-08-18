from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.
    >>> items = [2,2,3,6,7,9]
    >>> find_two_smallest(items)
    (0, 1)
    >>> items == [2,2,3,6,7,9]
    True
    """
    # Get a sorted copy of the list so that the two smallest items are at the # front
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]
    
    # Find the indices in the original list L
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)
    
    return (min1, min2)

print(find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476]))

if __name__ == '__main__': 
    # print('doctest is being executed')
    import doctest
    doctest.testmod()