def find_min(L: list, b: int) -> int: 
    """Precondition: L[b:] is not empty.
    Return the index of the smallest value in L[b:].
    >>> find_min([3, -1, 7, 5], 0)
    1
    >>> find_min([3, -1, 7, 5], 1)
    1
    >>> find_min([3, -1, 7, 5], 2)
    3
    """
    smallest = b # The index of the smallest so far. 
    i=b+1
    while i != len(L):
        if L[i] < L[smallest]:
    # We found a smaller item at L[i].
            smallest = i 
            
        i=i+1

    return smallest


def selection_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    i=0
    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i] 
        i=i+1


def insert(L: list, b: int) -> None: 
    """Precondition: L[0:b] is already sorted. Insert L[b] where it belongs in L[0:b + 1].
    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    >>> insert(L, 4)
    >>> L
    [-1, 2, 3, 4, 7, 5]
    """
    # Find where to insert L[b] by searching backwards from L[b] 
    # # for a smaller item.
    i=b
    while i != 0 and L[i - 1] >= L[b]:
        i=i-1
    
    # Move L[b] to index i, shifting the following values to the right.
    value = L[b]
    del L[b] 
    L.insert(i, value)


def insertion_sort(L: list) -> None:
    """Reorder the items in L from smallest to largest.
        >>> L = [3, 4, 7, -1, 2, 5]
        >>> insertion_sort(L)
        >>> L
        [-1, 2, 3, 4, 5, 7]
    """
    i=0
    # print(L)
    while i != len(L):
            # Insert L[i] where it belongs in L[0:i+1].
        insert(L, i)
        i=i+1

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
        # print(lst)
    # sweep through the list. 
        for i in range(0, end):
            if lst[i] > lst[i + 1]:
                 tmp = lst[i + 1] 
                 lst[i + 1] = lst[i] 
                 lst[i] = tmp
        end = end - 1