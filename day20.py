"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""

def reverse_vowels(string):

	vowels = ""

	for char in string:

		if char in "aeiouAEIOU":
			vowels += char

	new_string = ""

	for char in string:
		if char in "aeiouAEIOU":
			new_string += vowels[-1]
			vowels = vowels[:-1]

		else:
			new_string += char

	return new_string


print(reverse_vowels("hello")) #holle
print(reverse_vowels("leetcode")) #leotcede