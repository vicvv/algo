# Average case if the tree is balanced
# O(nlog(n)) time | O(h) space where n is 
# the nuber of node and h is the height of BT


def allKindsOfNodeDepths(root):
    sumOfAllDepth = 0
    stack = [root]
    while len(stack):
        node = stack.pop()
        if node is None:
            continue
        sumOfAllDepth += nodeDepth(node)
        stack.append(node.left)
        stack.append(node.right)
    return sumOfAllDepth

def nodeDepth(node, depth= 0):
    if node is None:
        return 0
    return depth + nodeDepth(node.left, depth+1) + nodeDepth(node.right, depth+1)



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