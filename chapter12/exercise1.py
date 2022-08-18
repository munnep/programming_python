def complement(sequence): 
    """ (str) -> str
    Return the complement of sequence.
    >>> complement('AATTGCCGT') 'TTAACGGCA'
    """
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'} 
    sequence_complement = ''

    for char in sequence:
        sequence_complement = sequence_complement + complement_dict[char]

    return sequence_complement

print(complement('AATTGCCGT'))