class BinaryTree:
    def __init__(self, value, right=None, left=None, parent=None):
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent

def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftmostChild(node.right)
    return getRightMostParent(node)

def getLeftmostChild(node):
	currentNode = node
	while currentNode.left is not None:
		currentNode = currentNode.left
	return currentNode


def getRightMostParent(node):
	currentNode = node
	while currentNode.parent is not None and currentNode.parent.right == currentNode:
		currentNode = currentNode.parent
	return currentNode.parent

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.parent = root
        root.right = BinaryTree(3)
        root.right.parent = root
        root.left.left = BinaryTree(4)
        root.left.left.parent = root.left
        root.left.right = BinaryTree(5)
        root.left.right.parent = root.left
        root.left.left.left = BinaryTree(6)
        root.left.left.left.parent = root.left.left
        node = root.left.right
        expected = root
        actual = findSuccessor(root, node)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()