
'''return 3 largest number from sorted array'''
# time O(n) | space O(1)
import unittest

# def findThreeLargestNumbers(array):
#     array.sort()
#     return array[-3:None]

#array = [141,1,17,-7, -17,-27 ,18,541,8,7,7]
# res [14,141,547]
#print(findThreeLargestNumbers(array))

def findThreeLargestNumbers(array):   
   targetArray = [None, None, None]   
   for num in array:
       updateArray(targetArray, num)
   return targetArray

def updateArray(targetArray, num):
    if targetArray[2] is None or num > targetArray[2]  :
        shiftAndUpdate(targetArray, 2, num)
    elif targetArray[1] is None or num > targetArray[1]:
        shiftAndUpdate(targetArray, 1, num)
    elif targetArray[0] is None or num > targetArray[0] :
        shiftAndUpdate(targetArray, 0, num)

def shiftAndUpdate(targetArray, idx, num):
    for i in range(idx + 1):
        if i == idx:
            targetArray[i] = num
        else:
            targetArray[i] = targetArray[i + 1]


class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findThreeLargestNumbers([55, 7, 8]), [7, 8, 55])

    def test_case_2(self):
        self.assertEqual(findThreeLargestNumbers([55, 43, 11, 3, -3, 10]), [11, 43, 55])

    def test_case_3(self):
        self.assertEqual(findThreeLargestNumbers([7, 8, 3, 11, 43, 55]), [11, 43, 55])

    def test_case_4(self):
        self.assertEqual(findThreeLargestNumbers([55, 7, 8, 3, 43, 11]), [11, 43, 55])

    def test_case_5(self):
        self.assertEqual(findThreeLargestNumbers([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]), [7, 7, 7])

    def test_case_6(self):
        self.assertEqual(findThreeLargestNumbers([7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7]), [7, 7, 8])

    def test_case_7(self):
        self.assertEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])

    def test_case_8(self):
        self.assertEqual(findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]), [-2, -1, 7])



if __name__ == "__main__":
    unittest.main()