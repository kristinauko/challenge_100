"""Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W,
 without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", 
"kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right 
letters, they are not in the right order.

The word "kangaroo" is the longest word in D, but it isn't a subsequence of S."""


def find_longest(s, d):
	"""Take string, set of words and find the longest word of set which is in the string"""

	word_dict = {}
	longest_word = ""
	

	for word in d: 
		current_word = ''	
		j = 0
		for letter in word: 

			for i in range(j, len(s)): 

				if letter == s[i]: 
					current_word += letter 
					j = i                  
					break
				else:				
					continue        

		if (current_word) == word and len(longest_word) < len(current_word):
			longest_word = current_word

		else:
			continue

	return longest_word



print(find_longest("abppplee", {"able", "ale", "apple", "bale", "kangaroo"}))
print(find_longest("helozolomrsociolalalapiath", {"th", "hello", "sociopath"}))
