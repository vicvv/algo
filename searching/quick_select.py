
# O(n) time and O(1) space

def quickselect(array, k):
    position = k - 1
    return helper(array, 0, len(array) - 1, position)


def helper(array, start, end, position):
    while True:
        if start > end:
            raise Exception ("bad place for algorithm")
        pivot = start
        left = start + 1
        right = end

        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(left, right, array)
            if array[left] <= array[pivot]:
                left += 1
            if array[right] >= array[pivot]:
                right -= 1
        swap(pivot, right, array)

        if right == position:
            return array[right]
        elif right < position:
            start = right + 1
        else:
            end = right - 1

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]




array = [8, 5, 2, 9, 7, 6, 3]
k = 3
print(quickselect(array,k))

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(quickselect([1], 1), 1)

    def test_case_2(self):
        self.assertEqual(quickselect([43, 24, 37], 1), 24)

    def test_case_3(self):
        self.assertEqual(quickselect([43, 24, 37], 2), 37)

    def test_case_4(self):
        self.assertEqual(quickselect([43, 24, 37], 3), 43)

    def test_case_5(self):
        self.assertEqual(quickselect([8, 5, 2, 9, 7, 6, 3], 3), 5)

    def test_case_6(self):
        self.assertEqual(quickselect([8, 3, 2, 5, 1, 7, 4, 6], 1), 1)

    def test_case_7(self):
        self.assertEqual(quickselect([8, 3, 2, 5, 1, 7, 4, 6], 2), 2)

    def test_case_8(self):
        self.assertEqual(quickselect([8, 3, 2, 5, 1, 7, 4, 6], 3), 3)

    def test_case_9(self):
        self.assertEqual(quickselect([8, 3, 2, 5, 1, 7, 4, 6], 4), 4)

    def test_case_10(self):
        self.assertEqual(quickselect([8, 3, 2, 5, 1, 7, 4, 6], 5), 5)

    def test_case_11(self):
        self.assertEqual(quickselect([8, 3, 2, 5, 1, 7, 4, 6], 6), 6)

    def test_case_12(self):
        self.assertEqual(quickselect([8, 3, 2, 5, 1, 7, 4, 6], 7), 7)

    def test_case_13(self):
        self.assertEqual(quickselect([8, 3, 2, 5, 1, 7, 4, 6], 8), 8)

    def test_case_14(self):
        self.assertEqual(quickselect([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 5), 25)

    def test_case_15(self):
        self.assertEqual(quickselect([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 4), 15)

    def test_case_16(self):
        self.assertEqual(quickselect([102, 41, 58, 81, 2, -5, 1000, 10021, 181, -14515, 25, 15], 9), 102)

    def test_case_17(self):
        self.assertEqual(
            quickselect([1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151125], 12),
            55516151125,
        )

    def test_case_18(self):
        self.assertEqual(
            quickselect([1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151125], 4), 123
        )
if __name__ == "__main__":
    unittest.main()