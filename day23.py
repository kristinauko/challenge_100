"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store
 integers within the 32-bit signed integer range: [−231,  231 − 1]. 
 For the purpose of this problem, assume that your function returns 
 0 when the reversed integer overflows.
"""


def reverse(x):
    """Take integer and reverse it, given limits [−2**31,  2**31 − 1]"""
    
    if x > 0:
        x = int(str(x)[::-1])

    elif x < 0:
        x = x * -1
        x = -1 * int(str(x)[::-1])

    if x < -2 ** 31 or x > 2 ** 31 - 1:
        return 0
        
    return x


print(reverse(123))
print(reverse(-123))
print(reverse(120))
