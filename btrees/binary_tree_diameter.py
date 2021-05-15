# find the longest path in the tree. It might or might not travel thrue root

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
  	return getTreeInfo(tree).diameter
    #return getTreeInfo(tree) if we want to see height and diamenter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0)

    leftTreeInfo = getTreeInfo(tree.left)
    righTreeInfo = getTreeInfo(tree.right)

    longestPathTrueRoot = leftTreeInfo.height +	righTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, righTreeInfo.diameter)
    currentDiameter =max(longestPathTrueRoot, maxDiameterSoFar)
    currentHeight = 1+ max(leftTreeInfo.height, righTreeInfo.height)
    
    print(currentDiameter, currentHeight)

    return TreeInfo(currentDiameter, currentHeight)

class TreeInfo:
	def __init__(self, diameter,height):
		self.diameter = diameter
		self.height = height

# uncoment main for test case below.
root = BinaryTree(1)
root.left = BinaryTree(3)
root.left.left = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)
root.left.right = BinaryTree(4)
root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)
root.right = BinaryTree(2)

print(binaryTreeDiameter(root))

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.right = BinaryTree(2)
        expected = 6
        actual = binaryTreeDiameter(root)
        self.assertEqual(actual, expected)

# if __name__ == "__main__":
#     unittest.main()