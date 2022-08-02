# Write a function called count_duplicates that takes a dictionary as an argument and returns the number of values that appear two or more times.

def count_duplicates(colors):
    
    values = list(colors.values())
    duplicate = 0
    
    values_set = list(set(colors.values()))
    # print(values_set)
    
    for i in values:
        # print(values.count(i))
        
        if values.count(i) >= 2:
            duplicate = duplicate + 1
            num_occurrences = values.count(i)
            for x in range(num_occurrences):
                values.remove(i)
        # print(i)
        
        
    
    return print(duplicate)


colors = {'red': 1, 'green': 1, 'blue': 2, 'yellow': 2}

count_duplicates(colors)

