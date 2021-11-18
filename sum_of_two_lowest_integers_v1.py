"""
Create a function that returns the sum of the two lowest positive numbers 
given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], 
the output should be 7.

In my solution, I find the sum of the first two items in the 
sorted list. The list is sorted from smallest to largest therefore
the first two numbers are the smallest. 
"""

def sum_two_smallest_numbers(numbers):
    
    return (sum(sorted(numbers)[:2]))
    
    