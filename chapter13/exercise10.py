def merge(L1: list, L2: list) -> list:
    """Merge sorted lists L1 and L2 into a new list and return that new list. 
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """
    
    newL = []
    i1 = 0
    i2 = 0
    # For each pair of items L1[i1] and L2[i2], copy the smaller into newL. 
    while not (i1 == len(L1) and i2 == len(L2)):
        if i2 == len(L2) or (i1 != len(L1) and L1[i1] <= L2[i2]):
            newL.append(L1[i1])
            i1 += 1 
        else:
            newL.append(L2[i2]) 
            i2 += 1
    
    return newL

print(merge([1,3,4],[3,4,5,6]))

