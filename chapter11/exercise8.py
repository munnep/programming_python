# A balanced color is one whose red, green, and blue values add up to 1.0. Write a function called is_balanced that takes a dictionary whose keys are 'R', 'G', and 'B' and whose values are between 0 and 1 as input and that returns True if they represent a balanced color.

def is_balanced(colors):

    values = list(colors.values())
    total = sum(values)

    return print(total == 1.0)

colors1 = {'R': 0.3, 'G': 0.5, 'B': 0.2}

colors2 = {'R': 0.1, 'G': 0.5, 'B': 0.2}

is_balanced(colors1)
is_balanced(colors2)