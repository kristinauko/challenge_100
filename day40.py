"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in 
chronological order, write a function that calculates the maximum profit 
you could have made from buying and selling that stock once. You must buy 
before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you 
could buy the stock at 5 dollars and sell it at 10 dollars.

"""


def buy_and_sell(l):
    """Take a list of integers and return max_profit"""

    max_profit, current_max = 0, 0 

    for price in reversed(l):                           #loop through reversed list
        current_max = max(current_max, price)           #get current maximum - compare current maximum with current price
        potential_profit = current_max - price          #get potential profit - current maximum minus current price
        max_profit = max(potential_profit, max_profit)  #get max of profit

    return max_profit


print(buy_and_sell([9, 11, 8, 5, 7, 10])) #5
print(buy_and_sell([])) #0
print(buy_and_sell([1])) #0
print(buy_and_sell([1, 2, 8, 1])) #7


