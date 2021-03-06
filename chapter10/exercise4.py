from typing import TextIO 
from io import StringIO
def skip_header(reader: TextIO) -> str:
    """Skip the header in reader and return the first real piece of data.
    >>> infile = StringIO('Example\\n# Comment\\n# Comment\\nData line\\n')
    >>> skip_header(infile)
    'Data line\\n'
    """
    # Read the description line
    line = reader.readline()
    #Find the first non-comment line
    line = reader.readline() 
    while line.startswith('#'):
        line = reader.readline()
    # Now line contains the first real piece of data
    return line
    
def process_file(reader):
    """ (file open for reading) -> NoneType
    Read and print the data from reader, which must start with a single
    description line, then a sequence of lines beginning with '#', then a
    sequence of data.
    """
 
    # Find and print the first piece of data.
    line = skip_header(reader).strip()
    print(line)
 
    # Read the rest of the data.
    print(reader.read())    

if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        process_file(input_file)
 