from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two smallest values in list L.
    >>> items = [2,2,3,6,7,9]
    >>> find_two_smallest(items)
    (0, 1)
    >>> items == [2,2,3,6,7,9]
    True
    """
    # Find the index of the minimum and remove that item
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)
    
    # Find the index of the new minimum
    next_smallest = min(L)
    min2 = L.index(next_smallest)
    
    # Put smallest back into L
    L.insert(min1, smallest)
    
    # Fix min2 in case it was affected by the removal and reinsertion:
    if min1 <= min2: 
        min2 = min2 + 1
        # min2 += 1 # this is the same as the sentence above

    return (min1, min2)

print(find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476]))

if __name__ == '__main__': 
    # print('doctest is being executed')
    import doctest
    doctest.testmod()