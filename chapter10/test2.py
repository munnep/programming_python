with open('test/file_example.txt', 'r') as file:
    contents = file.read() 
    
print(contents.strip())