'''
Given a pattern and a string str, find if str follows the same 
pattern.

Here follow means a full match, such that there is a bijection 
between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, 
and str contains lowercase letters that may be separated 
by a single space.

RESULT: 

Runtime: 32 ms, faster than 89.71% of Python3 online 
submissions for Word Pattern.

Memory Usage: 13.8 MB, less than 5.55% of Python3 online 
submissions for Word Pattern.

'''

def wordPattern(pattern, str):
        
    new_list = str.split(" ")
    
    if len(pattern) != len(new_list):
        return False
    
    d = {}
    
    for i in range(len(pattern)): 

        if pattern[i] not in d.keys():
            if new_list[i] not in d.values():
                d[pattern[i]] = new_list[i]
            else: 
                return False
        else:
            if d[pattern[i]] != new_list[i]:
                return False    
    return True


print(wordPattern("aaa", "aa aa aa aa")) # false
print(wordPattern("abba", "aa dog dog aa")) # true
print(wordPattern("aaaa", "aa dog dog aa")) # false
