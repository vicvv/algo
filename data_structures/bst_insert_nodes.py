class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
        
class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def add(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val <= currentNode.value:
            if currentNode.left:
                self.insertNode(currentNode.left, val)
            else:
                currentNode.left = Node(val)
        else:
            if currentNode.right:
                self.insertNode(currentNode.right, val)
            else:
                currentNode.right = Node(val)
        
    def traverse(self):
        self._traverse(self.root)
        
    def _traverse(self, node):
        if node != None:
            self._traverse(node.left)
            print(node.value)
            self._traverse(node.right)
                



bst = BST()
bst.add(5)


bst.add(3)
bst.add(7)
bst.add(1)
bst.add(4)
bst.add(10)
bst.traverse()

#		  5
#   	/   \
#     3     7
#    / \      \
#   1   4     10

