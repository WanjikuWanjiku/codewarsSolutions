"""
An isogram is a word that has no repeating letters, 
consecutive or non-consecutive. 
Implement a function that determines whether a string 
that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

My solution compares the length of the string with the length 
the string. If it is equal, it means no letter has been repeated,
hence, the string is an isogram. 

"""
def is_isogram(string):
    string = string.upper()
    return len(set(string)) == len(string)