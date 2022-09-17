

'''
Min Number Of Jumps
You're given a non-empty array of positive integers where each integer represents 
the maximum number of steps you can take forward in the
array. For example, if the element at index 1 is 3 , you can go from index 1 to index 2 , 3 , or 4 .
Write a function that returns the minimum number of jumps needed to reach the final index.
Note that jumping from index i to index i + x always constitutes one jump, no matter how large x is.
Sample Input
array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
Sample Output
4 // 3 --> (4 or 2) --> (2 or 3) --> 7 --> 3
'''


# def minNumberOfJumps(array):
# 	if len(array) == 1:
# 		return 0
# 	jumps = [float('inf') for x in array]
# 	jumps[0] = 0
# 	for i in range(1, len(array)):
# 		for j in range(0,i):
# 			if array[j] >= i - j:
# 				jumps[i] = min(jumps[j] +1, jumps[i])
# 	return jumps[-1]


# time  O(n)| space O(1) --> storing just max val and not building the array
def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    maxReach = array[0]
    steps = array[0]
    jumps = 0
    for i in range(1, len(array)-1):
        maxReach = max(maxReach, i+array[i])
        steps -=1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
            
    return jumps +1


import unittest

class TestProgram(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)
        #self.assertEqual(minNumberOfJumps([1]), [0])
    
    def test_case2(self):
        self.assertEqual(minNumberOfJumps([1]), 0)

    def test_case3(self):
        self.assertEqual(minNumberOfJumps([1,1]), 1)
    
    def test_case4(self):
        self.assertEqual(minNumberOfJumps([3,1]), 1)

    def test_case5(self):
        self.assertEqual(minNumberOfJumps([1,1,1]), 2)

    def test_case6(self):
        self.assertEqual(minNumberOfJumps([2,1,1]), 1)

    def test_case7(self):
        self.assertEqual(minNumberOfJumps([2, 1, 2, 3, 1]), 2)

    def test_case8(self):
        self.assertEqual(minNumberOfJumps([2, 1, 2, 3, 1, 1, 1]), 3)

    def test_case9(self):
        self.assertEqual(minNumberOfJumps([2, 1, 2, 2, 1, 1, 1]), 4)

    def test_case10(self):
        self.assertEqual(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 6, 2, 1, 1, 1, 1]), 5)

    def test_case11(self):
        self.assertEqual(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]), 7)

    def test_case12(self):
        self.assertEqual(minNumberOfJumps([3, 12, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]), 5)

    def test_case13(self):
        self.assertEqual(minNumberOfJumps([3, 10, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]), 6)

    def test_case14(self):
        self.assertEqual(minNumberOfJumps([3, 12, 2, 1, 2, 3, 15, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]), 3)
    
    # def test_case15(self):
    #     self.assertEqual(minNumberOfJumps([3,2,1,0,4]),-1)

    
if __name__ == "__main__":
    unittest.main()