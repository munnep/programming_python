# Chapter 11: Storing Data Using Other Collection Types

A set is an unordered collection of distinct items. No duplicates

```
>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> vowels
{'i', 'o', 'a', 'u', 'e'}
```

No duplicates

```
>>> {'a', 'e', 'i', 'o', 'u'} == {'a', 'e', 'a', 'a', 'i', 'o', 'u', 'u'}
True
```

instead of {}
```
set([2, 3, 2, 5])
```

adding to a set

```
>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> vowels
{'i', 'o', 'a', 'u', 'e'}
>>> vowels.add('y')
>>> vowels
{'y', 'i', 'o', 'a', 'u', 'e'}
>>> vowels.add('y')
>>> vowels.add('y')
>>> vowels.add('y')
>>> vowels
{'y', 'i', 'o', 'a', 'u', 'e'}
```

do things if it is in the set
```
>>> ten = set(range(10))
>>> lows = {0, 1, 2, 3, 4}
>>> odds = {1, 3, 5, 7, 9}
>>> lows.add(9)
>>> lows
{0, 1, 2, 3, 4, 9}
>>> lows.difference(odds)
{0, 2, 4}
>>> lows.intersection(odds)
{1, 3, 9}
>>> lows.issubset(ten)
True
>>> lows.issuperset(odds)
False
>>> lows.remove(0)
>>> lows
{1, 2, 3, 4, 9}
>>> lows.symmetric_difference(odds) {2, 4, 5, 7}
>>> lows.union(odds)
{1, 2, 3, 4, 5, 7, 9}
>>> lows.clear()
>>> lows
set()
```
```
>>> lows = set([0, 1, 2, 3, 4])
>>> odds = set([1, 3, 5, 7, 9])
>>> lows - odds 
{0, 2, 4}
>>> lows & odds 
{1, 3}
>>> lows <= odds 
False
>>> lows >= odds 
False
>>> lows | odds
{0, 1, 2, 3, 4, 5, 7, 9}
```

tuples are immutable sequence
```
>>> bases = ('A', 'C', 'G', 'T')
>>> for base in bases:
...     print(base)
... 
A
C
G
T
```

tuples and changing

```
>>> life = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
>>> life
(['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
>>> life[0][1] = 80.0
>>> life[1][1] = 80.0
>>> life
(['Canada', 80.0], ['United States', 80.0], ['Mexico', 72.0])
```

dictionary is also knows as a map
```
>>> bird_to_observations = {'canada goose': 3, 'northern fulmar': 1}
>>> bird_to_observations
{'canada goose': 3, 'northern fulmar': 1}

>>> bird_to_observations['northern fulmar']
1
```

examples
```
>>> bird_to_observations = {}
>>> bird_to_observations['snow goose'] = 33
>>> bird_to_observations['eagle'] = 999
>>> bird_to_observations
{'snow goose': 33, 'eagle': 999}
>>> bird_to_observations[eagle]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'eagle' is not defined
>>> bird_to_observations['eagle']
999
>>> bird_to_observations['eagle'] = 9
>>> bird_to_observations
{'snow goose': 33, 'eagle': 9}


>>> del bird_to_observations['snow goose']
>>> bird_to_observations
{'eagle': 9}

>>> if 'eagle' in bird_to_observations:
...     print('eagles have been seen')
... 
eagles have been seen


```

dictionaries and the for loop option

```
>>> bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71,'snow goose': 63, 'northern fulmar': 1}
>>> for bird in bird_to_observations:
...     print(bird, bird_to_observations[bird])
... 
canada goose 183
long-tailed jaeger 71
snow goose 63
northern fulmar 1
```

Do things with dictionaries

```
>>> bird_to_observations.keys()
dict_keys(['canada goose', 'long-tailed jaeger', 'snow goose', 'northern fulmar'])
>>> bird_to_observations.values()
dict_values([183, 71, 63, 1])
>>> bird_to_observations.get('snow goose')
63
>>> bird_to_observations.get('snow goose2', 44)
44
>>> bird_to_observations
{'canada goose': 183, 'long-tailed jaeger': 71, 'snow goose': 63, 'northern fulmar': 1}
```

using the key and value together

```
scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809,'Turing' : 1912}


for scientist, birthdate in scientist_to_birthdate.items():
    print(scientist, 'was born in', birthdate)


invert a dictionary

```
bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71,'snow goose': 63, 'northern fulmar': 1}
observations_to_birds_list = {}

for bird, observations in bird_to_observations.items():
    if observations in bird_to_observations.items():
        observations_to_birds_list[observations].append(bird)
    else:
        observations_to_birds_list[observations] = [bird]

observations_to_birds_list

{183: ['canada goose'], 71: ['long-tailed jaeger'], 63: ['snow goose'], 1: ['northern fulmar']}
```

check a value is a key in a dictionary

```
>>> bird_to_observations = {'canada goose': 183, 'long-tailed jaeger': 71, 'snow goose': 63, 'northern fulmar': 1}
>>> 'snow goose' in bird_to_observations
True
>>> 183 in bird_to_observations
False
```

exercises:
