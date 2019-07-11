"""
Given a non-negative integer numRows, generate the first numRows of Pascal's 
triangle.


In Pascal's triangle, each number is the sum of the two numbers directly 
above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def pascal_triangle(num):

    final_list = []
    lst = 1

    for i in range(num): 

        interm_list = []
        interm_list.append(lst)

        for j in range(len(final_list) - 1):
            interm_list.append((final_list[-1][j] + final_list[-1][j+1]))

        if i != 0:
            interm_list.append(lst)

        final_list.append(interm_list)
  
    return final_list


print(pascal_triangle(5))
print(pascal_triangle(10))

