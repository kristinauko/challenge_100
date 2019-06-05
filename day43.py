'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

def searchRange(nums, target):
  """Given an array of integers, find the starting and ending 
  position of a given target value."""

  target_i = []
  start = -1
  end = -1

  for i in range(len(nums)):
      if target == nums[i] and start == -1:
          start = i
          end = i
      elif target == nums[i] and start != -1:
          end = i

  target_i.append(start)
  target_i.append(end)

  return target_i


#O(n)

print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
