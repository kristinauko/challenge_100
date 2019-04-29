"""Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same 
character but a character may map to itself.

"""


def isIsomorphic(s, t):
    """Given two strings s and t, determine if they are isomorphic."""
        
    dict_s = {}
    dict_t = {}
    
    for i, value in enumerate(s):
        dict_s[value] = dict_s.get(value, []) + [i]
            
    for j, value in enumerate(t):
        dict_t[value] = dict_t.get(value, []) + [j]
    
    if sorted(dict_s.values()) == sorted(dict_t.values()):
        return True
    else:
        return False

print(isIsomorphic("egg", "add"))