# Say you have an array for which the i-th element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell 
# the stock before you buy again).
# Example 1:
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.


def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    pass

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2), 93)

if __name__ == "__main__":
    unittest.main()
