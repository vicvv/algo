'''
You're given three nodes that are contained in the same Binary Search Tree: nodeOne , nodeTwo , and nodeThree . 
Write a function that returns a boolean representing whether one of nodeOne or nodeThree is an ancestor of nodeTwo 
and the other node is a descendant of nodeTwo . For example, if your function determines that nodeOne is an ancestor 
of nodeTwo , then it needs to see if nodeThree is a descendant of
nodeTwo . If your function determines that nodeThree is an ancestor, then it needs to see if nodeOne is a descendant.
A descendant of a node N is defined as a node contained in the
tree rooted at N . A node N is an ancestor of another node M
if M is a descendant of N . It isn't guaranteed that nodeOne or nodeThree will be
ancestors or descendants of nodeTwo , but it is guaranteed that
all three nodes will be unique and will never be None / null .
In other words, you'll be given valid input nodes.
Each BST node has an integer value , a left child node,and a right child node. A node is said to be a valid BST node
if and only if it satisfies the BST property: its value is strictly
greater than the values of every node to its left; its value is less
than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves 
or None/ null .

'''

import unittest
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if is_desendant(nodeTwo, nodeOne):
        return is_desendant(nodeThree,nodeTwo)

    if is_desendant(nodeTwo, nodeThree):
        return is_desendant(nodeOne, nodeTwo)

    return False

def is_desendant(node, target):
    if node is None: return False
    if node == target:
        return True
    return is_desendant(node.left, target) if node.value > target.value else is_desendant(node.right, target)
    
    

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(5)
        root.left = BST(2)
        root.right = BST(7)
        root.left.left = BST(1)
        root.left.right = BST(4)
        root.right.left = BST(6)
        root.right.right = BST(8)
        root.left.left.left = BST(0)
        root.left.right.left = BST(3)

        nodeOne = root
        nodeTwo = root.left
        nodeThree = root.left.right.left
        expected = True
        actual = validateThreeNodes(nodeOne, nodeTwo, nodeThree)
        self.assertEqual(actual, expected)


if __name__=="__main__":
    unittest.main()