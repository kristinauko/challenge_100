"""
Given a sorted array nums, remove the duplicates in-place such that each 
element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of 
nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements 
of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""


def removeDuplicates(nums):
    """Given a sorted array, remove duplicates"""
 
 #Solution 1 - brute force

    # if nums == []:
    #     return 0
    
    # for i in range(len(nums) - 1): #o(n)
    #     if nums[i] == nums[i+1]:
    #         nums[i] = None
    
    # current = 0
    # next_valid = 0

    # while current < len(nums): 

    #     if nums[current] == None:
    #         next_valid = current + 1

    #         while next_valid < len(nums) and nums[next_valid] == None:
    #             next_valid += 1

    #         if next_valid < len(nums):
    #             nums[current] = nums[next_valid]
    #             nums[next_valid] = None

    #         else:
    #             break
        
    #     current += 1

    # return current 


#Solution 2 which is FASTER 

    for i in range (len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i-1]
    return len(nums)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1,2,2]))
