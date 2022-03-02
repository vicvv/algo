'''
You're given the root node of a Binary Tree, a target value of a
node that's contained in the tree, and a positive integer k . Write
a function that returns the values of all the nodes that are exactly
distance k from the node with target value.
The distance between two nodes is defined as the number of
edges that must be traversed to go from one node to the other.
For example, the distance between a node and its immediate left
or right child is 1 . The same holds in reverse: the distance
between a node and its parent is 1 . In a tree of three nodes
where the root node has a left and right child, the left and right
children are distance 2 from each other.
Each BinaryTree node has an integer value , a left child
node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null .
Note that all BinaryTree node values will be unique, and your
function can return the output values in any order.
'''

import unittest
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space - where n is the number of nodes in the tree
def findNodesDistanceK(tree, target, k):
    nodesToParents = {}
    populateNodesToParents(tree, nodesToParents)
    targetNode = getNodeFromValue(target, tree, nodesToParents)
    return breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k)
def breadthFirstSearchForNodesDistanceK(targetNode, nodesToParents, k):
    # We could use the `deque` object instead of a standard Python
    # list if we wanted to optimize our `.pop(0) operations.`
    queue = [(targetNode, 0)]
    seen = {targetNode.value}
    while len(queue) > 0:
        currentNode, distanceFromTarget = queue.pop(0)
        if distanceFromTarget == k:
            nodesDistanceK = [node.value for node, _ in queue]
            nodesDistanceK.append(currentNode.value)
            return nodesDistanceK
        connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]
        for node in connectedNodes:
            if node is None:
                continue
            if node.value in seen:
                continue
            seen.add(node.value)
            queue.append((node, distanceFromTarget + 1))
    return []


def getNodeFromValue(value, tree, nodesToParents):
    if tree.value == value:
        return tree
    nodeParent = nodesToParents[value]
    if nodeParent.left is not None and nodeParent.left.value == value:
        return nodeParent.left
    return nodeParent.right
def populateNodesToParents(node, nodesToParents, parent=None):
    if node is not None:
        nodesToParents[node.value] = parent
        populateNodesToParents(node.left, nodesToParents, node)
        populateNodesToParents(node.right, nodesToParents, node)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        root.right.right.left = BinaryTree(7)
        root.right.right.right = BinaryTree(8)
        target = 3
        k = 2
        expected = [2, 7, 8]
        actual = findNodesDistanceK(root, target, k)
        actual.sort()
        self.assertCountEqual(actual, expected)
if __name__ == '__main__':
    unittest.main()