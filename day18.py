
"""Given an integer, write a function to determine if it is a power of three."""

def isPowerOfThree(n):
"""Take int and return true if it is a power of three, false - if it is not"""

    while n  > 3:
        n = n / 3

    return n == 1 or n == 3
    

print(isPowerOfThree(27)) #true
print(isPowerOfThree(45)) #false
print(isPowerOfThree(0)) #false