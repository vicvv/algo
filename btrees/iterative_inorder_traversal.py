
# O(n) time| O(1) space
# to decide where or not to call the callback on the given node
# we have to know what the previous node I just traverced was

def iterativeInOrderTraversal(tree, callback):
	previousNode = None
	currentNode = tree
	
	while currentNode is not None:
		if previousNode is None or previousNode == currentNode.parent:
			if currentNode.left is not None:
				nextNode = currentNode.left
			else:
				callback(currentNode)
				nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
				
		elif previousNode == currentNode.left:
			callback(currentNode)
			nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
		
		else:
			nextNode = currentNode.parent
		previousNode = currentNode
		currentNode = nextNode

  

import unittest


class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


def testCallback(testArray, tree):
    if tree is None:
        return
    testArray.append(tree.value)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2, parent=root)
        root.left.left = BinaryTree(4, parent=root.left)
        root.left.left.right = BinaryTree(9, parent=root.left.left)
        root.right = BinaryTree(3, parent=root)
        root.right.left = BinaryTree(6, parent=root.right)
        root.right.right = BinaryTree(7, parent=root.right)

        testArray = []
        actualTestCallback = lambda x: testCallback(testArray, x)
        iterativeInOrderTraversal(root, actualTestCallback)
        self.assertEqual(testArray, [4, 9, 2, 1, 6, 3, 7])

if __name__ =="__main__":
    unittest.main()