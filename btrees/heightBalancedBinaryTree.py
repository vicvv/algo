
#(O)n time and (O)h space.

# find if btree is height balanced. Meaning for each node in the tree the diff between
# the height of its left subtree and the height of its right subtree is at most 1.


class BinaryTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)
    leftSubtreeInfo = getTreeInfo(node.left)
    rightSubtreeInfo = getTreeInfo(node.right)

    isBalanced = (
        leftSubtreeInfo.isBalanced
        and rightSubtreeInfo.isBalanced
        and abs(leftSubtreeInfo.height - rightSubtreeInfo.height )<=1
    )

    height = max(leftSubtreeInfo.height, rightSubtreeInfo.height) +1
    return TreeInfo(isBalanced, height)


import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        root.left.right.left = BinaryTree(7)
        root.left.right.right = BinaryTree(8)
        expected = True
        actual = heightBalancedBinaryTree(root)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()