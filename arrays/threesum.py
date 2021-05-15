'''given the array of distinct integer and a target sum return the triplets
which sum is equal to the given sum in sorted order. The resulting array also should be sorted
If no triplets exists return empty array'''

'''
in this solution we have 3 pointers: current, left and right. Note how we set the range
len(arr) - 2? It is due to us moving 2 pointers intead of one all the time.
So we have 2 loops: external for and internal while loop and we checking the sum. 


'''

#O(n2) time | O(n) space

import unittest

array = [12,3,1,2,-6,5,-8,6]
#[-8, -6, 1, 2, 3, 5, 6, 12]
targetSum = 0
# sample output [[-8,2,6],[-8,3,5],[-6,1,5]]

def threeNumberSum(array, targetSum):
   
    narr = []
    array.sort()

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        
        while left < right:
            
            curSum = array[i] + array[left] + array[right]
            #print(curSum)
            if curSum == targetSum:
                narr.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif curSum < targetSum:
                left += 1
            elif curSum > targetSum:
                right -=1

    
    return narr

#print(threeNumberSum(array, targetSum))

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(threeNumberSum([1, 2, 3], 6), [[1, 2, 3]])

    def test_case_2(self):
        self.assertEqual(threeNumberSum([1, 2, 3], 7), [])

    def test_case_3(self):
        self.assertEqual(threeNumberSum([8, 10, -2, 49, 14], 57), [[-2, 10, 49]])

    def test_case_4(self):
        self.assertEqual(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])

    def test_case_5(self):
        self.assertEqual(
            threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1], 0), [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]]
        )

    def test_case_6(self):
        self.assertEqual(
            threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0),
            [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-1, 0, 1]],
        )

    def test_case_7(self):
        self.assertEqual(
            threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0),
            [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-5, -1, 6], [-5, 0, 5], [-5, 2, 3], [-1, 0, 1]],
        )

    def test_case_8(self):
        self.assertEqual(
            threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18),
            [[1, 2, 15], [1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]],
        )

    def test_case_9(self):
        self.assertEqual(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32), [[8, 9, 15]])

    def test_case_10(self):
        self.assertEqual(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33), [])

    def test_case_11(self):
        self.assertEqual(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 5), [])

    def test_case_12(self):
        self.assertEqual(threeNumberSum([-1, 0, 1, 2, -1, -4],0), [[-1, 0, 1],[-1, -1, 2]])

if __name__ == "__main__":
    unittest.main()

