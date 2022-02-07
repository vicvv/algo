class BST:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self,value):
        currentNode = self
        while True:
            if currentNode.value < value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left

        return self
    
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if currentNode.value < value:
                currentNode = currentNode.right
            elif currentNode.value > value:
                currentNode = currentNode.left
            else:
                return True
        return False  


    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if currentNode.value < value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif currentNode.value > value:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                #case where we have 2 children at the node that we want to delete
                if currentNode.right is not None and currentNode.left is not None:
                    currentNode.value = currentNode.right.getMinVal()
                    currentNode.right.remove(currentNode.value, currentNode)
                # HERE WE ARE DEALING WITH THE ROOT NODE
                elif parentNode is not None:
                    # if root node has only left child. order of execution is important
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    # if root has only left child
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        pass
                # case where we have only left child at the node that we want to remove
                elif parentNode.left == currentNode:
                    #   5
					#  / 
					# 3   <- IF WE REMOVING 3
					#  \
					#   4 <- WE REASIGHN 4 TO 5 IF 3 HAS NO LEFT CHILD
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                # case whre we have only the right child at the node that we want to remove
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right


    def getMinVal(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    def getMaxVal(self):
        currentNode = self
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode.value

def inOrderTraverse(tree):
    if tree is not None:       
        inOrderTraverse(tree.left)
        print(tree.value)
        inOrderTraverse(tree.right)

mytree = BST(10)
mytree.insert(5)
mytree.insert(15)
mytree.insert(2)
mytree.insert(4)
mytree.insert(14)
mytree.insert(12)


print(mytree.contains(25))
print(mytree.getMinVal())
print(mytree.getMaxVal())

print('before remove 15')
inOrderTraverse(mytree)
mytree.remove(15)
print('after remove 15')
inOrderTraverse(mytree)



            