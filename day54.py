""" 
Find the index of the string at which the given substring starts, otherwise 
return None.

Examples: 
1) findIndex("hello people", "pe") -> 6
2) findIndex("hello people", "hll") -> None
"""

def findIndex(s, p):
    """Given the string and substring, return the index"""

    if len(p) > len(s):
        return None

    for i in range(len(s)):

        for j in range(len(p)):

            if s[i + j] == p[j] and j == len(p) - 1:
                return i
                
            elif s[i + j] != p[j]:
                break

    return None


print(findIndex("hello people", "pe"))
print(findIndex("", ""))
print(findIndex("hello people", "h"))
print(findIndex("hello world", "hello people"))
print(findIndex("hello people", "hll"))