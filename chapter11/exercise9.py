# Write a function called dict_intersect that takes two dictionaries as arguments and returns a dictionary that contains only the key/value pairs found in both of the original dictionaries.

def dict_intersect(dict1, dict2):

    inter = {}
    
    for (key, value) in dict1.items():
        if key in dict2 and value == dict2[key]:
            inter[key] = value

    return print(inter)

dict1 = {'R': 0.3, 'G': 0.5, 'B': 0.2}

dict2 = {'R': 0.1, 'G': 0.5, 'B': 0.2}

dict_intersect(dict1, dict2)
