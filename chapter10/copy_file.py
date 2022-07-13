file = input("which file do you want to copy: ")

with open(file, 'r') as file:
    contents = file.read() 

with open('topics.txt', 'w') as output_file: 
    output_file.write(contents + '.bak')
