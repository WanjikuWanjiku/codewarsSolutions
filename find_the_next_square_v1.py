"""
Complete the findNextSquare method that finds the next integral 
perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n 
such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 
hould be returned. You may assume the parameter is non-negative.

My solution calculates the square root then compares whether 
its whole number (int) squared is equal to the square. 

"""

import math

def find_next_square(sq):
    square_root = math.sqrt(sq)
    # Return the next square if sq is a square, -1 otherwise
    if int(square_root)**2 == sq:
        return (square_root + 1)**2
    else:
        return -1
