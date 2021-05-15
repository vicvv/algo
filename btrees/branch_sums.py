# function takes in binary tree and returns list of branch sums ordered
# from left most to right most

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self,value):
        print(value)
        currentNode = self
        while True:
            if value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BinaryTree(value)
                    break
                else:
                    currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = BinaryTree(value)
                    break
                else:
                    currentNode = currentNode.left
        return self
# O(n) time | O(n) space
def branchSums(root):
    sums = []
    calculateSums(root, 0, sums)    
    return sums

def calculateSums(node, curSum, sums):
    if node is None:
        return

    newSum = curSum + node.value
    if node.left is None and node.right is None:
        sums.append(newSum)
        return

    calculateSums(node.left, newSum, sums)
    calculateSums(node.right, newSum, sums)


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left,array)
        array.append(tree.value)
        inOrderTraverse(tree.right,array)
    return array
    
import unittest
#test1 = BinaryTree(10)
test1 = BinaryTree(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)

#print(inOrderTraverse(test1,[]))
print(branchSums(test1))

class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(inOrderTraverse(test1, []), [2, 5, 5, 10, 14, 15, 22])

    def test2(self):
        self.assertEqual(branchSums(test1),[22,39,47])
if __name__ == "__main__":
    unittest.main()



