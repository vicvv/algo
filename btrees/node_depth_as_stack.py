def nodeDepths(root):
    sumOfDepth = 0
    stack = [{"node": root, "depth":0}]
    while len(stack):
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepth +=depth
        stack.append({"node": node.left, "depth":depth+1})
        stack.append({"node": node.right, "depth":depth+1})
        
    return sumOfDepth


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
        actual = nodeDepths(root)
        self.assertEqual(actual, 16)

if __name__ == "__main__":
    unittest.main()