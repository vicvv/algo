class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val,end=" ")
        printInorder(root.right)


def height(node):

    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def diameter(root):

    if root is None:
        return 0

    LH = height(root.left)
    RH = height(root.right)

    LD = diameter(root.left)
    RD = diameter(root.right)

    return max(LH + RH + 1, max(LD, RD))

if __name__ == '__main__':

    Root = Node(100)
    Root.left = Node(200)
    Root.right = Node(300)

    Root.left.right = Node(400)
    Root.left.left = Node(500)
    Root.right.left = Node(600)
    Root.right.right = Node(700)
    print('\n')
    print('Inorder Traversal of BT is:')
    printInorder(Root)
    print('\n')
    print('Diameter of BT is:{}'.format(diameter(Root)))

else:
    pass