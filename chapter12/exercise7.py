from typing import List, Tuple

def dutch_flag(colors):
    """Return a tuple of the indices of the two smallest values in list L.
    >>> colors = ['red','blue','white','blue','white','red']
    >>> dutch_flag(colors)
    ['red', 'red', 'white', 'white', 'blue', 'blue']
    """
    color_flags = []

    color_red = []
    color_white = []
    color_blue = []
    for color in colors:
        if color == 'red':
            color_red.append(color)
        elif color == 'white':
            color_white.append(color)
        elif color == 'blue':
            color_blue.append(color)
    
    color_flags = color_red + color_white + color_blue


    # print(color_flags)
    return color_flags

print(dutch_flag(['red','blue','white','blue','white','red','red','red']))



if __name__ == '__main__': 
    # print('doctest is being executed')
    import doctest
    doctest.testmod()

