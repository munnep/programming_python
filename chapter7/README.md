
```
>>> str.center('Sonnet 43', 26)
'             Sonnet 43            '
>>> str.count('How do I love thee? Let me count the ways.', 'the') 
2
```

```
>>> 'species'.startswith('a') 
False
>>> 'species'.startswith('spe') 
True
```
```
>>> str.upper('test')
'TEST'
```
preferred way
```
>>> 'test'.upper()
'TEST'
```
```
>>> '"{0}" is derived from "{1}"'.format('none', 'no one')
'"none" is derived from "no one"'
```

```
>>> my_pi = 3.14159
>>> 'Pi rounded to {0} decimal places is {1:.2f}.'.format(2, my_pi) 
'Pi rounded to 2 decimal places is 3.14.'
>>> 'Pi rounded to {0} decimal places is {1:.3f}.'.format(3, my_pi) 
'Pi rounded to 3 decimal places is 3.142.'
```

# exercises



1. In the Python shell, execute the following method calls:
a. 'hello'.upper()
```
HELLO
```
b. 'Happy Birthday!'.lower()
```
'happy birthday!'
```
c. 'WeeeEEEEeeeEEEEeee'.swapcase()
```
'wEEEeeeeEEEeeeeEEE'
```
d. 'ABC123'.isupper()
```
True
```
e. 'aeiouAEIOU'.count('a')
```
1
```
f. 'hello'.endswith('o')
```
True
```
g. 'hello'.startswith('H')
```
False
```
h. 'Hello {0}'.format('Python')
```
'Hello Python'
```
i. 'Hello {0}! Hello {1}!'.format('Python', 'World')
```
'Hello Python! Hello World!'
```
2. Using string method count, write an expression that produces the number of o’s in 'tomato'.
```
'tomato'.count('o')
```
3. Using string method find, write an expression that produces the index of the first occurrence of o in 'tomato'.
```
'tomato'.find('o')
```
4. Using string method find, write a single expression that produces the index of the second occurrence of o in 'tomato'. Hint: Call find twice.
```
'tomato'.find('o', 'tomato'.find('o') + 1)
```
5. Using your expression from the previous exercise, find the second o in 'avocado'. If you don’t get the result you expect, revise the expression and try again.
```
'avocado'.find('o', 'avocado'.find('o') + 1)
```
6. Using string method replace, write an expression that produces a string based on 'runner' with the n’s replaced by b’s.
```
'runner'.replace('nn','bb')
```
7. Variable s refers to ' yes '. When a string method is called with s as its argument, the string 'yes' is produced. Which string method was called?
```
s = ' yes '
>>> s.strip()
'yes'
```
8. Variable fruit refers to 'pineapple'. For the following function calls, in what order are the subexpressions evaluated?
a. fruit.find('p', fruit.count('p'))
```
fruit = 'pineapple'
fruit.find('p', fruit.count('p'))
fruit.find('p', 3)
6
```

b. fruit.count(fruit.upper().swapcase())
```
fruit = 'pineapple'
fruit.count(fruit.upper().swapcase())

upper
swapcase
count


```


c. fruit.replace(fruit.swapcase(), fruit.lower())
```
fruit = 'pineapple'
fruit.replace(fruit.swapcase(), fruit.lower())

fruit.replace('PINEAPPLE', 'pineapple')
```
9. Variable season refers to 'summer'. Using string method format and variable season, write an expression that produces 'I love summer!'
```
season = 'summer'

'I love {0}!'.format(season)
'I love summer!'
```
10. Variables side1, side2, and side3 refer to 3, 4, and 5, respectively. Using string method format and those three variables, write an expression that produces 'The sides have lengths 3, 4, and 5.'
```
side1 = 3
side2 = 4
side3 = 5

'The sides have lengths {0}, {1}, and {2}.'.format(side1, side2, side3)
```
11. Using string methods, write expressions that produce the following:
a. A copy of 'boolean' capitalized
```
'boolean'.capitalize()
```
b. The first occurrence of '2' in 'CO2 H2O'
```
'CO2 H2O'.find('2')
```
c. The second occurrence of '2' in 'CO2 H2O'
```
'CO2 H2O'.find('2', 'CO2 H2O'.find('2') + 1)
```
d. True if and only if 'Boolean' begins lowercase
```
'Boolean'.islower()
```

Correct answer is ?????????
```
'Boolean'[0].islower()
```
e. A copy of "MoNDaY" converted to lowercase and then capitalized
```
"MoNDaY".lower().capitalize()
```
f. A copy of " Monday" with the leading whitespace removed
" Monday".lstrip()

12. Complete the examples in the docstring and then write the body of the following function:
```
def total_occurrences(s1: str, s2: str, ch: str) -> int: 
    """Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    >>> total_occurrences('green', 'purple', 'b')
    """
    return (s1 + s2).count(ch)
```

```
>>> def total_occurrences(s1: str, s2: str, ch: str) -> int: 
...     """Precondition: len(ch) == 1
...     Return the total number of times that ch occurs in s1 and s2.
...     >>> total_occurrences('color', 'yellow', 'l')
...     3
...     >>> total_occurrences('red', 'blue', 'l')
...     >>> total_occurrences('green', 'purple', 'b')
...     """
...     return (s1 + s2).count(ch)
... 
>>> total_occurrences('color', 'yellow', 'l')
3
>>> total_occurrences('red', 'blue', 'l')
1
>>> total_occurrences('green', 'purple', 'b')
0
```

Not the answer from the book but mine looks much better
```
     return s1.count(ch) + s2.count(ch)
```