"""
Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output 
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected 
output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def product(int_list):
    """Take array of integers, return new array in which each element at 
    index i is the product of all the numbers in the 
    original array except the one at i"""

    new_list = []

    for i in int_list:
        product = 1

        for j in int_list:     
            if j != i:
                product = product * j
        new_list.append(product)

    return new_list

print(product([1, 2, 3, 4, 5]))
print(product([3, 2, 1]))