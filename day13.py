"""
Count the number of prime numbers less than a non-negative number, n.
"""


def countPrimes(n):
	""" Take number n and count the number of prime numbers"""
    count = 0
    
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            count += 1

    return count

print(countPrimes(10)) # 4

