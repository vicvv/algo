'''Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's val (in string format) should be put in the exactly middle 
of the first row it can be put. The column and the row where the root node belongs 
will separate the rest space into two parts (left-bottom part and right-bottom part). 
You should print the left subtree in the left-bottom part and print the right subtree in the 
right-bottom part. The left-bottom part and the right-bottom part should have the same size. 
Even if one subtree is none while the other is not, you don't need to print anything for the 
none subtree but still need to leave the space as large as that for the other subtree. 
However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].'''

'''
class Solution:
    def get_tree_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_tree_height(root.left), self.get_tree_height(root.right))
    
    def helper(self, root, l, r, cur_level):
        if not root:
            return
        # determine the index of the list where the "" has to be replaced by value
        root_index = l + (2**(self.h - cur_level - 1)) - 1
        # replace "" with the value stored in the node
        self.res[cur_level][root_index] = str(root.val)
        # traverse the left and right subtree
        self.helper(root.left, l, root_index - 1, cur_level + 1)
        self.helper(root.right, root_index + 1, r, cur_level + 1)
    
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # determine the height of the tree
        self.h =self.get_tree_height(root)
        # initialise the result 2D list with ""
        self.res = [['' for _ in range(2**self.h - 1)] for _ in range(self.h)]
        # call the recursive function to fill the result 2D list
        self.helper(root, 0, 2**self.h - 1, 0)
        # return the result
        return self.res
'''

class BST:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    
    def insert(self,val):
        curNode = self
        while True:
            if val < curNode.value:
                if curNode.left is None:
                    curNode.left = BST(val)
                    break
                else:
                    curNode = curNode.left
            else:               
                if curNode.right is None:
                    curNode.right = BST(val)
                    break
                else:
                    curNode = curNode.right
        return self


def printInOrder(tree,array) :
    if tree is not None:
        array.append(tree.value)
        printInOrder(tree.left, array)  
        printInOrder(tree.right, array)
    return array

test = BST(10).insert(9).insert(15).insert(12).insert(8).insert(6)

print(printInOrder(test,[]))

def getTreeHeight(node):
    if node is None:
        return 0
    return 1 + max(getTreeHeight(node.left), getTreeHeight(node.right))

def printTreeAsMatrix(tree):
    


       


       

        