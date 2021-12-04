
import math module and use it

```
>>> import math

>>> sqrt(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined

>>> math.sqrt(9)
3.0

>>> math.pi
3.141592653589793

>>> math.pi
3.141592653589793
```

specific parts of a module to use by creating those functions
```
from math import sqrt, pi
```

the python module index
[https://docs.python.org/release/3.6.0/py-modindex.html](https://docs.python.org/release/3.6.0/py-modindex.html)

Using doctest
```
python -m doctest -v exercise.py
```


# exercises

1. Import module math, and use its functions to complete the following exercises. (You can call dir(math) to get a listing of the items in math.)  
a. Write an expression that produces the floor of -2.8.  
```
import math
math.floor(-2.8)

```
b. Write an expression that rounds the value of -4.3 and then produces the absolute value of that result.
```
abs(round(-4.3))
```
c. Write an expression that produces the ceiling of the sine of 34.5.
```
math.ceil(math.sin(34.5))
```

2. In the following exercises, you will work with Python’s calendar module:
a. Visit the Python documentation website at http://docs.python.org/release/3.6.0/py-modindex.html, and look at the documentation on module calendar.
b. Import module calendar.
```
import calendar
```
c. Using function help, read the description of function isleap.
```
help(calendar.isleap)

Help on function isleap in module calendar:

isleap(year)
    Return True for leap years, False for non-leap years
```
d. Use isleap to determine the next leap year.
```
>>> calendar.isleap(2021)
False
>>> calendar.isleap(2022)
False
>>> calendar.isleap(2023)
False
>>> calendar.isleap(2024)
True
```
e. Use dir to get a list of what calendar contains.
```
dir(calendar)
```
f. Find and use a function in module calendar to determine how many leap years there will be between the years 2000 and 2050, inclusive.
```
calendar.leapdays(2000, 2050)
```
g.  Find and use a function in module calendar to determine which day of the week July 29, 2016, will be.
```
calendar.weekday(2016, 7, 29)
```

3. Create a file named exercise.py with this code inside it: 
```
def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2.
    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    """
    return num1 + num2 / 2
```


```
python -m doctest -v exercise.py

Trying:
    average(10,20)
Expecting:
    15.0
**********************************************************************
File "/Users/patrickmunne/git/programming_python/chapter6/exercise.py", line 3, in exercise.average
Failed example:
    average(10,20)
Expected:
    15.0
Got:
    20.0
Trying:
    average(2.5, 3.0)
Expecting:
    2.75
**********************************************************************
File "/Users/patrickmunne/git/programming_python/chapter6/exercise.py", line 5, in exercise.average
Failed example:
    average(2.5, 3.0)
Expected:
    2.75
Got:
    4.0
1 items had no tests:
    exercise
**********************************************************************
1 items had failures:
   2 of   2 in exercise.average
2 tests in 2 items.
0 passed and 2 failed.
***Test Failed*** 2 failures.
```

change code to following
```
def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2.
    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    """
    return (num1 + num2) / 2
```

```
python -m doctest -v exercise.py
Trying:
    average(10,20)
Expecting:
    15.0
ok
Trying:
    average(2.5, 3.0)
Expecting:
    2.75
ok
1 items had no tests:
    exercise
1 items passed all tests:
   2 tests in exercise.average
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

```