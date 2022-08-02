# Programmers sometimes use a dictionary of dictionaries as a simple database. For example, to keep track of information about famous scientists, you might have a dictionary where the keys are strings and the values are dictionaries, like this

def db_headings(dict_of_dict):
    """ (dict of dict) -> set
    Return a set of the keys in the inner dictionaries in dict_of_dict.
    >>> db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    {1, 2, 3}
    """
 
    inner_keys = set()
    
    for key in dict_of_dict:
        print(key)
        for inner_key in dict_of_dict[key]:
            inner_keys.add(inner_key)
    
    return print(inner_keys)



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

db_headings(example)