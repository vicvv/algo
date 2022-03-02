'''Write a function that takes in a sorted array of distinct integers and returns the first
index in the array that is equal to the value at that index. In other words, your function
should return the minimum index where index == array[index] .
If there is no such index, your function should return -1 .'''

# O(n) time | O(1) space - where n is the length of the input array
def indexEqualsValue(array):
    for index in range(len(array)):
        value = array[index]
        if index == value:
            return index
    return -1

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-5, -3, 0, 3, 4, 5, 9]
        expected = 3
        actual = indexEqualsValue(array)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()