"""Design a stack that supports push, pop, peek, and retrieving the minimum 
element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
peek() -- Get the top element.
get_min() -- Retrieve the minimum element in the stack.

"""


class Stack(object):
    def __init__(self):
        self._stack = []

    def push(self, item):
        if self._stack == []:
            self._stack.append([item,item])
        else:
            self._stack.append([item, min(self._stack[-1][1], item)])

    def pop(self):
        self._stack.pop()


    def peek(self):
        return self._stack[-1][0]


    def is_empty(self):
        return self._stack == []


    def get_min(self):
        return self._stack[-1][1]


if __name__== "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(-1)
    stack.push(5)
    print(stack.get_min())
    print(stack.push(-2))
    print(stack.push(7))
    print(stack.peek())
    print(stack.get_min())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.push(-6))
    print(stack.get_min())
    print(stack.is_empty())

