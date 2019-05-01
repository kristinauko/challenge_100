"""In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, 
then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
"""

def collect_fruit(trees):
	"""Take a list of trees and return maximum fruit amount which you can gather"""

	basket1, basket2, count1, count2, previous, maximum = None, None, 0, 0, 0, 0

	for fruit in trees:

		if fruit == basket2:
			count2, previous = count2 + 1, previous + 1

		elif fruit == basket1:
			basket1, basket2, count1, count2, previous = basket2, basket1, count2, count1 + 1, 1

		else:

			basket1, basket2, count1, count2, previous = basket2, fruit, previous, 1, 1

		maximum = max(maximum, count1 + count2)

	return maximum


print(collect_fruit([1,2,1]))
print(collect_fruit([0,1,2,2]))
print(collect_fruit([1,2,3,2,2]))
print(collect_fruit([3,3,3,1,2,1,1,2,3,3,4]))


