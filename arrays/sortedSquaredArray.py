'''
Write a function that 
takes in a non-empty array of integers that are sorted in ascending 
order and returns a new array of the same length with the squares of the
original integers also sorted in ascending order.

'''

array =[1,2,3,5,6,8,9]
def sortedSquaredArray(array):
    return [i**2 for i in array]

print(sortedSquaredArray(array))

import unittest

class TestProgram(unittest.TestCase):
    def test_case1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
