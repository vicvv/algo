# create as balanced tree if possible

arr = [1, 2, 5, 7, 10, 13, 14, 15, 22]

# # Time O(nlogn) | space O(n)  using provided insert which adds log(N) to time
# def minHeightBst(array):
#     return minHelper(array, None, 0, len(array) -1)

# def minHelper(array, bst, start, end):
# 	if end < start:
# 		return
# 	mid = (start + end)//2
# 	valToAdd = array[mid]
# 	if bst is None:
# 		bst = BST(valToAdd)
# 	else:
# 		bst.insert(valToAdd)
# 	minHelper(array, bst, start, mid-1)
# 	minHelper(array, bst, mid+1, end)
# 	return bst

# O(n) | O(n) # using manual insert
def minHeightBst(array):
    return minHelper(array, None, 0, len(array) -1)

def minHelper(array, bst, start, end):
    if end < start:
        return
    mid = (start + end) >> 1
    newNode = BST(array[mid])

    if bst is None: 
        bst = newNode
    else:
        if array[mid] < bst.value:
            bst.left = newNode
            bst = bst.left
        else:
            bst.right = newNode
            bst = bst.right


    minHelper(array, bst, start, mid-1)
    minHelper(array, bst, mid+1, end)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def insert(self, value):
    #     if value < self.value:
    #         if self.left is None:
    #             self.left = BST(value)
    #         else:
    #             self.left.insert(value)
    #     else:
    #         if self.right is None:
    #             self.right = BST(value)
    #         else:
    #             self.right.insert(value)





import unittest


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = minHeightBst(array)

        self.assertTrue(validateBst(tree))
        self.assertEqual(getTreeHeight(tree), 4)

        inOrder = inOrderTraverse(tree, [])

        self.assertEqual(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])

# if __name__ == "__main__":
#     unittest.main()


bstree = minHeightBst(arr)
arr = inOrderTraverse(bstree, [])
print(arr)