# Notes

len to calculate number of characters being used
```
>>> len("Bruce")
7
```

concatenation operator
```
>>> "bruce" + "wayne"
'brucewayne'
>>> "bruce" + " wayne"
'bruce wayne'
```

With a number
```
"bruce" + " wayne" + " age" + " 49"
'bruce wayne age 49'
```
or
```
"bruce" + " wayne" + " age " + str(49)
'bruce wayne age 49'
```

same can be done to numbers

```
>>> int("33")
33
>>> 
>>> float("33")
33.0
```

```
>>> "BLA" * 5
'BLABLABLABLABLA'
```

special characters
```
>>> "that's better"
"that's better"
>>> 'She said, "That is better."' 'She said, "That is better."'

>>> '\''
"'"
```

special escape sequences
|Escape Sequence|Description|
|---|--|
|\' |Single quote |
|\" |Double quote|
|\\ |Backslash|
|\t |Tab|
|\n |Newline|
|\r|Carriage return|
  
```
>>> text = """line 1
... line 2
... line 3"""

>>> print(text)
line 1
line 2
line 3

>>> print("line 1\nline 2\nline 3")
line 1
line 2
line 3

>>> print("line 1\ttab1\nline 2\ttab2\nline 3\ttab3")
line 1	tab1
line 2	tab2
line 3	tab3

```

seperator to change the seperator character
```
>>> print('a', 'b', 'c')
a b c
>>> print('a', 'b', 'c', sep=', ') 
a, b, c
>>> print('a', 'b', 'c', sep=' | ') 
a | b | c

```

end of a new line
```
>>> print('a', 'b', 'c', end='') 
a b c>>> 
```

input
```
>>> species = input()
test
>>> species
'test'
```

input conversion
```
>>> money = input()
393
>>> money
'393'
>>> money = int(money)
>>> money
393


>>> money = int(input())
300
>>> money
300


>>> money = int(input("show me the money: "))
show me the money: 393
>>> money
393
```


# Exercises

1. What value does each of the following expressions evaluate to? Verify your answers by typing the expressions into the Python shell.
a. 'Computer' + ' Science'
Computer Science
```
>>> 'Computer' + ' Science'
'Computer Science'
```

b. 'Darwin\'s'
"Darwin's"
```
>>> 'Darwin\'s'
"Darwin's"
```

c. 'H2O' * 3
'H2OH2OH2O'
```
>>> 'H2O' * 3
'H2OH2OH2O'
```
d. 'CO2' * 0
''
```
>>> 'CO2' * 0
''
```
2. Express each of the following phrases as Python strings using the appropriate type of quotation marks (single, double, or triple) and, if necessary, escape sequences. There is more than one correct answer for each of these phrases.
a. They’ll hibernate during the winter.
"They’ll hibernate during the winter."
'They’ll hibernate during the winter.'

b. “Absolutely not,” he said.
"“Absolutely not,” he said."

c. “He said, ‘Absolutely not,’” recalled Mel.
"“He said, ‘Absolutely not,’” recalled Mel."

d. hydrogen sulfide
"hydrogen sulfide"
e. left\right
"left\right"
'left\\right'

3. Rewrite the following string using single or double quotes instead of triple quotes:
'''A 
B 
C'''

'A\nB\nC'
```
>>> print('A\nB\nC')
A
B
C
```
4. Use built-in function len to find the length of the empty string.
```
>>> len('')
0
```
5. Given variables x and y, which refer to values 3 and 12.5, respectively, use function print to print the following messages. When numbers appear in the messages, variables x and y should be used.
```
x=3
y=12.5
```
a. The rabbit is 3.
print("The rabbit is " + str(x) + ".")
b. The rabbit is 3 years old.
print("The rabbit " + str(x) + " years old.")

c. 12.5 is average.
```
>>> print(y, "is average.")
12.5 is average.

```

d. 12.5 * 3
```
>>> print(y, "*", x)
12.5 * 3
```
e. 12.5 * 3 is 37.5.
print(str(y) + " * " + str(x) + " is " + str(y * x) + ".")


6. Consider this code:
```
>>> first = 'John'
>>> last = 'Doe'
>>> print(last + ', ' + first)
What is printed by this code?
Doe, John
```
```
>>> print(last + ', ' + first)
Doe, John
>>> last + ', ' + first
'Doe, John'
```

7. Use input to prompt the user for a number, store the number entered as a float in a variable named num, and then print the contents of num.

num = float(input())
print(num)
```
>>> num = float(input())
12.5
>>> print(num)
12.5
```

8. Complete the examples in the docstring and then write the body of the
following function:
```
def repeat(s: str, n: int) -> str:
    """ Return s repeated n times; if n is negative, return the empty string.
    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    >>> repeat('no', -2)
    >>> repeat('yesnomaybe', 3)
    """
    return s * n

repeat('yes', 4)

>>> repeat('yesnomaybe', 3)
'yesnomaybeyesnomaybeyesnomaybe'
>>> repeat('yes', 4)
'yesyesyesyes'
```

9. Complete the examples in the docstring and then write the body of the following function:
```
def total_length(s1: str, s2: str) -> int:
    """ Return the sum of the lengths of s1 and s2.
    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')
    >>> total_length('YES!!!!', 'Noooooo')
    """
    return len(s1 + s2)


>>> total_length('yes', 'no')
5
>>> total_length('yes', '')
3
>>> total_length('YES!!!!', 'Noooooo')
14
```

```
>>> 45 > 34
True
```

```
>>> 67.0 == 67 
True
>>> 67.0 != 67 
False
```

 “iff,” which stands for “if and only if.”
 ```
 >>> def is_positive(x: float) -> bool:
... """Return True iff x is positive. ...
...     >>> is_positive(3)
... True
...     >>> is_positive(-4.6)
... False
... """
... returnx>0 ...
>>> is_positive(3) True
```

this
```
>>> x = 3
>>> (1 < x) and (x <= 5)
```
is the same as this
```
>>> x = 3
>>> 1 < x <= 5
```

```
>>> not 0 
True
>>> not 1 
False
>>> not 34.2 
False
>>> not -87 
False
```

strings
```
>>> not '' 
True
>>> not 'bad' 
False
```