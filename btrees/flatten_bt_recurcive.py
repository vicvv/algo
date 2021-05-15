###############
# O(n) time | O(d) space where n in the number of nodes 
# d is the depth of the tree
def flattenBinaryTree(root):
	leftMost, _ = flattenTree(root)
	return leftMost
	
def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        connectNodes(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost
        
    if node.right is None:
        rightMost = node
    else:
        rightMostSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
        connectNodes(node,rightMostSubtreeLeftMost)
        rightMost = rightSubtreeRightMost
        
    return [leftMost, rightMost]
		
		
def connectNodes(left, right):
	left.right = right
	right.left = left



import unittest

# This is the class of the input root. 
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def leftToRightToLeft(self):
        nodes = []
        current = self
        while current.right is not None:
            nodes.append(current.value)
            current = current.right
        nodes.append(current.value)
        while current is not None:
            nodes.append(current.value)
            current = current.left
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1).insert([2, 3, 4, 5, 6])
        root.left.right.left = BinaryTree(7)
        root.left.right.right = BinaryTree(8)
        leftMostNode = flattenBinaryTree(root)
        leftToRightToLeft = leftMostNode.leftToRightToLeft()
        expected = [4, 2, 7, 5, 8, 1, 6, 3, 3, 6, 1, 8, 5, 7, 2, 4]
        self.assertEqual(leftToRightToLeft, expected)


if __name__ =="__main__":
    unittest.main()



