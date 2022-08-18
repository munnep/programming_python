# Chapter 12: Designing algorithms

find the smallest value

```
>>> counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
>>> min(counts)
96
>>> counts.index(min(counts))
6
```

try to write down what you want before translating it to code

```
def find_two_smallest(L): """ (see above) """
    # Get the minimum item in L            <-- This line is new
    # Find the index of that minimum item  <-- This line is new
    # Remove that item from the list
    # Find the index of the new minimum item in the list
    # Put the smallest item back in the list
    # If necessary, adjust the second index
    # Return the two indices
```
code eventually is `smallest1.py`

You can solve the same problem in difference ways. Two other ways are the following

`smallest2.py`
`smallest3.py`




