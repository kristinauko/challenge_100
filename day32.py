
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""


def isValid(s):
    valid_paren = {"[":"]", "{":"}", "(":")"}
    left_char = []
    
    for char in s:
        
        if char in valid_paren:
            left_char.append(char) 
        
        elif not left_char or valid_paren[left_char.pop()] != char:
            return False
        
    return not left_char

 
print(isValid("()")) #true
print(isValid("()[]{}")) #true
print(isValid("(]")) #false
print(isValid("([)]")) #false
print(isValid("{[]}")) #true