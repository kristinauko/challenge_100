"""

Given a N by M matrix of numbers, print out the matrix line by line:
forward > backwards > forward >...

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
9
8
7
6
11
12
13
14
15
20
19
18
17
16
"""


def print_matrix(numbers):
    """Take matrix and print it line by line: forward > backwards > forward >..."""

    positive = True 
    
    for line in numbers:

        if positive == True: 
            i = 0
            while i < len(line):
                print(line[i])
                i += 1
            positive = False

        else: 
            i = -1
            while i > -1 * len(line) - 1:
                print(line[i])
                i = i - 1
            positive = True


print_matrix([[1,  2,  3,  4,  5],
             [6,  7,  8,  9,  10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20]])

print_matrix([[],
             [],
             [],
             []])
