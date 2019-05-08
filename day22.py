"""Write a program that prints the numbers from 1 to 15. But for multiples 
of three print “Fizz” instead of the number and for the multiples of five 
print “Buzz”. For numbers which are multiples of both three and five print 
“FizzBuzz”.
"""


def fizzBuzz(n):
	"""Takes integer and prints "Fizz", "Buzz", "FizzBuzz" or number"""

	for num in range(1, n+1):

		if num % 5 == 0 and num % 3 == 0:
			print("FizzBuzz")

		elif num % 5 == 0 and not num % 3 == 0:
			print("Buzz")

		elif num % 3 == 0 and not num % 5 == 0:
			print("Fizz")

		else:
			print(num)


fizzBuzz(20)