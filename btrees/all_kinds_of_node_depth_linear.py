
#O(n) time | O(n) space

# the idea here is to calculate the depth of the root node and and add the total node count to it
# so this will compute the sum of all depth of all subtrees. 

def allKindsOfNodeDepths(root):
    nodeCounts = {}
    addNodeCounts(root, nodeCounts)
    nodeDepth = {}
    addNodeDepth(root, nodeDepth, nodeCounts)
    return sumAllNodeDepth(root, nodeDepth)

def sumAllNodeDepth(root, nodeDepths):
	if root is None:
		return 0
	return sumAllNodeDepth(root.right, nodeDepths) + sumAllNodeDepth(root.left, nodeDepths) + nodeDepths[root] 

def addNodeDepth(root, nodeDepth, nodeCounts):
	nodeDepth[root] = 0
	if root.left is not None:
		addNodeDepth(root.left, nodeDepth, nodeCounts)
		nodeDepth[root] += nodeDepth[root.left] + nodeCounts[root.left]
	if root.right is not None:
		addNodeDepth(root.right, nodeDepth, nodeCounts)
		nodeDepth[root] += nodeDepth[root.right] + nodeCounts[root.right]
	
		
def addNodeCounts(root, nodeCounts):
	nodeCounts[root] = 1
	if root.left is not None:
		addNodeCounts(root.left, nodeCounts)
		nodeCounts[root] += nodeCounts[root.left]
	if root.right is not None:
		addNodeCounts(root.right, nodeCounts)
		nodeCounts[root] += nodeCounts[root.right]



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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