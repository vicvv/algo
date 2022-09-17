'''Write a function that takes in two non-empty arrays of integers, finds the pair of 
numbers (one from each array) whose absolute difference is
closest to zero, and returns an array containing these two numbers, with the number 
from the first array in the first position.
Note that the absolute difference of two integers is the distance between them on 
the real number line. For example, the absolute difference of
-5 and 5 is 10, and the absolute difference of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with the smallest difference.
Sample Input
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
Sample Output
[28, 26]'''

arrayOne = [-1,5,10,20,28,3]
arrayTwo = [26,134,135,15,17]
# result = [28,26]


'''
# O(N2)
def smallestDifference(arrayOne, arrayTwo):
    min = float("inf")
    minarr =[]
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            res = abs(arrayOne[i]- arrayTwo[j])
            if res < min:
                min = res
                minarr = [arrayOne[i],arrayTwo[j]]
    return minarr
    '''

#print(ssmallestDifference(arrayOne,arrayTwo))

# # O(nlog(n) + mlog(m)) time| O(1) space
# def smallestDifference(arrayOne, arrayTwo):
#     arrayOne.sort()
#     arrayTwo.sort()   
#     smalest = float("inf")
#     current = float("inf")
    
#     idx1 = 0
#     idx2 = 0
    
#     pair = []
    
#     while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
#         firstnum = arrayOne[idx1]
#         secondnum = arrayTwo[idx2]
#         #current = abs(firstnum - secondnum )
#         if firstnum > secondnum:
#             current = firstnum - secondnum
#             idx2 += 1
#         elif secondnum > firstnum:
#             current = secondnum - firstnum
#             idx1 += 1
#         else:
#             # they both are equal and diff is 0
#             return[firstnum, secondnum]
#         if smalest > current:
#             smalest = current
#             pair =  [firstnum, secondnum]
#     return pair


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    indexOne, indexTwo = 0,0
    smallest, smallestPair = float('inf'), []

    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
        firstNum = arrayOne[indexOne]
        secondNum = arrayTwo[indexTwo]
        current = abs(firstNum - secondNum)
        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]
        elif firstNum > secondNum:
            indexTwo +=1
        else:
            indexOne +=1
    return smallestPair


print(smallestDifference(arrayOne,arrayTwo))

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]), [20, 17])

    def test_case_2(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])

    def test_case_3(self):
        self.assertEqual(smallestDifference([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031]), [25, 1005])

    def test_case_4(self):
        self.assertEqual(smallestDifference([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031]), [25, 1005])

    def test_case_5(self):
        self.assertEqual(
            smallestDifference([10, 0, 20, 25, 2000], [1005, 1006, 1014, 1032, 1031]), [2000, 1032]
        )

    def test_case_6(self):
        self.assertEqual(
            smallestDifference([240, 124, 86, 111, 2, 84, 954, 27, 89], [1, 3, 954, 19, 8]), [954, 954]
        )

    def test_case_7(self):
        self.assertEqual(smallestDifference([0, 20], [21, -2]), [20, 21])

    def test_case_8(self):
        self.assertEqual(
            smallestDifference([10, 1000], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]), [1000, 1014]
        )

    def test_case_9(self):
        self.assertEqual(
            smallestDifference(
                [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
            ),
            [-123, -124],
        )

    def test_case_10(self):
        self.assertEqual(
            smallestDifference(
                [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530],
                [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530],
            ),
            [530, 530],
        )

if __name__ == "__main__":
    unittest.main()