with open('./test/file_example.txt', 'r') as file:
    first_ten_chars = file.read(5)
    contents = file.read() 
print(first_ten_chars)
print(contents)