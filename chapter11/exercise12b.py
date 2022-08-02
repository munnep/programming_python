# The dot product of two vectors is the sum of the products of corre- sponding elements. For example, the dot product of [1, 2, 3] and [4, 5, 6] is 4+10+18, or 32. Write another function called sparse_dot that calculates the dot product of two sparse vectors.

def sparse_add(dict1, dict2):
 
    dot = 0
 
    for key1 in dict1:
        if key1 in dict2:
             dot = dot + dict1[key1] * dict2[key1]
 
    return dot

dict1 = {1: 3, 2: 4}
dict2 = {1: 3, 3: 4}

print(sparse_add(dict1, dict2))