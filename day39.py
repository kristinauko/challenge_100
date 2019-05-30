"""

Given an array nums of n integers and an integer target, find three integers in nums such 
that the sum is closest to target. Return the sum of the three integers. You may assume 
that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


def closest_to_target(nums, target):
    """Given an array nums of n integers and an int target return the sum of 
    three integers which sum is closest to target"""

    if len(nums) >= 3: 

        closest_distance = target - nums[0]
        current_distance, max_sum = None, None

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for g in range(j+1, len(nums)):

                    num_sum = nums[i] + nums[j] + nums[g]
                    
                    if num_sum <= target:
                        current_distance = target - num_sum
                    elif num_sum > target:
                        current_distance = num_sum - target

                    if abs(current_distance) < abs(closest_distance):
                        closest_distance = current_distance
                        max_sum = num_sum

        return max_sum

    else:
        return None


print(closest_to_target([-1, 2, 1, -4], 1)) #2
print(closest_to_target([-1, 2, 1, -4], -5)) #-4
print(closest_to_target([], 1)) #None




