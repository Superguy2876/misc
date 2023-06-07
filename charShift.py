

import sys
import math

"""You will see a sequence of characters separated by spaces.
The script is made as a sequence:
- A character representing the direction of movement (> starting from|< coming from)
- A number of moves to be made
- A reference character from which to make the displacement
Example:
>2T : 2 displacements starting from the character T = U
<5S : 5 displacements coming from the character S = N
Example
Input
>1G <3H <5Q >7E <3R
Output
HELLO
"""
def charShift(char_list: str):
    """
    :param char_list: list of characters
    :return: list of characters with displacement
    """
    # Initialize variables
    char_list = char_list.split()
    moves = []
    for i in char_list:

        moves.append((i[0], i[-1], int(i[1:-1])))
    
    # Initialize list of characters
    output = ''
    # Loop through the list of characters
    for i in (moves):
        if i[0] == '>':
            output += chr(ord(i[1]) + i[2])
        elif i[0] == '<':
            output += chr(ord(i[1]) - i[2])
    return output
