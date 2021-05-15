# Determine if array is monolitic. If it increases or decreses but not both

# O(n) time | O(1) space

def isMonotonic(array):
    if not array or len(array) == 1:
        return True
    for i in range(len(array)):
        if array[i] > array[len(array) -  1]:
            if array[i] > array[i+1] or array[i] == array[i+1]:
                continue
            else:
                return False

        if array[i] < array[len(array) -  1]:
            print(array[i], array[i+1])
            if array[i] < array[i+1] or array[i] == array[i+1]:
                continue
            else:
                return False

    return True


# def isMonotonic(array):
#     isNotIncreasing = True
#     isNotDecreasing = True

#     for i in range(1, len(array)):
#         if array[i] < array[i - 1]:
#             isNotDecreasing = False
#         if array[i] > array[i - 1]:
#             isNotIncreasing = False

#   return isNotDecreasing or isNotDecreasing


print(isMonotonic([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]))


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = []
        self.assertEqual(isMonotonic(array), True)

    def test_case_2(self):
        array = [1]
        self.assertEqual(isMonotonic(array), True)

    def test_case_3(self):
        array = [1, 2]
        self.assertEqual(isMonotonic(array), True)

    def test_case_4(self):
        array = [2, 1]
        self.assertEqual(isMonotonic(array), True)

    def test_case_5(self):
        array = [1, 5, 10, 1100, 1101, 1102, 9001]
        self.assertEqual(isMonotonic(array), True)

    def test_case_6(self):
        array = [-1, -5, -10, -1100, -1101, -1102, -9001]
        self.assertEqual(isMonotonic(array), True)

    def test_case_7(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        self.assertEqual(isMonotonic(array), True)

    def test_case_8(self):
        array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
        self.assertEqual(isMonotonic(array), False)

    def test_case_9(self):
        array = [1, 2, 0]
        self.assertEqual(isMonotonic(array), False)

    def test_case_10(self):
        array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
        self.assertEqual(isMonotonic(array), False)

    def test_case_11(self):
        array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
        self.assertEqual(isMonotonic(array), True)

    def test_case_12(self):
        array = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11]
        self.assertEqual(isMonotonic(array), False)

    def test_case_13(self):
        array = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]
        self.assertEqual(isMonotonic(array), True)

    def test_case_14(self):
        array = [-1, -1, -1, -1, -1, -1, -1, -1]
        self.assertEqual(isMonotonic(array), True)

if __name__ == "__main__":
    unittest.main()