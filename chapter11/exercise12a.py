# The sum of two vectors is just the element-wise sum of their elements. For example, the sum of [1, 2, 3] and [4, 5, 6] is [5, 7, 9]. Write a function called sparse_add that takes two sparse vectors stored as dictionaries and returns a new dictionary representing their sum.

def sparse_add(dict1, dict2):
 
    sum_vector = dict1.copy()
    for key in dict2:
        if key in sum_vector:
            sum_vector[key] = sum_vector[key] + dict2[key]
        else:
            sum_vector[key] = dict2[key]
 
    return sum_vector

dict1 = {1: 3, 2: 4}
dict2 = {1: 3, 3: 4}

print(sparse_add(dict1, dict2))