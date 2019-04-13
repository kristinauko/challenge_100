

"""Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice."""


def twoSum(nums, target):
    """Take an array of integers, return indices of the two numbers such that 
they add up to a specific target"""
    
    list_of_indexes = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                list_of_indexes.append(i)
                list_of_indexes.append(j)
                return list_of_indexes


print(twoSum([3, 4, 7, 10], 17))

"""
LeetCode review:
Runtime: 5728 ms, faster than 11.52% of Python3 online submissions for Two Sum.
Memory Usage: 13.7 MB, less than 33.18% of Python3 online submissions for Two Sum.
"""