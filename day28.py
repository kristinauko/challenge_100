"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of 
character insertions, deletions, and substitutions required to change one 
string to the other. For example, the edit distance between “kitten” and 
“sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, 
and append a “g”.

Given two strings, compute the edit distance between them.
"""

def edit_distance(string1, string2):
    """Take two strings and compute the edit distance between them"""

    if len(string1) > len(string2):
        difference = len(string1) - len(string2)
        string1[:difference]

    elif len(string2) > len(string1):
        difference = len(string2) - len(string1)
        string2[:difference]

    else:
        difference = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            difference += 1

    return difference

print(edit_distance("kitten", "sitting")) #3
print(edit_distance("medium", "median")) #2
