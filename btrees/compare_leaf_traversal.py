'''Compare Leaf Traversal
Write a function that takes in the root nodes of two Binary Trees
and returns a boolean representing whether their leaf traversals
are the same.
The leaf traversal of a Binary Tree traverses only its leaf nodes
from left to right. A leaf node is any node that has no left or
right children.'''



import unittest

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# O(n + m) time | O(h1 + h2) space - where n is the number of nodes in the first
# Binary Tree, m is the number in the second, h1 is the height of the first Binary
# Tree, and h2 is the height of the second
def compareLeafTraversal(tree1, tree2):
    tree1TraversalStack = [tree1]
    tree2TraversalStack = [tree2]
    while len(tree1TraversalStack) > 0 and len(tree2TraversalStack) > 0:
        tree1Leaf = getNextLeafNode(tree1TraversalStack)
        tree2Leaf = getNextLeafNode(tree2TraversalStack)
        if tree1Leaf.value != tree2Leaf.value:
            return False
    return len(tree1TraversalStack) == 0 and len(tree2TraversalStack) == 0
def getNextLeafNode(traversalStack):
    currentNode = traversalStack.pop()
    while not isLeafNode(currentNode):
        if currentNode.right is not None:
            traversalStack.append(currentNode.right)
            # We purposely add the left node to the stack after the
            # right node so that it gets popped off the stack first.
        if currentNode.left is not None:
            traversalStack.append(currentNode.left)
        currentNode = traversalStack.pop()
    return currentNode
def isLeafNode(node):
    return node.left is None and node.right is None






class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree1 = BinaryTree(1)
        tree1.left = BinaryTree(2)
        tree1.right = BinaryTree(3)
        tree1.left.left = BinaryTree(4)
        tree1.left.right = BinaryTree(5)
        tree1.right.right = BinaryTree(6)
        tree1.left.right.left = BinaryTree(7)
        tree1.left.right.right = BinaryTree(8)

        tree2 = BinaryTree(1)
        tree2.left = BinaryTree(2)
        tree2.right = BinaryTree(3)
        tree2.left.left = BinaryTree(4)
        tree2.left.right = BinaryTree(7)
        tree2.right.right = BinaryTree(5)
        tree2.right.right.left = BinaryTree(8)
        tree2.right.right.right = BinaryTree(6)

        expected = True
        actual = compareLeafTraversal(tree1, tree2)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()