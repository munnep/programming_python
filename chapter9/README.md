# Chapter 9

Using a loop
```
velocities = [0.0, 9.81, 19.62, 29.43]
for velocity in velocities:
    print('Metric:', velocity, 'm/sec;', 'Imperial:', velocity * 3.28, 'ft/sec')


Metric: 0.0 m/sec; Imperial: 0.0 ft/sec
Metric: 9.81 m/sec; Imperial: 32.1768 ft/sec
Metric: 19.62 m/sec; Imperial: 64.3536 ft/sec
Metric: 29.43 m/sec; Imperial: 96.5304 ft/sec    
```
```
for <<variable>> in <<list>>:
    <<block>>
    
```

string example
```
country = "Netherlands France Germany"
for ch in country:
    print(ch)

N
e
t
h
e
r
l
a
n
d
s
 
F
r
a
n
c
e
 
G
e
r
m
a
n
y    
```

looping over a range of numbers

```
for num in range(10):
    print(num)

0
1
2
3
4
5
6
7
8
9

```

list a range
```
list(range(3))

[0, 1, 2]
```

list a range with stop and start value
```
list(range(1, 5))
```

step size is default 1. You can change this by using a third argument. Can also be negative
```
list(range(2000, 2050, 4))
[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
>>> list(range(2050, 2000, -4))
[2050, 2046, 2042, 2038, 2034, 2030, 2026, 2022, 2018, 2014, 2010, 2006, 2002]
```

```
>>> total = 0
>>> for i in range(1, 11): 
...     total = total + i
...     print(total)
... 
1
3
6
10
15
21
28
36
45
55
```

double number in a list

```
values = [4, 10, 3, 8, -6]
for i in range(len(values)):
     print(i, values[i])


0 4
1 10
2 3
3 8
4 -6



values = [4, 10, 3, 8, -6]
for i in range(len(values)):
     values[i] = values[i] * 2

values
[8, 20, 6, 16, -12]

```

Parallel lists using indexes
```
metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]
for i in range(len(metals)):
    print(metals[i], weights[i])

Li 6.941
Na 22.98976928
K 39.0983
```

Nesting loops in loops
```
outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print(metal + halogen)

LiF
LiCl
LiBr
NaF
NaCl
NaBr
KF
KCl
KBr
```

Looping Over Nested Lists
```
elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
for inner_list in elements:
    for item in inner_list:
        print(item)

Li
Na
K
F
Cl
Br
```        


Looping Over Ragged Lists
```
info = [['Isaac Newton', 1643, 1727],
        ['Charles Darwin', 1809, 1882],
        ['Alan Turing', 1912, 1954, 'alan@bletchley.uk']] 
for item in info:
    print(len(item))

3
3
4
```

Looping Until a Condition Is Reached

```
while «expression»: 
    «block»
```

```
rabbits = 3
while rabbits > 0:
    print(rabbits)
    rabbits = rabbits - 1

3
2
1    
```

with user input

formula.py
```
text = ""
while text != "quit":
    text = input("Please enter a chemical formula (or 'quit' to exit): ") 
    if text == "quit":
        print("...exiting program") 
    elif text == "H2O":
        print("Water") 
    elif text == "NH3":
        print("Ammonia") 
    elif text == "CH4":
        print("Methane") 
    else:
        print("Unknown compound")
````

run
```
python formula.py 
Please enter a chemical formula (or 'quit' to exit): f
Unknown compound
Please enter a chemical formula (or 'quit' to exit): H20
Unknown compound
Please enter a chemical formula (or 'quit' to exit): H2O
Water
Please enter a chemical formula (or 'quit' to exit): quit
```

using the break
```
text = ""
while True:
    text = input("Please enter a chemical formula (or 'quit' to exit): ") 
    if text == "quit":
        print("...exiting program") 
        break
    elif text == "H2O":
        print("Water") 
    elif text == "NH3":
        print("Ammonia") 
    elif text == "CH4":
        print("Methane") 
    else:
        print("Unknown compound")
```







# excercises

1. Write a for loop to print all the values in the celegans_phenotypes list from Slicing Lists, on page 137, one per line. celegans_phenotypes refers to ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma'].
```
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
for i in celegans_phenotypes:
    print(i)

Emb
Him
Unc
Lon
Dpy
Sma    
```

2. Write a for loop to print all the values in the half_lives list from Operations on Lists, on page 135, all on a single line. half_lives refers to [87.74, 24110.0, 6537.0, 14.4, 376000.0].
```
half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
for i in half_lives:
    print(i)

87.74
24110.0
6537.0
14.4
376000.0
```    

3. Write a for loop to add 1 to all the values from whales from Storing and Accessing Data in Lists, on page 129, and store the converted values in a new list called more_whales. The whales list shouldn’t be modified. whales refers to [5,4,7,3,2,3,2,6,4,2,1,7,1,3].
```
whales = [5,4,7,3,2,3,2,6,4,2,1,7,1,3]
more_whales = []

for value in whales:
    more_whales.append(value + 1)


```

4. In this exercise, you’ll create a nested list and then write code that per- forms operations on that list.

a. Create a nested list where each element of the outer list contains the atomic number and atomic weight for an alkaline earth metal. The values are beryllium (4 and 9.012), magnesium (12 and 24.305), cal- cium (20 and 40.078), strontium (38 and 87.62), barium (56 and 137.327), and radium (88 and 226). Assign the list to variable alkaline_earth_metals.

```
alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.62], [56, 137.327], [88, 226]]

```



b. Write a for loop to print all the values in alkaline_earth_metals, with the atomic number and atomic weight for each alkaline earth metal on a different line.

My answer:
```
alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.62], [56, 137.327], [88, 226]]

for inner_list in alkaline_earth_metals:
    for item in inner_list:
        print(item)
```

Book answer:
```
for inner_list in alkaline_earth_metals:
 print(inner_list[0])
 print(inner_list[1])
```
same result


c. Write a for loop to create a new list called number_and_weight that contains the elements of alkaline_earth_metals in the same order but not nested.

My answer
```
alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.62], [56, 137.327], [88, 226]]
number_and_weight = []

for inner_list in alkaline_earth_metals:
    for item in inner_list:
        number_and_weight.append(item)

number_and_weight
[4, 9.012, 12, 24.305, 20, 40.078, 38, 87.62, 56, 137.327, 88, 226]
```        

Book answer:
```
number_and_weight = []
for inner_list in alkaline_earth_metals:
    number_and_weight.append(inner_list[0])
    number_and_weight.append(inner_list[1])
```

5. The following function doesn’t have a docstring, type annotations, or com- ments. Write enough of all three to make it easy for another programmer to understand what the function does and how, and then compare your solution with those of at least two other people. How similar are they? Why do they differ?

```
values = ["one", "two", "three"]

def mystery_function(values): 
    """
    This function returns the gives list and inner list in reversed order

    >>> mystery_function(["one", "two", "three"])
    [['e', 'n', 'o'], ['o', 'w', 't'], ['e', 'e', 'r', 'h', 't']]

    >>> mystery_function([["one", "two"],["three","four"]])
    """
    result = []
    for sublist in values: 
        result.append([sublist[0]]) 
        for i in sublist[1:]:
            result[-1].insert(0, i) 
    return result
```   

6. In Repetition Based on User Input, on page 162, you saw a loop that prompted users until they typed quit. This code won’t work if users type Quit, or QUIT, or any other version that isn’t exactly quit. Modify that loop so that it terminates if a user types that word with any capitalization.

```
text = ""
while text.lower() != "quit":
    text = input("Please enter a chemical formula (or 'quit' to exit): ") 
    if text == "quit":
        print("...exiting program") 
    elif text == "H2O":
        print("Water") 
    elif text == "NH3":
        print("Ammonia") 
    elif text == "CH4":
        print("Methane") 
    else:
        print("Unknown compound")
```

7. Consider the following statement, which creates a list of populations of countries in eastern Asia (China, DPR Korea, Hong Kong, Mongolia, Republic of Korea, and Taiwan) in millions: country_populations = [1295, 23, 7, 3, 47, 21]. Write a for loop that adds up all the values and stores them in variable total. (Hint: Give total an initial value of zero, and, inside the loop body, add the population of the current country to total.)

my answer
```
country_populations = [1295, 23, 7, 3, 47, 21]
total = 0

for population in country_populations: 
    total = total + population

total
```

book answer
```
country_populations = [1295, 23, 7, 3, 47, 21]
total = 0
for population in country_populations:
    total += population
```

8. You are given two lists, rat_1 and rat_2, that contain the daily weights of two rats over a period of ten days. Assume the rats never have exactly
the same weight. Write statements to do the following:

a. If the weight of rat 1 is greater than that of rat 2 on day 1, print "Rat 1 weighed more than rat 2 on day 1."; otherwise, print "Rat 1 weighed less than rat 2 on day 1.".

```
rat_1 = [201, 204, 205, 202, 203, 204, 204, 201, 204, 204]
rat_2 = [202, 202, 202, 203, 204, 205, 206, 207, 203, 205]

if rat_1[0] > rat_2[0]: 
    print("Rat 1 weighed more than rat 2 on day 1.")
else: 
    print("Rat 1 weighed less than rat 2 on day 1.")   
```

for i in range(len(rat_1)):

b. If rat 1 weighed more than rat 2 on day 1 and if rat 1 weighs more than rat 2 on the last day, print "Rat 1 remained heavier than Rat 2."; other- wise, print "Rat 2 became heavier than Rat 1."

```
rat_1 = [201, 204, 205, 202, 203, 204, 204, 201, 204, 204]
rat_2 = [202, 202, 202, 203, 204, 205, 206, 207, 203, 205]

if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
    print("Rat 1 remained heavier than Rat 2.")
else: 
    print("Rat 2 became heavier than Rat 1.")   
```

c. If your solution to the previous exercise used nested if statements, then do it without nesting, or vice versa.
```
if rat_1[0] > rat_2[0]:
    if rat_1[-1] > rat_2[-1]:
          print("Rat 1 remained heavier than Rat 2.")
    else:
          print("Rat 2 became heavier than Rat 1.")
else:
    print("Rat 2 became heavier than Rat 1.")
```    

9. Print the numbers in the range 33 to 49 (inclusive).

```
for num in range(33, 50):
    print(num)
```

10. Print the numbers from 1 to 10 (inclusive) in descending order, all on one line.
my answer --> wrong because descending order.....
```
for number in range(1, 11):
    print(number, end=' ')

1 2 3 4 5 6 7 8 9 10 >>>     
```    
book answer. so simple
```
for number in range(10):
    print(10 - number, end=' ')
```

11.  Using a loop, sum the numbers in the range 2 to 22 (inclusive), and then calculate the average.
```
total = 0
run = 0
for i in range(2, 23): 
    total = total + i
    run = run + 1

average = total / run
average
12
```

12. Consider this code:
```
from typing import List
def remove_neg(num_list: List[float]) -> None:
    """Remove the negative numbers from the list num_list.
    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numbers
    [1, 2]
    """
    for item in num_list: 
        if item < 0:
            num_list.remove(item)
```


When remove_neg([1, 2, 3, -3, 6, -1, -3, 1]) is executed, it produces [1, 2, 3, 6, -3, 1]. The for loop traverses the elements of the list, and when a negative value (like -3 at position 3) is reached, it is removed, shifting the subsequent values one position earlier in the list (so 6 moves into position 3). The loop then continues on to process the next item, skipping over the value that moved into the removed item’s position. If there are two negative numbers in a row (like -1 and -3), then the second one won’t be removed.
Rewrite the code to avoid this problem.

answer in the book and i just don't get it at the moment
```
def remove_neg(num_list):
    index = 0
    while index < len(num_list):
         if num_list[index] < 0:
            del num_list[index]
    else:
        index += 1
```

13. Using nested for loops, print a right triangle of the character T on the screen where the triangle is one character wide at its narrowest point and seven characters wide at its widest point:

my answer
```
letter = "T"
for i in range(8):
   if i < 7:
       print(letter)
       letter += "T"
```

book answer
```
for width in range(1, 8):
    print('T' * width)
```

14. Using nested for loops, print the triangle described in the previous exercise with its hypotenuse on the left side:

took me some time
```
for width in range(1, 8):
    print(' ' * (7 - width), 'T' * width, sep='')
```

15. Redo the previous two exercises using while loops instead of for loops.

```
number = 1
while number < 8:
    print("T" * number)
    number = number + 1
```

```
number = 1
while number < 8:
    print(' ' * (7 - number), 'T' * number, sep='')
    number = number + 1
```