# O(log(n)) time and O(log(n)) space
# recursive solution:
def shiftedBinarySearch(array, target):
    return helper(array, target, 0, len(array) - 1)

def helper(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    potentialMatch = array[mid]
    leftNum = array[left]
    rightNum = array[right]

    if target == potentialMatch:
        return mid
    elif leftNum <= potentialMatch:
        if target < potentialMatch and target >= leftNum:
            return helper(array,target,left, mid-1)
        else:
            return helper(array, target, mid + 1, right)
    else:
        if target > potentialMatch and target <= rightNum:
            return helper(array,target, mid+1, right)
        else:
            return helper(array, target, left, mid-1)


# O(log n) time | O(1) space
# iterative solution
# def shiftedBinarySearch(array, target):
#     return helper(array, target, 0, len(array) - 1)

# def helper(array, target, left, right):
#     while left <= right:
#         mid = (left + right) // 2
#         potentialMatch = array[mid]
#         leftNum = array[left]
#         rightNum = array[right]
#         if potentialMatch == target:
#             return mid
#         if leftNum <= potentialMatch:
#             if target < potentialMatch and target >= leftNum:
#                 right = mid -1
#             else:
#                 left = mid + 1
#         else:
#             if target > potentialMatch and target <= rightNum:
#                 left = mid+1
#             else:
#                 right = mid -1

#     return -1


array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
target = 33

print(shiftedBinarySearch(array, target))


# Add, edit, or remove tests in this file.
# Treat it as your playground!


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(shiftedBinarySearch([5, 23, 111, 1], 111), 2)

    def test_case_2(self):
        self.assertEqual(shiftedBinarySearch([111, 1, 5, 23], 5), 2)

    def test_case_3(self):
        self.assertEqual(shiftedBinarySearch([23, 111, 1, 5], 35), -1)

    def test_case_4(self):
        self.assertEqual(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 45], 33), 8)

    def test_case_5(self):
        self.assertEqual(shiftedBinarySearch([61, 71, 72, 73, 0, 1, 21, 33, 45, 45], 33), 7)

    def test_case_6(self):
        self.assertEqual(shiftedBinarySearch([72, 73, 0, 1, 21, 33, 45, 45, 61, 71], 72), 0)

    def test_case_7(self):
        self.assertEqual(shiftedBinarySearch([71, 72, 73, 0, 1, 21, 33, 45, 45, 61], 73), 2)

    def test_case_8(self):
        self.assertEqual(shiftedBinarySearch([73, 0, 1, 21, 33, 45, 45, 61, 71, 72], 70), -1)

    def test_case_9(self):
        self.assertEqual(shiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 355, 0, 1, 21], 355), 7)

    def test_case_10(self):
        self.assertEqual(shiftedBinarySearch([33, 45, 45, 61, 71, 72, 73, 355, 0, 1, 21], 354), -1)
