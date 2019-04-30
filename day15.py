"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""


def longestCommonPrefix(strs):
	"""Take list of strings and return the longest common prefix amongst an array of strings"""

    if not strs:
        return ""

    shortest = min(strs,key=len)

    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]

    return shortest 


print(longestCommonPrefix(["flower","flow","flight"])) #"fl"
print(longestCommonPrefix(["dog","racecar","car"]))