# write the function that takes binary tree that has pointer to parent node in adition to left and
# right child and return the closes successor.
# A node successor is the next node to be visited
# O(N) time | O(N) space
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    inOrderTraversal = getInOrderTraversal(tree)
    print(inOrderTraversal)
    for idx, curNode in enumerate(inOrderTraversal):
        if curNode != node:
            continue
        if idx == len(inOrderTraversal)-1:
            return None
        print(idx)
        return inOrderTraversal[idx+1]

def getInOrderTraversal(node, order=[]):
	if node is None:
		return order
	getInOrderTraversal(node.left, order)
	order.append(node)
	getInOrderTraversal(node.right, order)
	
	return order
	

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