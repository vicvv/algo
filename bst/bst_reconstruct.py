
# preorder traversed array is given as an input. reconstruct BST.
import unittest


class BST:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues)==0:
        return None
    currentValue = preOrderTraversalValues[0]
    right_most_index = len(preOrderTraversalValues)

    for idx in range(1, len(preOrderTraversalValues)):
        if currentValue >= preOrderTraversalValues[idx]:
            right_most_index = idx
        break
    left_side_val = reconstructBst(preOrderTraversalValues[1:right_most_index])
    right_side_val= reconstructBst(preOrderTraversalValues[right_most_index:])

    return BST(currentValue, left_side_val, right_side_val)


def getDfsOrder(node, values):
    if node is None:
        return
    values.append(node.value)
    getDfsOrder(node.left, values)
    getDfsOrder(node.right, values)
    return values


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        preOrderTraversalValues = [10, 4, 2, 1, 3, 17, 19, 18]
        tree = BST(10)
        tree.left = BST(4)
        tree.left.left = BST(2)
        tree.left.left.left = BST(1)
        tree.left.right = BST(3)
        tree.right = BST(17)
        tree.right.right = BST(19)
        tree.right.right.left = BST(18)
        expected = getDfsOrder(tree, [])
        actual = reconstructBst(preOrderTraversalValues)
        actualDfsOrder = getDfsOrder(actual, [])
        self.assertEqual(actualDfsOrder, expected)

if __name__=="__main__":
    unittest.main()
