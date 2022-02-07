def pairs_sum_to_target(list1, list2, target):
  return [[i,j] for i in range(len(list1)) for j in range(len(list2)) if list1[i] + list2[j]==target]


import unittest



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        list1 = [1, -2, 4, 5, 9]
        list2 = [4, 2, -4, -4, 0]
        target = 5
        expected = [[0, 0], [3, 4], [4, 2], [4, 3]]
        result = pairs_sum_to_target(list1, list2, target)
        self.assertEqual(result, expected)

    def test_case_2(self):
        list1 = []
        list2 = []
        target = 5
        expected = []
        result = pairs_sum_to_target(list1, list2, target)
        self.assertEqual(result, expected)

    def test_case_3(self):
        list1 = [3, 4]
        list2 = [-2, 1]
        target = 5
        expected = [[1, 1]]
        result = pairs_sum_to_target(list1, list2, target)
        self.assertEqual(result, expected)

    def test_case_4(self):
        list1 = []
        list2 = []
        target = 0
        expected = []
        result = pairs_sum_to_target(list1, list2, target)
        self.assertEqual(result, expected)

    def test_case_5(self):
        list1 = [1, 2, 3, 4, 5, 6]
        list2 = [6, 5, 4, 3, 2, 1]
        target = -5
        expected = []
        result = pairs_sum_to_target(list1, list2, target)
        self.assertEqual(result, expected)

    def test_case_6(self):
        list1 = [1, 2, 3, 4, 5, 6]
        list2 = [6, 5, 4, 3, 2, 1]
        target = 7
        expected = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        result = pairs_sum_to_target(list1, list2, target)
        self.assertEqual(result, expected)

    def test_case_7(self):
        list1 = [-4, -5, 6, 7, 8, 0, -19]
        list2 = [7, 5, 7, 2, 3, 5, 6]
        target = 12
        expected = [[2, 6], [3, 1], [3, 5]]
        result = pairs_sum_to_target(list1, list2, target)
        self.assertEqual(result, expected)

    def test_case_8(self):
        list1 = [1, 2, 3]
        list2 = [-3, -3, -3]
        target = 0
        expected = [[2, 0], [2, 1], [2, 2]]
        result = pairs_sum_to_target(list1, list2, target)
        self.assertEqual(result, expected)