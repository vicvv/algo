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

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value>self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value,self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # single node tree
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right ==self:
                parent.right = self.left if self.left is not None else self.right
        
        return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()

import unittest
test1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
test2 = BST(10).insert(15).insert(11).insert(22).remove(10)
test3 = BST(10).insert(5).insert(7).insert(2).remove(10)
test4 = (
    BST(10)
    .insert(5)
    .insert(15)
    .insert(22)
    .insert(17)
    .insert(34)
    .insert(7)
    .insert(2)
    .insert(5)
    .insert(1)
    .insert(35)
    .insert(27)
    .insert(16)
    .insert(30)
    .remove(22)
    .remove(17)
)

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    
    return array


print(inOrderTraverse(test2,[]))

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(test1.left.value, 5)

    def test_case_2(self):
        self.assertEqual(test1.right.right.value, 22)

    def test_case_3(self):
        self.assertEqual(test1.right.left.value, 14)

    def test_case_4(self):
        self.assertEqual(test1.left.right.value, 5)

    def test_case_5(self):
        self.assertEqual(test1.left.left.value, 2)

    def test_case_6(self):
        self.assertEqual(test1.left.left.left, None)

    def test_case_7(self):
        self.assertEqual(test1.right.left.right, None)

    def test_case_8(self):
        self.assertEqual(test1.contains(15), True)

    def test_case_9(self):
        self.assertEqual(test1.contains(2), True)

    def test_case_10(self):
        self.assertEqual(test1.contains(5), True)

    def test_case_11(self):
        self.assertEqual(test1.contains(10), True)

    def test_case_12(self):
        self.assertEqual(test1.contains(22), True)

    def test_case_13(self):
        self.assertEqual(test1.contains(23), False)

    def test_case_14(self):
        self.assertEqual(inOrderTraverse(test2, []), [11, 15, 22])

    def test_case_15(self):
        self.assertEqual(inOrderTraverse(test3, []), [2, 5, 7])

    def test_case_16(self):
        self.assertEqual(inOrderTraverse(test4, []), [1, 2, 5, 5, 7, 10, 15, 16, 27, 30, 34, 35])

    def test_case_17(self):
        self.assertEqual(test4.right.right.value, 27)

    def test_case_18(self):
        self.assertEqual(test4.right.right.left.value, 16)

if __name__ == "__main__":
    unittest.main()