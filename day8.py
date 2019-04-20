"""Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell 
one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price."""


def most_profit(stock):
	"""Take a list of integers and decide when it's the best time to buy and sell, return the profit"""

	max_profit = 0

	for i in range(len(stock)):
		profit = 0

		for j in range(i+1, len(stock)):
			profit = stock[j] - stock[i]
			print(stock[j], stock[i])
			if  profit > max_profit:
				max_profit = profit

	return max_profit


print(most_profit([7,1,5,3,6,4])) #5
print(most_profit([7,6,4,3,1])) #0
print(most_profit([1,2])) #1

