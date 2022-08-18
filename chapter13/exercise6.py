def bubble_sort_2(lst):
    """ (list) -> NoneType
    Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5] 
    >>> bubble_sort_2(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    >>> L = []
    >>> bubble_sort_2(L) 
    >>> L
    []
    >>> L = [1]
    >>> bubble_sort_2(L) 
    >>> L
    [1]
    >>> L = [2, 1]
    >>> bubble_sort_2(L) 
    >>> L
    [1, 2]
    >>> L = [1, 2]
    >>> bubble_sort_2(L) 
    >>> L
    [1, 2]
    >>> L = [3, 3, 3]
    >>> bubble_sort_2(L) 
    >>> L
    [3, 3, 3]
    """
    beginning = 0
    # print('start')
    # Keep going until there is only one item to consider. 
    while beginning < len(lst):
        # print('while loop')
    # sweep through the list.
        for i in range(len(lst) - 1, beginning, -1):
               if lst[i] < lst[i - 1]: 
                   tmp = lst[i - 1]
                   lst[i - 1] = lst[i] 
                   lst[i] = tmp
    
        beginning = beginning + 1

L = [6, 5, 4, 3, 7, 1, 2]

bubble_sort_2(L)
print(L)

if __name__ == '__main__': 
    print('doctest')
    import doctest
    doctest.testmod()