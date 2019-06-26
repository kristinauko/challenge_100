"""
Given an array strings, determine whether it follows the sequence given in the 
patterns array. In other words, there should be no i and j for which 
strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which 
strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], 
the output should be areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the 
output should be areFollowingPatterns(strings, patterns) = false.
"""


def areFollowingPatterns(strings, patterns):
    
    if len(strings) != len(patterns):
        return False
    
    s_dict = {}
    p_set = set()
    s_set = set()
    
    for i in range(len(patterns)):

        p_set.add(patterns[i])
        s_set.add(strings[i])

        if patterns[i] not in s_dict.keys():
            s_dict[patterns[i]] = []
            
        keys = s_dict[patterns[i]]
        keys.append(strings[i])
        s_dict[patterns[i]] = keys

    if len(p_set) != len(s_set):
        return False   

    for values in s_dict.values():

        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False
    
    return True



print(areFollowingPatterns(["cat", 
 "dog", 
 "doggy"], ["a", 
 "b", 
 "b"])) #False

print(areFollowingPatterns(["cat", 
 "dog", 
 "dog"], ["a", 
 "b", 
 "b"])) #True 

print(areFollowingPatterns(["a", 
 "a", 
 "b"],["a", 
 "a", 
 "a"])) #False
