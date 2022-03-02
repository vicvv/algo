
class BST:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    if tree is None:
        return k
    array = helper([], tree)
    return array[-k]

def helper(array, tree):
    if tree is not None:		
        helper(array, tree.left)
        array.append(tree.value)
        helper(array, tree.right)
    return array

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(15)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.left.right = BST(3)
        root.left.right = BST(5)
        root.right = BST(20)
        root.right.left = BST(17)
        root.right.right = BST(22)
        k = 3
        expected = 17
        actual = findKthLargestValueInBst(root, k)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
