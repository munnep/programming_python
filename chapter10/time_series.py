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