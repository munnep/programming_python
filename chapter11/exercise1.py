def find_dups(L):
    """ (list) -> set
    
    Return the number of duplicates numbers from L.
    
    >>> find_dups([1, 1, 2, 3, 4, 2])
    {1, 2}
    
    >>> find_dups([1, 2, 3, 4])
    set()
    """
    elem_set = set()
    dups_set = set()
    for entry in L:
        # print(elem_set)
        # print(dups_set)
        len_initial = len(elem_set)  # how long is the current set
        # print('length_before ', len_initial)
        elem_set.add(entry) # add the value.......if the value is already there it won't be added
        len_after = len(elem_set) # check the lenght again
        # print('length_after ', len_after)
        if len_initial == len_after: # if the the lenght is the same before and after it meant the same value was added...which is a duplicate
            dups_set.add(entry) # add it to the other list
            # print('had to to add this entry: ', entry)
            # print('duplicate list: ', dups_set)
            
    return(dups_set)

print(find_dups([1, 1, 2, 3, 4, 2]))