"""
Given a array find equilibrium index. If it does not exist, return 1.

"""


def equilibrium(a):
  """Take the array and return the index of equilibrium"""

  if len(a) == 0:
    return -1

  left_sum = 0

  for i in range(len(a) - 1):

    right_sum = 0
    middle_point = i + 1
    left_sum += a[i]

    for j in range(middle_point + 1, len(a)):
      right_sum += a[j]

    if left_sum == right_sum:
      return middle_point
  
  return -1

print(equilibrium([1,4,2,0,3,8,-4])) #3 
print(equilibrium([])) #-1