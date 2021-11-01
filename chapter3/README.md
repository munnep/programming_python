# Notes

abs is a function that gives tha absolute value of a number
```
>>> abs(-9) 
9
```

«function_name»(«arguments»)
   abs              9

```
>>> abs(3.3) 
3.3
```

produces 7 instead of -7
```
>>> day_temperature = 3
>>> night_temperature = 10
>>> abs(day_temperature - night_temperature)
7
```

```
abs(-7) + abs(3.3)
7+3.3 =10.3
```

```
pow(abs(-2), round(4.3))
```
from left to right. 

first abs(-2) = 2
second round(4.3) = 4
third pow(2,4) = 2 power of 4 = 16

```
>>> int(34.6) 
34
>>> int(-4.3) 
-4
>>> float(21) 
21.0
```

what do we see with the following
```
>>> int(34.6)
34
>>> round(34.6)
35
>>> float(34.6)
34.6
>>> float(34.0)
34.0
>>> round(float(34.6))
35
```

what does a function do
```
help(int)
class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
....
```

round with a second arguments round to the nearest after 2 decimals
```
>>> round(3.141592653)
3
>>> round(3.141592653, 2)
3.14
```


We can write the following as
```
>>> pow(2, 4, 3)
1

2x2x2x2=16

16%3 = 1 --> 16%3 remaining 16 divided by 3 is 15 closest that leaves 1 remaining 

>>> 16 % 3
1
>>> 17 % 3
2
>>> 18 % 3
0
>>> 19 % 3
1

```

each value is stored in memory. With ID we can get that memory
```
>>> id(-9)
4353846384
>>>  id(23.1)
  File "<stdin>", line 1
    id(23.1)
IndentationError: unexpected indent
>>> id(23.1)
4353843696
>>> fahrenheit = 77.7
>>> id(fahrenheit)
4353843760
```

creating your own function
```
def «function_name»(«parameters»): «block»

```

first example. Before return are 4 spaces
```
>>> def convert_to_celcius(fahrenheit):
...     return (fahrenheit - 32) * 5 / 9
... 
>>> convert_to_celcius(212)
100.0
```

second example
```
def quadratic(a, b, c, x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

quadratic(2, 3, 4, 0.5)
```

first, second and third are called local variables

```
def f(x):
    x=2*x
    return x
x = 1
x = f(x + 1) + f(x + 2)
```
What do we get?
```
x = f(1 + 1) + f(1 + 2)
    f(2)     + f(3)
    4        +  6

x = 10   

>>> def f(x):
...     x=2*x
...     return x
... 
>>> x = 1
>>> x = f(x + 1) + f(x + 2)
>>> x
10
```

Writing a good function
```
• What do you name the function?
• What are the parameters, and what types of information do they refer to? 
• What calculations are you doing with that information?
• What information does the function return?
• Does it work like you expect it to?
```

Example function with documentation
```
def days_difference(day1: int, day2: int) -> int:
    """Return the number of days between day1 and day2, which are ... both in the range 1-365 (thus indicating the day of the
    year).
   
    >>> days_difference(200, 224)
    24
    >>> days_difference(50, 50)
    0
    >>> days_difference(100, 99)
    -1
    """
    return day2 - day1
```

1. Examples --> write examples
2. Header --> think of parameter names and what kind they are and the kind of output you suspect
3. Description --> Write a short detail what the function does with some examples
4. Body --> Write the code
5. Test --> Test your code

Run it is a script
```
[~] % python temperature.py 
26.11111111111111
```

Precondition. Add this to your function to warn about invalid usage
```
def pie_percent(n: int) -> int: 
    """Precondition: n > 0
    Assuming there are n people who want to eat a pie, return the percentage
    of the pie that each person gets to eat.
    >>> pie_percent(5)
    20
    >>> pie_percent(2)
    50
    >>> pie_percent(1)
    100
    """
    return int(100 / n)
```


# Exercises

1. Two of Python’s built-in functions are min and max. In the Python shell,
execute the following function calls:
a. min(2, 3, 4)
```
>>> min(2, 3, 4)
2
```
b. max(2, -3, 4, 7, -9)
```
>>> max(2, -3, 4, 7, -9)
7
```
c. max(2, -3, min(4, 7), -5)
```
>>> max(2, -3, min(4, 7), -5)
4
```


2. For the following function calls, in what order are the subexpressions evaluated?  

a. min(max(3, 4), abs(-5))  
```
min(4, 5)
4  
```  

b. abs(min(4, 6, max(2, 8)))  
```
abs(min(4, 6, 8))  
abs(4)  
4  
```
c. round(max(5.572, 3.258), abs(-2))  
```
round(max(5.572, 3.258), 2)  
round(5.572, 2)  
5.72  
```
3. Following the function design recipe, define a function that has one parameter, a number, and returns that number tripled.
```
1. Examples --> write examples  
triple(3)  
9  
2. Header --> think of parameter names and what kind they are and the kind of output you suspect  
def triple(value: int) -> int:  

3. Description --> Write a short detail what the function does with some examples  
""" this wil triple the value  
4. Body --> Write the code  

def triple(number: int) -> int:
    """ this wil triple the value
    """
    return number * 3


5. Test --> Test your code

>>> triple(3)
9
>>> triple(4)
12
>>> triple(5)
15
```


4. Following the function design recipe, define a function that has two parameters, both of which are numbers, and returns the absolute value of the difference of the two. Hint: Call built-in function abs.

```
1. Examples --> write examples  
difference(2,4)
2

2. Header --> think of parameter names and what kind they are and the kind of output you suspect  
def difference(number1: int, number2 int) -> int:

3. Description --> Write a short detail what the function does with some examples  
    """
    absolute value of the difference between the 2
    difference(2,4)
    2
    """
4. Body --> Write the code  
def difference(number1: int, number2: int) -> int:
    """
    absolute value of the difference between the 2 numbers
    difference(2,4)
    2
    """
    return abs(number1 - number2)
    


5. Test --> Test your code
>>> difference(2,8)
6
>>> difference(2,4)
2

```

5. Following the function design recipe, define a function that has one parameter, a distance in kilometers, and returns the distance in miles. (There are 1.6 kilometers per mile.)

```
1. Examples --> write examples  
convert_to_miles(40)

2. Header --> think of parameter names and what kind they are and the kind of output you suspect  
def convert_to_miles(miles: float) -> float 


3. Description --> Write a short detail what the function does with some examples  
    """
    Converts the kilometers into miles

    example:
    convert_to_miles(40)
    """

4. Body --> Write the code  
def convert_to_miles(km: float) -> float:
    """
    Converts the kilometers into miles

    example:
    convert_to_miles(40)
    """
    return km / 1.6


5. Test --> Test your code
>>> convert_to_miles(40)
25.0
>>> convert_to_miles(43)
26.875

```

6. Following the function design recipe, define a function that has three parameters, grades between 0 and 100 inclusive, and returns the average of those grades.

```
1. Examples --> write examples  
average_grade(37.5, 4, 5.2)

2. Header --> think of parameter names and what kind they are and the kind of output you suspect  
def average_grade(grade1: float, grade2: float, grade3: float) -> float:

3. Description --> Write a short detail what the function does with some examples  
    """
    Calculates the average grade between the 3 grades given between 0 and 100

    example:
    average_grade(37.5, 4, 5.2)
    """

4. Body --> Write the code  
def average_grade(grade1: float, grade2: float, grade3: float) -> float:
    """
    Calculates the average grade between the 3 grades given between 0 and 100

    example:
    average_grade(37.5, 4, 5.2)
    15.57
    """
    return round((grade1 + grade2 + grade3)/3, 2)


5. Test --> Test your code
>>> average_grade(37.5, 4, 5.2)
15.57
```

7. Following the function design recipe, define a function that has four parameters, all of them grades between 0 and 100 inclusive, and returns the average of the best 3 of those grades. Hint: Call the function that you defined in the previous exercise.

Calling the other function was to complex in my opinion
```
1. Examples --> write examples  
average_grade_best_three(37.5, 4, 5.2, 4)

2. Header --> think of parameter names and what kind they are and the kind of output you suspect  
def average_grade_best_three(grade1: float, grade2: float, grade3: float, grade4: float) -> float:

3. Description --> Write a short detail what the function does with some examples  
    """
    Calculates the average grade between the 3 highest grades given between 0 and 100

    example:
    average_grade_best_three(37.5, 4, 5.2, 4)
    """

4. Body --> Write the code  
def average_grade_best_three(grade1: float, grade2: float, grade3: float, grade4: float) -> float:
    """
    Calculates the average grade between the 3 grades given between 0 and 100

    example:
    average_grade_best_three(37.5, 4, 5.2, 4)
    15.57
    """
    total_grade = (grade1 + grade2 + grade3 + grade4) 
    lowest_grade = min (grade1, grade2, grade3, grade4)
    
    return round((total_grade - lowest_grade) / 3, 2)


5. Test --> Test your code
>>> average_grade_best_three(50, 60, 70, 80)
70.0
```

8. Complete the examples in the docstring and then write the body of the following function:
```
1. Examples --> write examples  
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2

2. Header --> think of parameter names and what kind they are and the kind of output you suspect  
def weeks_elapsed(day1: int, day2: int) -> int:

3. Description --> Write a short detail what the function does with some examples  
    """
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    >>> weeks_elapsed(40, 61)
    """

4. Body --> Write the code  
def weeks_elapsed(day1: int, day2: int) -> int:
    """
    def weeks_elapsed(day1, day2): (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    >>> weeks_elapsed(40, 61)
    """
    max_day = max(day1, day2)
    min_day = min(day1, day2)
    days_in_between = max_day - min_day
    return days_in_between // 7


This is not the solution of the book
def weeks_elapsed(day1, day2):
    """ (int, int) -> int
    day1 and day2 are days in the same year. Return the number of full weeks
    that have elapsed between the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    return int(abs(day1 - day2) / 7)



5. Test --> Test your code
>>> weeks_elapsed(3, 20)
2
>>> weeks_elapsed(20, 3)
2
>>> weeks_elapsed(8, 5)
0
>>> weeks_elapsed(40, 61)
3
```

9. 
```
def square(num):
    """ 
    (number) -> number
    Return the square of num.
    >>> square(3)
    9
    """
```


Parameter: num    
Argument: 3   
Function name:  square  
Function call: square(3)  

10. Write the body of the square function from the previous exercise.
```
1. Examples --> write examples  
square(3)
    9
2. Header --> think of parameter names and what kind they are and the kind of output you suspect  
def square(number: int) -> int:
3. Description --> Write a short detail what the function does with some examples  
    """ 
    (number) -> number
    Return the square of num.
    >>> square(3)
    9
    """
4. Body --> Write the code  
def square(number: int) -> int:
    """ 
    (number) -> number
    Return the square of num.
    >>> square(3)
    9
    """
    return number ** 2

5. Test --> Test your code
>>> square(3)
9

```
