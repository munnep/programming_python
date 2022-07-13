# normal with list
for line in list(open("alkaline_metals.txt")):
    print(line.rstrip())  
    
# normal reversed    
for line in reversed(list(open("alkaline_metals.txt"))):
    print(line.rstrip())    