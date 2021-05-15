#O(n) time | O(h) space

def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepth

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0,0,0)
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	sumOfLeftDepth = leftTreeInfo.sumOfDepth + leftTreeInfo.numNodesInTree
	sumOfRightDepth = rightTreeInfo.sumOfDepth + rightTreeInfo.numNodesInTree
	
	numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodesInTree
	sumOfDepth = sumOfLeftDepth + sumOfRightDepth
	sumOfAllDepth = sumOfDepth + leftTreeInfo.sumOfAllDepth + rightTreeInfo.sumOfAllDepth
	
	return TreeInfo(numNodesInTree, sumOfDepth, sumOfAllDepth)
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
class TreeInfo:
	def __init__(self, numNodesInTree, sumOfDepth, sumOfAllDepth):
		self.numNodesInTree = numNodesInTree
		self.sumOfDepth = sumOfDepth
		self.sumOfAllDepth = sumOfAllDepth


import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        actual = allKindsOfNodeDepths(root)
        self.assertEqual(actual, 26)
if __name__ =="__main__":
    unittest.main()