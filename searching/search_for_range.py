# return start and end index of target. apply binary search twice to fine left and right
# time|space

def searchForRange(array, target):
    finalrange = [-1,-1]
    alteredBS(array, target,0,len(array) - 1, finalrange, True)
    alteredBS(array, target,0,len(array) - 1, finalrange, False)
    return finalrange

def alteredBS(array, target, left, right, finalrange, goLeft):
	if left > right:
		return
	mid = (left + right) // 2	
	if array[mid] < target:
		alteredBS(array, target, mid+1, right, finalrange, goLeft)
	elif array[mid] > target:
		alteredBS(array, target, left, mid-1, finalrange,goLeft)
	else:
		if goLeft:
			if mid == 0 or array[mid - 1] != target:
				finalrange[0] = mid
			else:
				alteredBS(array, target, left, mid-1, finalrange, goLeft )
		else:
			if mid == len(array) - 1 or array[mid + 1] != target:
				finalrange[1] = mid
			else:
				alteredBS(array, target, mid+1, right, finalrange,goLeft)


array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
print(searchForRange(array, target))

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(searchForRange([5, 7, 7, 8, 8, 10], 5), [0, 0])

    def test_case_2(self):
        self.assertEqual(searchForRange([5, 7, 7, 8, 8, 10], 7), [1, 2])

    def test_case_3(self):
        self.assertEqual(searchForRange([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_case_4(self):
        self.assertEqual(searchForRange([5, 7, 7, 8, 8, 10], 10), [5, 5])

    def test_case_5(self):
        self.assertEqual(searchForRange([5, 7, 7, 8, 8, 10], 9), [-1, -1])

    def test_case_6(self):
        self.assertEqual(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 47), [-1, -1])

    def test_case_7(self):
        self.assertEqual(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], -1), [-1, -1])

    def test_case_8(self):
        self.assertEqual(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45), [4, 9])

    def test_case_9(self):
        self.assertEqual(searchForRange([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 45, 45, 45], 45), [4, 12])
