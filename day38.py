"""

Given an array nums of n integers, are there elements a, b, c in nums such 
that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

def find_triplet(nums):
    """Given array, find find all unique sets which sum up to 0"""

    unique_lists = []
    num_list = []

    if len(nums) >= 3: 

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):

                for g in range(i+2, len(nums)):

                    if nums[i] + nums[j] + nums[g] == 0:

                        num_list.append(nums[i])
                        num_list.append(nums[j])
                        num_list.append(nums[g])

                        num_list.sort()

                        if num_list not in unique_lists:

                            unique_lists.append(num_list)

                        num_list = []

        if unique_lists == []:
            return None

        return unique_lists

    else:
        return None



print(find_triplet([-1, 0, 1, 2, -1, -4]))
print(find_triplet([-1, 0, 1]))
print(find_triplet([1]))
print(find_triplet([1, 5, 6, 8]))




