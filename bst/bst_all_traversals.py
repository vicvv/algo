#O(n) time | O(n) space

# in order I first expore all the nodes in the left tree,pritn the top node 
# and then I explore all nodes on the right
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right,array)
    print(array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


# Add, edit, or remove tests in this file.
# Treat it as your playground!


import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


test1 = BST(10).insert(5).insert(15)

test2 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22)

test3 = (
    BST(100)
    .insert(5)
    .insert(15)
    .insert(5)
    .insert(2)
    .insert(1)
    .insert(22)
    .insert(1)
    .insert(1)
    .insert(3)
    .insert(1)
    .insert(1)
    .insert(502)
    .insert(55000)
    .insert(204)
    .insert(205)
    .insert(207)
    .insert(206)
    .insert(208)
    .insert(203)
)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(inOrderTraverse(test1, []), [5, 10, 15])

    def test_case_2(self):
        self.assertEqual(inOrderTraverse(test2, []), [1, 2, 5, 5, 10, 15, 22])

    def test_case_3(self):
        self.assertEqual(
            inOrderTraverse(test3, []),
            [1, 1, 1, 1, 1, 2, 3, 5, 5, 15, 22, 100, 203, 204, 205, 206, 207, 208, 502, 55000],
        )

    def test_case_4(self):
        self.assertEqual(preOrderTraverse(test1, []), [10, 5, 15])

    def test_case_5(self):
        self.assertEqual(preOrderTraverse(test2, []), [10, 5, 2, 1, 5, 15, 22])

    def test_case_6(self):
        self.assertEqual(
            preOrderTraverse(test3, []),
            [100, 5, 2, 1, 1, 1, 1, 1, 3, 15, 5, 22, 502, 204, 203, 205, 207, 206, 208, 55000],
        )

    def test_case_7(self):
        self.assertEqual(postOrderTraverse(test1, []), [5, 15, 10])

    def test_case_8(self):
        self.assertEqual(postOrderTraverse(test2, []), [1, 2, 5, 5, 22, 15, 10])

    def test_case_9(self):
        self.assertEqual(
            postOrderTraverse(test3, []),
            [1, 1, 1, 1, 1, 3, 2, 5, 22, 15, 5, 203, 206, 208, 207, 205, 204, 55000, 502, 100],
        )
if __name__ =="__main__":
    unittest.main()