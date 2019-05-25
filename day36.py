"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack

pop(), which pops off and returns the topmost element of the stack. 
If there are no elements in the stack, then it should throw an error or 
return null.

max(), which returns the maximum value in the stack currently. 
If there are no elements in the stack, then it should throw an error 
or return null.
"""

def createStack():
    """Create Stack

    >>> createStack()
    []
    """

    stack = []
    return stack


def push(stack, val):
    """Push value on the stack
    
    >>> stack = [1,2,3]
    >>> push(stack, 9)
    [1, 2, 3, 9]
    >>> len(stack)
    4

    """

    stack.append(val)
    return stack


def max(stack):
    """Returns max of stack
    >>> stack = [1, 2, 3, 9]
    >>> max(stack)
    9
    >>> stack = [1, 9, 8, 45, 0, 9]
    >>> max(stack)
    45

    """

    if len(stack) == 0:
        return null

    maxim = stack[0]

    for item in stack:
        if maxim < item:
            maxim = item

    return maxim 


#Proposed Solution

# class MaxStack:
#     def __init__(self):
#         self.stack = []
#         self.maxes = []

#     def push(self, val):
#         self.stack.append(val)
#         if self.maxes:
#             self.maxes.append(max(val, self.maxes[-1]))
#         else:
#             self.maxes.append(val)

#     def pop(self):
#         if self.maxes:
#             self.maxes.pop()
#         return self.stack.pop()

#     def max(self):
#         return self.maxes[-1]


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()




