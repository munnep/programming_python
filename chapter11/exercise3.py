# Python’s set objects have a method called pop that removes and returns an arbitrary element from the set. If the set gerbils contains five cuddly little ani- mals, for example, calling gerbils.pop() five times will return those animals one by one, leaving the set empty at the end. Use this to write a function called mating_pairs that takes two equal-sized sets called males and females as input and returns a set of pairs; each pair must be a tuple containing one male and one female. (The elements of males and females may be strings containing gerbil names or gerbil ID numbers—your function must work with both.)

# male = {'jan', 'klaas', 'piet', 'kees', 'ruud'}
# female = {'ria', 'susan', 'lotte', 'marja', 'babette'}

# >>> mating_pairs({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob', 'Chen'})

def mating_pairs(males,females):
    """
    """
    
    pairs = set()
    num_gerbils = len(males)
     
    for i in range(num_gerbils):
        male = males.pop()
        female = females.pop()
        pairs.add((male, female),)
     
    return pairs
 
 
males = {'jan', 'klaas', 'piet', 'kees', 'ruud'}
females = {'ria', 'susan', 'lotte', 'marja', 'babette'}

print(mating_pairs(males,females))






# Removes key k from dictionary D and returns the value that was asso- ciated with k—if k isn’t in D, an error is raised.

# D.pop(k)
# male = {'jan', 'klaas', 'piet', 'kees', 'ruud'}
# >>> male.pop()
# 'kees'
# >>> male.pop()
# 'piet'
# >>> male.pop()
# 'ruud'
# >>> male
# {'jan', 'klaas'}