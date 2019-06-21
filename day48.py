"""
Given a list of integers, return the largest product 
that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we 
should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def largest_product(l):
    """Take a list and return the largest product of three integers"""

    maximum = l[1]

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(i+2, len(l)):

                maximum = max(l[i] * l[j] * l[k], maximum)

    return maximum


print(largest_product([-10, -10, 5, 2]))
print(largest_product([-10, -1, 5, 2]))
print(largest_product([-1, -1, 5, 2, 8, 10, 100]))





