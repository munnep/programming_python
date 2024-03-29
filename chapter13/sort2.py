import bisect

def bin_sort(values: list) -> list:
    """Return a sorted version of the values. (This does not mutate values.) >>> L = [3, 4, 7, -1, 2, 5]
    >>> bin_sort(L)
    [-1, 2, 3, 4, 5, 7]
    """

    result = []
    for v in values:
        bisect.insort_left(result, v) 
    
    return result

print(bin_sort([9,3,5,1]))    