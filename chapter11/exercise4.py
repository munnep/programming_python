# . The PDB file format is often used to store information about molecules. A PDB file may contain zero or more lines that begin with the word AUTHOR (which may be in uppercase, lowercase, or mixed case), followed by spaces or tabs, followed by the name of the person who created the file. Write a function that takes a list of filenames as an input argument and returns the set of all author names found in those files.

def books(filenames):
    
    author_names = set()
    
    for filename in filenames:
        file = open(filename)
        
        for line in file:
            if line.lower().startswith('author'):
                author = line[6:].strip()
                author_names.add(author)
            # print(line)
    
    return print(author_names)

filenames = ['books1.pdb', 'books2.pdb']

books(filenames)