"""

Solution 2 - O(n lon n)

Given a list of integers, return the largest product 
that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we 
should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def largest_product1(l): 
    """Take array of integers and return the largest product of three"""

    l.sort()

    return max(l[-1] * l[-2] * l[-3], l[0] * l[1] * l[-1])


print(largest_product1([-10, -10, 5, 2]))
print(largest_product1([-10, -1, 5, 2]))
print(largest_product1([-1, -1, 5, 2, 8, 10, 100]))