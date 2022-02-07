class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
        
class BST:
    def __init__(self):
        self.root = None
        
    def add(self, value):
        newNode = Node(value)
        #if there is no node in BST
        if self.root == None:
            self.root = newNode
        else:
            self._add(self.root, newNode)
            return
    # recursive function to add a newNode below node 
    def _add(self, node, newNode):
        # if the value in newNode is less than the current node's value
        if newNode.value < node.value:
            # see if left is null
            if node.left == None:
                node.left = newNode
            else:
                self._add(node.left, newNode)
        # if the value in newNode is more than the current node's value
        else:
            # see if right is null
            if node.right == None:
                node.right = newNode
            else:
                self._add(node.right, newNode)

    def in_order(self):
        self._in_order(self.root)
        
    def _in_order(self, node):
        if node != None:
            self._in_order(node.left)
            print(node.value)
            self._in_order(node.right)
        
    def pre_order(self):
        self._pre_order (self.root)
    
    def _pre_order(self, node): 
        if node != None:       
            print(node.value)
            self._pre_order(node.left)
            self._pre_order(node.right)


    def post_order(self):
        self._post_order(self.root)

    def _post_order(self, node):
        if node != None:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.value)

bst = BST()
bst.add(5)
bst.add(3)
bst.add(7)
bst.add(1)
bst.add(4)
bst.add(10)

#		  5
#   	/   \
#     3     7
#    / \      \
#   1   4     10

print("Pre Order: #to log 5 3 1 4 7 10")
bst.pre_order() 
print("In order: #to log 1 3 4 5 7 10")
bst.in_order() #to log 1 3 4 5 7 10
print("Post order #to log 1 4 3 10 7 5")
bst.post_order() #to log 1 4 3 10 7 5