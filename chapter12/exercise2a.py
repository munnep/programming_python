from typing import List, Tuple

def find_smallest(L: List[float]) -> Tuple[int, int]:
    """Return a tuple smallest and the index
    """

    min = 1000
    min_index = 9999

    for i in range(len(L)):
        if L[i] <= min:
            min = L[i] 
            min_index = i
    
    return (min, min_index)

print(find_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476]))