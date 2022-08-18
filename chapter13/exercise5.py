def bubble_sort(lst):
    """ (list) -> NoneType
    Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5] >>> bubble_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    >>> L = []
    >>> bubble_sort(L) >>> L
    []
    >>> L = [1]
    >>> bubble_sort(L) >>> L
    [1]
    >>> L = [2, 1]
    >>> bubble_sort(L) >>> L
    [1, 2]
    >>> L = [1, 2]
    >>> bubble_sort(L) >>> L
    [1, 2]
    >>> L = [3, 3, 3]
    >>> bubble_sort(L) >>> L
    [3, 3, 3]
    >>> L = [-5, 3, 0,
    >>> bubble_sort(L)
    >>> L
    [-6, -5, 0, 1, 1, 2, 3, 3] 
    """
    # The end of the unsorted section. The largest item will be placed here. 
    end = len(lst) - 1
    # Keep going until there are either 0 or 1 items to consider. 
    # # (The 0 case is for the empty list.)
    while end > 0:
        print(lst)
    # sweep through the list. 
        for i in range(0, end):
            if lst[i] > lst[i + 1]:
                 tmp = lst[i + 1] 
                 lst[i + 1] = lst[i] 
                 lst[i] = tmp
        end = end - 1

L = [6, 5, 4, 3, 7, 1, 2]

bubble_sort(L)
print(L)