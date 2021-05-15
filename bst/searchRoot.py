'''
Given the node node of a binary search tree (BST) and a value. You need to find the node 
in the BST that the node's value equals the given value. Return the subtree nodeed with that node. 
If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is 
no node with value 5, we should return NULL.Note that an empty tree is represented by NULL, 
therefore you would see the expected output (serialized tree format) as [], not null.
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if self.val > value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

def searchBST(node, value):
    if node.val == value:
        return node
    while node is not None and node.val != value:
        node = node.left if node.val > value else node.right
    return Traverse(node)

def Traverse(node):
    if node is None:
        return  
    print(node.val)
    Traverse(node.left)
    Traverse(node.right)

node = TreeNode(4)
node.insert(2)
node.insert(1)
node.insert(3)
node.insert(5)
node.insert(6)

searchBST(node,2)


