

'''
Task
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. 
You are given a pointer, , pointing to the root of a binary search tree. Complete the getHeight 
function provided in your editor so that it returns the height of the binary search tree.
'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        return -1 if root is None else (1+ max(self.getHeight(root.left) , self.getHeight(root.right)))
    

T=[1,2,3,4,5,6,7,8,]
myTree=Solution()
root=None
for i in range(len(T)):
    #data=int(input())
    root=myTree.insert(root,i)
height=myTree.getHeight(root)
print(height)