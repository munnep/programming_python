creating
```
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3] 
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> 
>>> whales[0]
5
>>> whales[-1]
3

```

```
def average(L: list[float]) -> float:
    """Return the average of the values in L. 
    >>> average([1.4, 1.6, 1.8, 2.0])
    1.7
    """
    return average(L)

average(2.0, 3.0)    
```

changing
```
>>> nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
>>> nobles
['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
>>> nobles[1] = 'neon'
>>> nobles
['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
```

sorting
```
>>> nobles
['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
>>> len(nobles)
6
>>> sorted(nobles)
['argon', 'helium', 'krypton', 'neon', 'radon', 'xenon']
```

concatenation
```
>>> original = ['H', 'He', 'Li'] 
>>> final = original + ['Be'] 
>>> final
['H', 'He', 'Li', 'Be']
```

delete
```
>>> metals = ['Fe', 'Ni'] 
>>> del metals[0]
>>> metals
['Ni']
```

in operator
```
nobles = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon'] 
gas = input('Enter a gas: ')

if gas in nobles:
    print('{0} is noble.'.format(gas))
```

```
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> useful_markers = celegans_phenotypes[0:4]
>>> useful_markers
['Emb', 'Him', 'Unc', 'Lon']
```

```
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes[:4]
['Emb', 'Him', 'Unc', 'Lon']
>>> celegans_phenotypes[4:]
['Dpy', 'Sma']
```

copy
```
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_copy = celegans_phenotypes[:]
>>> celegans_phenotypes[5] = 'Lvl'
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> celegans_copy
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> 

```

Methods
```
>>> colors = ['red', 'orange', 'green']
>>> colors.extend(['black', 'blue'])
>>> colors
['red', 'orange', 'green', 'black', 'blue']
>>> colors.append('purple')
>>> colors
['red', 'orange', 'green', 'black', 'blue', 'purple']
>>> colors.insert(2, 'yellow')
>>> colors
['red', 'orange', 'yellow', 'green', 'black', 'blue', 'purple']
>>> colors.remove('black')
>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'purple']
```

list of lists
```
>>> life
[['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
```

```
>>> life
[['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> life[0]
['Canada', 76.5]
>>> life[0][1]
76.5
```

Exercises

1. Variable kingdoms refers to the list ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']. Using kingdoms and either slicing or indexing with positive indices, write expressions that produce the following:
a. The first item of kingdoms
```
kingdoms=['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']

>>> kingdoms[0]
'Bacteria'
```

b. The last item of kingdoms
```
>>> kingdoms[5]
'Animalia'
```
c. The list ['Bacteria', 'Protozoa', 'Chromista']
```
>>> kingdoms[:3]
['Bacteria', 'Protozoa', 'Chromista']
```
d. The list ['Chromista', 'Plantae', 'Fungi']
```
>>> kingdoms[2:5]
['Chromista', 'Plantae', 'Fungi']
```
e. The list ['Fungi', 'Animalia']
```
>>> kingdoms[4:]
['Fungi', 'Animalia']
```
f. The empty list
```
kingdoms[0:0]
```

2. use negative 
a. The first item of kingdoms
```
kingdoms=['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']

>>> kingdoms[-6]
'Bacteria'
```

b. The last item of kingdoms
```
>>> kingdoms[-1]
'Animalia'
```
c. The list ['Bacteria', 'Protozoa', 'Chromista']
```
>>> kingdoms[-6:-3]
['Bacteria', 'Protozoa', 'Chromista']
```
d. The list ['Chromista', 'Plantae', 'Fungi']
```
>>> kingdoms[-4:-1]
['Chromista', 'Plantae', 'Fungi']
```
e. The list ['Fungi', 'Animalia']
```
>>> kingdoms[-2:]
['Fungi', 'Animalia']
```
f. The empty list
```
kingdoms[-1:-1]
```

3. Variable appointments refers to the list ['9:00', '10:30', '14:00', '15:00', '15:30']. An appointment is scheduled for 16:30, so '16:30' needs to be added to the list.
a. Using list method append, add '16:30' to the end of the list that appoint-
ments refers to
```
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
>>> appointments.append('16:30')
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
```
b. Instead of using append, use the + operator to add '16:30' to the end of the list that appointments refers to.
```
appointments += ['16:30']
```
c. You used two approaches to add '16:30' to the list. Which approach modified the list and which approach created a new list?
```
a modified and b created a new list
```

4. Variable ids refers to the list [4353, 2314, 2956, 3382, 9362, 3900]. Using list methods, do the following:
a. Remove 3382 from the list.
```
>>> ids = [4353, 2314, 2956, 3382, 9362, 3900]
>>> ids
[4353, 2314, 2956, 3382, 9362, 3900]
>>> ids.remove(3382)
>>> ids
[4353, 2314, 2956, 9362, 3900]
```
b. Get the index of 9362.
```
>>> ids.index(9362)
3
```
c. Insert 4499 in the list after 9362.
```
>>> ids
[4353, 2314, 2956, 9362, 3900]
>>> ids.insert(4,4499)
>>> ids
[4353, 2314, 2956, 9362, 4499, 3900]
```
d. Extend the list by adding [5566, 1830] to it.
```
>>> ids
[4353, 2314, 2956, 9362, 4499, 3900]
>>> ids.extend([5566, 1830])
>>> ids
[4353, 2314, 2956, 9362, 4499, 3900, 5566, 1830]
```
e. Reverse the list.
```
>>> ids
[4353, 2314, 2956, 9362, 4499, 3900, 5566, 1830]
>>> ids.reverse()
>>> ids
[1830, 5566, 3900, 4499, 9362, 2956, 2314, 4353]
```
f. Sort the list.
```
>>> ids
[1830, 5566, 3900, 4499, 9362, 2956, 2314, 4353]
>>> ids.sort()
>>> ids
[1830, 2314, 2956, 3900, 4353, 4499, 5566, 9362]
```

5. 
a. Assign a list that contains the atomic numbers of the six alkaline earth metals—beryllium (4), magnesium (12), calcium (20), strontium (38), barium (56), and radium (88)—to a variable called alkaline_earth_metals.
```
alkaline_earth_metals = [ ['earth metals—beryllium', 4], ['magnesium', 12], ['calcium', 20], ['strontium', 38], ['barium', 56], ['radium' ,88]]
```

```
alkaline_earth_metals = [4, 12, 20, 38, 56, 88]
```



b. Which index contains radium’s atomic number? Write the answer in two ways, one using a positive index and one using a negative index.
```
alkaline_earth_metals[5][1]
alkaline_earth_metals[-1][-1]
```

```
alkaline_earth_metals[5], 
alkaline_earth_metals[-1]
```

c. Which function tells you how many items there are in alkaline_earth_metals?
```
>>> len(alkaline_earth_metals)
6
```
d. Write code that returns the highest atomic number in alkaline_earth_metals.
(Hint: Use one of the functions from Table 10, List Functions, on page 135.)

```
max(alkaline_earth_metals)
```

6. In this exercise, you’ll create a list and then answer questions about that list.
a. Create a list of temperatures in degrees Celsius with the values 25.2, 16.8, 31.4, 23.9, 28, 22.5, and 19.6, and assign it to a variable called temps.
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]


b. Using one of the list methods, sort temps in ascending order.
```
temps.sort()
```
c. Using slicing, create two new lists, cool_temps and warm_temps, which contain
the temperatures below and above 20 degrees Celsius, respectively.
```
cool_temps = temps[0:2]
warm_temps = temps[2:]
```
d. Using list arithmetic, recombine cool_temps and warm_temps into a new
list called temps_in_celsius.
```
temps_in_celsius = cool_temps + warm_temps

```

7. 
```
def same_first_last(L: list) -> bool: 
    """Precondition: len(L) >= 2
    Return True if and only if first item of the list is the same as the
    last.
    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    >>> same_first_last([4.0, 4.5])
    """
    return L[0] == L[-1]
```

8. 
```
def is_longer(L1: list, L2: list) -> bool:
    """Return True if and only if the length of L1 is longer than the length of L2.
    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3]
    """
    return len(L1) > len(L2)
```
9. Draw a memory model showing the effect of the following statements:
    values = [0, 1, 2]
    values[1] = values

```
>>> values = [0, 1, 2]
>>> 
>>> values[1] = values
>>> values
[0, [...], 2]
```
they point to the same value in memory

10. 
Variable units refers to the nested list [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]. Using units and either slicing or indexing with positive indices, write expressions that produce the following:

a. The first item of units (the first inner list)
```
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]

units[0]
```

b. The last item of units (the last inner list)
```
units[1]
```
c. The string 'km'
```
>>> units[0][0]
'km'
```
d. The string 'kg'
>>> units[1][0]
'kg'
e. The list ['miles', 'league']
```
>>> units[0][1:3]
['miles', 'league']
```
f. The list ['kg', 'pound']
>>> units[1][0:2]
['kg', 'pound']

11. 
a. The first item of units (the first inner list)
```
units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]

units[-2]
```

b. The last item of units (the last inner list)
```
units[-1]
```
c. The string 'km'
```
>>> units[-2][-3]
'km'
```
d. The string 'kg'
>>> units[-1][-3]
'kg'
e. The list ['miles', 'league']
```
>>> units[-2][-2:]
['miles', 'league']
```
f. The list ['kg', 'pound']
>>> units[-1][:-1]
['kg', 'pound']