"""
Given a string, determine if it is a palindrome, considering only alphanumeric 
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid 
palindrome."""

def is_palindrome(str):
	"""Takes a string and returns true if string is palindrome"""

	new_str = ""

	for char in str:
		if char in ".,?!:; ":
			continue
		else:
			new_str += char.lower()

	get_boolean = palindrome(new_str)
	return get_boolean


def palindrome(new_str):
	"""Takes string and checks if it's palindrome"""

	if new_str == '':
		return True

	if new_str[0]== new_str[-1]:
		return palindrome(new_str[1:-1])
	else:
		return False


print(is_palindrome("A man, a plan, a canal: Panama")) #TRUE 
print(is_palindrome("race a car")) #FALSE
