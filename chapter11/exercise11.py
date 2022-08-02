# Write another function called db_consistent that takes a dictionary of dictio- naries in the format described in the previous question and returns True if and only if every one of the inner dictionaries has exactly the same keys. (This function would return False for the previous example, since Rosalind Franklin’s entry doesn’t contain the 'author' key.)

def db_consistent(dict_of_dict):
    """ (dict of dict) -> set
    Return a set of the keys in the inner dictionaries in dict_of_dict.
    >>> db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    {1, 2, 3}
    """
 
    inner_keys_list = []
    # Build a list of list of keys
    for key in dict_of_dict:
       inner_keys = list(dict_of_dict[key].keys())
       inner_keys.sort()
       inner_keys_list.append(inner_keys)
     
    print(inner_keys_list) 
    for i in range(1, len(inner_keys_list)):
     # If the number of keys is different.
        if len(inner_keys_list[0]) != len(inner_keys_list[i]):
            return False
    
     # If the keys don't match.
    for j in range(len(inner_keys_list[0])):
        if inner_keys_list[0][j] != inner_keys_list[i][j]:
            return False
    
    return True


example = {
'jgoodall' : {'surname' : 'Goodall',
              'forename' : 'Jane',
              'born' : 1934,
              'died' : None,
              'notes' : 'primate researcher', 
              'author' : ['In the Shadow of Man',
                          'The Chimpanzees of Gombe']}, 
'rfranklin' : {'surname' : 'Franklin',
               'forename' : 'Rosalind',
               'born' : 1920,
               'died' : 1957,
               'notes' : 'contributed to discovery of DNA'},
'rcarson' : {'surname' : 'Carson', 
             'forename' : 'Rachel',
             'born' : 1907,
             'died' : 1964,
             'notes' : 'raised awareness of effects of DDT', 
             'author' : ['Silent Spring']}
}

print(db_consistent(example))