# Notes

```
>>> not True
False
>>> not False
True
```

```
>>> True and True
True
>>> False and False
False
>>> True and False
False
>>> False and True
False
```

inclusive or
```
>>> True or True 
True
>>> False or False 
False
>>> True or False 
True
>>> False or True 
True
```


|Symbol| Operation|
|------|----------------|
|>     |Greater than  |
|<     |Less than  |
|>=    |Greater than or equal to   |
|<=    |Less than or equal to   |
| ==     |Equal to  |
|!=    |Not equal to  |

special cases
```
>>> not 0 
True
>>> not 1 
False

>>> not '' 
True
>>> not 'bad' 
False
```

characters have special ASCII number.    
Capitals have lower numbers then lowercase

```

>>> 'A' < 'a' 
True
>>> 'A' > 'z' 
False
>>> 'abc' < 'abd' 
True
>>> 'abc' < 'abcd' 
True
```

Check if a string is in a sentence
```
>>> 'Jan' in '01 Jan 1838' 
True
>>> 'Feb' in '01 Jan 1838' 
False
```


IF condition
```
if «condition»: «block»
```

example if
```
>>> ph = float(input('Enter the pH level: ')) Enter the pH level: 8.0
>>> if ph < 7.0:
...     print(ph, "is acidic.")
```

example elif
```
>>> ph = float(input('Enter the pH level: ')) Enter the pH level: 8.5
>>> if ph < 7.0:
...    print(ph, "is acidic.")
... elif ph > 7.0:
...     print(ph, "is basic.")
```

example else. When nothing matches
```
if «condition»: 
    «if_block»
elif «condition»: 
    «elif_block» 
else:
    «else_block»


```
compound = input('Enter the compound: ') 

if compound == "H2O":
    print("Water")
elif compound == "NH3": 
    print("Ammonia")
elif compound == "CH4": 
    print("Methane")
else:
    print("Unknown compound")
```


Nested if 
```
value = input('Enter the pH level: ') 
if len(value) > 0:
    ph = float(value) 
    if ph < 7.0:
        print(ph, "is acidic.") 
    elif ph > 7.0:
        print(ph, "is basic.") 
    else:
        print(ph, "is neutral.") 
else:
    print("No pH value was given!")

# Exercises

1. What value does each expression produce? Verify your answers by typing the expressions into Python.  
a. True and not False
True


b. True and not false (Notice the capitalization.)
False
```
>>> True and not false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
```

c. True or True and False
false

of course
true and false
true
```
>>> True or True and False
True
```

d. not True or not False
false or true
true

e. True and not 0
true and true
true
```
>>> True and not 0
True

```
f. 52 < 52.3
true
```
>>> 52 < 52.3
True
```
g. 1+52<52.3
53 < 52.3
false

h. 4!=4.0
false
```
>>> 4!=4.0
False
```

2. Variables x and y refer to Boolean values.
a. Write an expression that produces True iff both variables are True.
x = True
y = True
x == y
x and y
```
>>> x = True
>>> y = True
>>> x == y
>>> x and y
True



```

b. Write an expression that produces True iff x is False.
x = False
y = True
x != y
```
>>> x = False
>>> y = True
>>> x == y
False
>>> x != y
True

questions says nothing about y so following is correct
>>> x = False
>>> y = True
>>> not x
True

```

c. Write an expression that produces True iff at least one of the variables is True.
x = False
y = True
x == y
x or y
```
>>> x = False
>>> y = True
>>> x or y
True
```

3. Variables full and empty refer to Boolean values. Write an expression that produces True if and only if at most one of the variables is True.

full = True
empty = False
full or empty
```
>>> full = True
>>> empty = False
>>> full or empty
True
```
answer of the book
```
(full or empty) and not (full and empty)
```
If they both are True then you should get a false

```
>>> full = True
>>> empty = True
>>> full or empty
True
>>> (full or empty) and not (full and empty)
False
```
4. You want an automatic wildlife camera to switch on if the light level is less than 0.01 lux or if the temperature is above freezing, but not if both conditions are true. (You should assume that function turn_camera_on has already been defined.) Your first attempt to write this is as follows:
```
if (light < 0.01) or (temperature > 0.0):
    if not ((light < 0.01) and (temperature > 0.0)):
        turn_camera_on()
```

is this better?
```
if (light < 0.01) != (temperature > 0.0): 
    turn_camera_on()
```

light = 0
temperature = 1

if (light < 0.01) != (temperature > 0.0): 
    turn_camera_on()
    print('camera on')


5. In Functions That Python Provides, on page 31, we saw built-in function abs. Variable x refers to a number. Write an expression that evaluates to True if x and its absolute value are equal and evaluates to False otherwise. Assign the resulting value to a variable named result.

x = -5
result = abs(x) == x

```
>>> x = -5
>>> result = abs(x) == x
>>> 
>>> result
False
>>> x = 5
>>> result = abs(x) == x
>>> result
True
```
6. Write a function named different that has two parameters, a and b. The function should return True if a and b refer to different values and should return False otherwise.



```
1. Examples --> write examples  
different(a, b)

different(3,4)
true

different(4,4)
False


2. Header --> think of parameter names and what kind they are and the kind of output you suspect  
def different(a ,b):

3. Description --> Write a short detail what the function does with some examples  
    """
    The function should return True if a and b refer to different values and should return False otherwise.

    example:
    different(a, b)

    different(3,4)
    true
    
    different(4,4)
    False
    """

4. Body --> Write the code  
def different(a ,b):
    """
    The function should return True if a and b refer to different values and should return False otherwise.

    example:
    different(a, b)

    different(3,4)
    true
    
    different(4,4)
    False
    """
    return a != b 

>>> different(2,3)
True
>>> different(3,3)
False
```

7. Variables population and land_area refer to floats.
a. Write an if statement that will print the population if it is less than
10,000,000.
b. Write an if statement that will print the population if it is between 10,000,000 and 35,000,000.
c. Write an if statement that will print “Densely populated” if the land density (number of people per unit of area) is greater than 100.
d. Write an if statement that will print “Densely populated” if the land density (number of people per unit of area) is greater than 100, and “Sparsely populated” otherwise.