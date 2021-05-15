# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)
                    
        return self


def flattenBinaryTree(root):
    inOrderNodes = getNodesInOrder(root,[])
    for i in range(0,len(inOrderNodes) - 1):
        leftNode = inOrderNodes[i]
        rightNode = inOrderNodes[i + 1]
        leftNode.right = rightNode
        leftNode.left = leftNode
    return inOrderNodes[0]

def getNodesInOrder(node,array):
    if node is not None:
        getNodesInOrder(node.left, array)
        array.append(node)
        getNodesInOrder(node.right,array)
    print(array)
    return array

test1 = BinaryTree(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)

print(flattenBinaryTree(test1))
