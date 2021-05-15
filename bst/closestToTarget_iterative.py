
# def findClosestValueInBst(tree, target):
#     closest = tree.value
#     while tree:
#         if abs(closest - target) > (tree.value - target):
#             closest = tree.value
#         if target < closest:
#             tree = tree.left
#         else:
#             tree = tree.right
#     return closest




import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


test = (
    BST(100)
    .insert(5)
    .insert(15)
    .insert(5)
    .insert(2)
    .insert(1)
    .insert(22)
    .insert(1)
    .insert(1)
    .insert(3)
    .insert(1)
    .insert(1)
    .insert(502)
    .insert(55000)
    .insert(204)
    .insert(205)
    .insert(207)
    .insert(206)
    .insert(208)
    .insert(203)
    .insert(-51)
    .insert(-403)
    .insert(1001)
    .insert(57)
    .insert(60)
    .insert(4500)
)



def findClosestValueInBst(tree, target):
    print(tree)
    print(target)
    return findClosestValueInBstHelper(tree, target,float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target-currentNode.value) < abs(target - closest):
            closest = currentNode.value
            print("closest",closest,currentNode.value, target)
        
        if target < currentNode.value:
            currentNode = currentNode.left
        if target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

print(findClosestValueInBst(test, 12))