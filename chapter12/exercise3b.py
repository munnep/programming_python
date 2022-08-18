def hopedale_average(filename): 
    """ (str) -> float
    Return the average number of pelts produced per year for the data in Hopedale
    file named filename. 
    """

    with open(filename, 'r') as hopedale_file:
    # Read the description line. 
        hopedale_file.readline()
    # Keep reading comment lines until we read the first piece of data. 
        data = hopedale_file.readline().strip()
        
        while data.startswith('#'):
            data = hopedale_file.readline().strip()
        
        # Now we have the first piece of data append it to an empty list. 
        pelts_list = []
        pelts_list.append(int(data))
        
        # Read the rest of the data. for data in hopedale_file:
        pelts_list.append(int(data.strip())) 
    
    return sum(pelts_list) / len(pelts_list)

print(hopedale_average('hopedale.txt'))    