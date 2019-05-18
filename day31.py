"""
Determine whether an integer is a palindrome. An integer is a palindrome 
when it reads the same backward as forward.
"""

def isPalindrome(x):
    """Take number and return True if it's a palindrome"""
    
    return str(x) == str(x)[::-1]


print(isPalindrome(121))
print(isPalindrome(-121))