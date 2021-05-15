'''the function returns the index of the integer if it is located in the given array'''


'''# non recursive solution
def binarySearch(array, target):
    left = 0
    right = len(array) -1 
    while left <= right:
        middle = (left + right) // 2
        if target == array[middle]:
            return middle
        elif target > array[middle]:
            left = middle +1
        elif target < array[middle]:
            right = middle - 1
        else:
            return -1
    return -1
            '''

# recursive solution

def binarySearch (array, target):
    return bshelper(array, target, 0, len(array) - 1 )

def bshelper(array, target, left, right):
    if left > right:
        return - 1
    mid = (left + right) >> 1
    # mid = (left + right) // 2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return bshelper(array, target, left, mid - 1)
    
    else:
        return bshelper(array, target, mid+1, right)


arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
tar = 33
print(binarySearch(arr,tar))

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch([1, 5, 23, 111], 111), 3)

    def test_case_2(self):
        self.assertEqual(binarySearch([1, 5, 23, 111], 5), 1)

    def test_case_3(self):
        self.assertEqual(binarySearch([1, 5, 23, 111], 35), -1)

    def test_case_4(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

    def test_case_5(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 72), 8)

    def test_case_6(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73), 9)

    def test_case_7(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 70), -1)

    def test_case_8(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 355), 10)

    def test_case_9(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 354), -1)


if __name__ == "__main__":
    unittest.main()