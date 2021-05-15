# write a function that takes a not negative number n and returns a number of
# posible binary tree topoloties that can be created with exactly n nodes

# kathelane formula (2n)!/n!(n+1)! |time complexity   <-- all the worse
def numberOfBinaryTreeTopologies(n):
    if n == 0:
        return 1
    numofTT = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numofRight = numberOfBinaryTreeTopologies(rightTreeSize)
        numofLeft =  numberOfBinaryTreeTopologies(leftTreeSize)

        numofTT += numofRight * numofLeft

    return numofTT

# with memoization

# O(n^2) time | O(n) space

# def numberOfBinaryTreeTopologies(n, cache={0:1}):
# 	if n in cache:
# 		return cache[n]
	
# 	numberOfTrees = 0
# 	for leftTreeSize in range(n):
# 		rightTreeSize = n - 1 - leftTreeSize
# 		numberofLTrees = numberOfBinaryTreeTopologies(leftTreeSize,cache)
# 		numberofRTrees = numberOfBinaryTreeTopologies(rightTreeSize,cache)
# 		numberOfTrees += numberofLTrees * numberofRTrees
# 	cache[n] = numberOfTrees
# 	return numberOfTrees

# iterative solution with memoization
# O(n^2) time | O(n) space

# def numberOfBinaryTreeTopologies(n):
# 	cache = [1]
# 	for m in range(1, n + 1):
# 		numberOfTrees = 0
# 		for leftTreeSize in range(m):
# 			rightTreeSize = m - 1 - leftTreeSize
# 			numberofLTrees = cache[leftTreeSize]
# 			numberofRTrees = cache[rightTreeSize]
# 			numberOfTrees += numberofLTrees * numberofRTrees
# 		cache.append(numberOfTrees)
# 	return cache[n]


import unittest

class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(numberOfBinaryTreeTopologies(3), 5)

if __name__ == "__main__":
    unittest.main()
