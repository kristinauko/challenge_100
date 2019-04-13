
"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def is_sum(list_of_numbers, k):
    """Take a list of numbers and integer k and return if any numbers in list add up to k"""

    for i in range(len(list_of_numbers)):
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[i] + list_of_numbers[j] == k:
                return True

    return False


print(is_sum([10, 15, 3, 7], 17))
print(is_sum([10, 10, 3, 7], 12))
print(is_sum([0, 0], 0))
