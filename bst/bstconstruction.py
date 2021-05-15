class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif currentNode.value < value:
                currentNode = currentNode.right
            else:
                return True

        return False

    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                # if we removing the current node we need to reasigh its children so we need to keep a parent(previous node)
                parentNode = currentNode 
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # case when we have 2 child nodes present
                if currentNode.left is not None and currentNode.right is not None:
                     currentNode.value = currentNode.right.getMinvalue()
                     # currentNode.value = to the smallest value in the right subtress
                     currentNode.right.remove  (currentNode.value,currentNode)
                # case when we have one child ither on left or right side
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        #this is a single node tree
                        pass
                elif parentNode.left == currentNode:
                     parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right == currentNode.right if currentNode.left is not None else currentNode.right
                break
        return self



    def getMinvalue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value


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
