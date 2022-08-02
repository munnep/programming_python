# The keys in a dictionary are guaranteed to be unique, but the values are not. Write a function called count_values that takes a single dictionary as an argument and returns the number of distinct values it contains. Given the input {'red': 1, 'green': 1, 'blue': 2}, for example, it should return 2.


def count_values(colors):
    
    unique_value = set()
    
    for color in colors:
        unique_value.add(colors[color])
        # print(colors[color])
    
    result = len(unique_value)  
    
    return print(result)


colors = {'red': 1, 'green': 3, 'blue': 2, 'yellow': 2}

count_values(colors)



# solution Book 

# def count_values(dictionary):
#     """ (dict) -> int
#     Return the number of unique values in dictionary.
#     >>> count_values({'red': 1, 'green': 2, 'blue': 2})
#     2
#     """
#     return len(set(dictionary.values()))