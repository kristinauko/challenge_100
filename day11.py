
#1 EXERCISE
"""Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary : 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}""" 

def concatenate(dict1, dict2, dict3):
	"""Take three dictionaries and concatenate them to one"""

	new_dict = {}

	for value in (dict1, dict2, dict3):
		new_dict.update(value)

	return new_dict


#print(concatenate({1:10, 2:20}, {3:30, 4:40}, {5:50,6:60}))



#2 EXERCISE
"""Write a Python script to check if a given key already exists in a dictionary."""

def find_key(dictionary, key):
	"""Take dictionary and key, return True if key exists in dictionary"""

	if dictionary.get(key):
		return True
	else:
		return False


# print(find_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 3))
# print(find_key({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 9))



#3 EXERCISE
"""Write a Python program to iterate over dictionaries using for loops."""

def iterate_dictionary(dictionary):
	"""Take dictionary, iterate through it and print key - values pairs"""

	for i in dictionary:
		print(i, dictionary[i])


#iterate_dictionary({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})



# 4 EXERCISE 
""" Write a Python script to generate and print a dictionary that contains a number (between 1 and n) 
in the form (x, x*x). Go to the editor
Sample Dictionary ( n = 5) : 
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""

def generate_dict(num):
	"""Take number and generate dictionary which contains key - number and value - number^2"""

	new_dict = {}

	for i in range(1, num + 1):
		new_dict[i] = i * i

	return new_dict

#print(generate_dict(5))



#5 EXERCISE
"""Write a Python program to map two lists into a dictionary."""

def zip_lists(keys, values):
	"""Take two lists and return dictionary with key/value pairs"""

	return dict(zip(keys, values))

#print(zip_lists([1, 2, 3, 4, 5], ["a", "b", "c", "d", "e"]))