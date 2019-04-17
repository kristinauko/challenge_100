"""Given an array of integers, find the first missing positive integer in 
linear time and constant space. In other words, find the lowest positive 
integer that does not exist in the array. The array can contain duplicates 
and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input 
[1, 2, 0] should give 3.
"""

def first_missing(int_list):
    """Given an array of integers, find the first missing positive integer in 
linear time and constant space"""

    if len(int_list) == 0:
        return 1
        
    int_list.sort()
    smallest_int = 0
    
    for i in range(len(int_list) - 1):

        if int_list[i] <= 0 or int_list[i] == int_list[i + 1]:
            continue
        else:
            if int_list[i + 1] - int_list[i] != 1:
                smallest_int = int_list[i] + 1
                return smallest_int
    
    if smallest_int == 0:
        smallest_int = int_list[-1] + 1

    return smallest_int
    


print(first_missing([3, 3, 4, 4, -1, 1])) 
print(first_missing([1, 1, 3, 4, -1, 1]))
print(first_missing([1, 2, 3, 4, 5, 6]))
print(first_missing([3, 4, -1, 1]))
print(first_missing([1, 2, 0]))
print(first_missing([]))