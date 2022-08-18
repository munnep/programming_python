# A DNA sequence is a string made up of the letters A, T, G, and C. To find the complement of a DNA sequence, As are replaced by Ts, Ts by As, Gs by Cs, and Cs by Gs. For example, the complement of AATTGCCGT is TTAACGGCA.

def dna_complement(dna):
    """Return the complement of DNA
    >>> dna = 'AATTGCCGT'
    >>> dna_complement(AATTGCCGT)
    'TTAACGGCA'
    
    split the string
    when T then A
    when A then T
    when G then C
    when C then G
    """
    dna_list=[]
    for letter in dna:
       if letter == 'T':
           dna_list.append('A')
       elif letter == 'A':
           dna_list.append('T')
       elif letter == 'G':
           dna_list.append('C')
       elif letter == 'C':
           dna_list.append('G')
    
    return str(dna_list)

print(dna_complement('AATTGCCGT'))    