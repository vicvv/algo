# Given array of coins and target money write a function that returns the
# number of way in which you can combine coins to get the target money

def numberOfWaysToMakeChange(n, coins):
    #ways = [0 for i in range(n+1)]
    ways = [1] + [0] * n
    #ways[0] = 1
    for coin in coins:
        for ammount in range(1, n + 1):
            if coin <= ammount:
                ways[ammount] += ways[ammount - coin] 
    return ways[n]

print(numberOfWaysToMakeChange(10,[1,5,10,25]))

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(numberOfWaysToMakeChange(0, [2, 3, 4, 7]), 1)

    def test_case_2(self):
        self.assertEqual(numberOfWaysToMakeChange(9, [5]), 0)

    def test_case_3(self):
        self.assertEqual(numberOfWaysToMakeChange(7, [2, 4]), 0)

    def test_case_4(self):
        self.assertEqual(numberOfWaysToMakeChange(6, [1, 5]), 2)

    def test_case_5(self):
        self.assertEqual(numberOfWaysToMakeChange(4, [1, 5, 10, 25]), 1)

    def test_case_6(self):
        self.assertEqual(numberOfWaysToMakeChange(5, [1, 5, 10, 25]), 2)

    def test_case_7(self):
        self.assertEqual(numberOfWaysToMakeChange(10, [1, 5, 10, 25]), 4)

    def test_case_8(self):
        self.assertEqual(numberOfWaysToMakeChange(25, [1, 5, 10, 25]), 13)

    def test_case_9(self):
        self.assertEqual(numberOfWaysToMakeChange(12, [2, 3, 7]), 4)

    def test_case_10(self):
        self.assertEqual(numberOfWaysToMakeChange(7, [2, 3, 4, 7]), 3)
    def test_case_11(self):
        self.assertEqual(numberOfWaysToMakeChange(10, [10]), 1)

if __name__ == "__main__":
    unittest.main()
