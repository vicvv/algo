def kadanesAlgorithm(array):
    maxEnding = array[0]
    maxFinal = array[0]

    for i in range(1, len(array)):
        maxEnding = max(array[i], maxEnding + array[i])
        maxFinal = max(maxFinal, maxEnding)
    return maxFinal 

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)


if __name__ == "__main__":
    unittest.main()