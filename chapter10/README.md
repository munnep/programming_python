reading and printing a file
```
file = open('file_example.txt', 'r') 
contents = file.read()
file.close()
print(contents)
```

prefer to using the with statement
```
with open('file_example.txt', 'r') as file:
    contents = file.read() 
print(contents)
```

get your current directory
```
>>> import os
>>> os.getcwd()
'/Users/patrick/git/programming_python/chapter10'
```

read the first 10 characters of a file and then the rest
```
with open('./test/file_example.txt', 'r') as file:
    first_ten_chars = file.read(5)
    contents = file.read() 
print(first_ten_chars)
print(contents)
```

This example reads the contents of a file into a list of strings and then prints that list:
```
with open('file_example.txt', 'r') as example_file: 
    lines = example_file.readlines()
print(lines)
```
output:
```
['First line of text.\n', 'Second line of text.\n', 'Third line of text.\n']
```

write to a file
```
with open('topics.txt', 'w') as output_file: 
    output_file.write('Computer Science')
```

for line in file
```
with open('planets.tx', 'r') as data_file:
    for line in data_file:
    print(len(line.strip()))
```    




Exercises

1. Write a program that makes a backup of a file. Your program should prompt the user for the name of the file to copy and then write a new file with the same contents but with .bak as the file extension.
`exercise1.py`

2. Suppose the file alkaline_metals.txt contains the name, atomic number, and atomic weight of the alkaline earth metals:
```
    beryllium 4 9.012
    magnesium 12 24.305
    calcium 20 20.078
    strontium 38 87.62
    barium 56 137.327
    radium 88 226
```

Write a for loop to read the contents of alkaline_metals.txt and store it in a list of lists, with each inner list containing the name, atomic number, and atomic weight for an element. (Hint: Use string.split.)
`exercise2.py`

3. All of the file-reading functions we have seen in this chapter read forward through the file from the first character or line to the last. How could you write a function that would read backward through a file?
`exercise3.py`

4. In Processing Whitespace-Delimited Data, on page 192, we used the “For Line in File” technique to process data line by line, breaking it into pieces using string method split. Rewrite function process_file to skip the header as normal but then use the Read technique to read all the data at once.
`exercise4.py`

5. Modify the file reader in read_smallest_skip.py of Skipping the Header, on page 188 so that it can handle files with no data after the header.
`exercise5.py`

6. Modify the file reader in read_smallest_skip.py of Skipping the Header, on page 188, so that it uses a continue inside the loop instead of an if. Which form do you find easier to read?
`exercise6.py`

7. Modify the PDB file reader of Multiline Records, on page 195, so that it ignores blank lines and comment lines in PDB files. A blank line is one that contains only space and tab characters (that is, one that looks empty when viewed). A comment is any line beginning with the keyword CMNT.



