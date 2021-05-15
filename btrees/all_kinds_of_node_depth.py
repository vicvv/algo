
# given b tree find depth of all subtrees and sumthem up.

#Average case if the tree is balanced
#O(nlog(n)) time | O(h) space where n is 
# the nuber of node and h is the height of BT

def allKindsOfNodeDepths(root):
    if root is None:
        return 0
    return allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right) + nodeDepth(root)

def nodeDepth(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepth(root.left, depth+1) + nodeDepth(root.right, depth+1)



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
       

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