'''given an array of integers and another array of three distinct integers. The first array is
guaranteed to only contain integers that are in the second array, and the second array represents a
desired order for the integers in the first array. For example, a second array of [x, y, z]
represents a desired order of [x, x, ..., x, y, y, ..., y, z, z, ..., z] in the first
array.
Write a function that sorts the first array according to the desired order in the second array.
The function should perform this in place (i.e., it should mutate the input array), and it shouldn't use
any auxiliary space (i.e., it should run with constant space: O(1) space).
Note that the desired order won't necessarily be ascending or descending and that the first array
won't necessarily contain all three integers found in the second array—it might only contain one or
two.'''

# O(n) time | O(1) space - where n is the length of the array
def threeNumberSort(array, order):
    valueCounts = [0, 0, 0]
    for element in array:
        orderIdx = order.index(element)
        valueCounts[orderIdx] += 1
    for i in range(3):
        value = order[i]
        count = valueCounts[i]
        numElementsBefore = sum(valueCounts[:i])
        for n in range(count):
            currentIdx = numElementsBefore + n
            array[currentIdx] = value
    return array

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 0, 0, -1, -1, 0, 1, 1]
        order = [0, 1, -1]
        expected = [0, 0, 0, 1, 1, 1, -1, -1]
        actual = threeNumberSort(array, order)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()