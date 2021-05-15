
# mirror binary tree. Non recursive method
def invertBinaryTree(tree):
    quie = [tree]
    while len(quie):
        current = quie.pop(0)
        if current is None:
            continue
        swapLeftAndRight(tree)
        quie.append(current.left)
        quie.append(current.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

        
# invert Recurcive
def invertBinaryTreeRecursive(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTreeRecursive(tree.left)
    invertBinaryTreeRecursive(tree.right)



# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

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

    def invertedInsert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
        self.invertedInsert(values, i + 1)
        return self


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])
        invertedTree = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7, 8, 9])
        invertBinaryTree(tree)
        self.assertTrue(tree.__eq__(invertedTree))


if __name__ == "__main__":
    unittest.main()