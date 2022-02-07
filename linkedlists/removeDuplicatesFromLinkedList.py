# This is an input class. Do not edit.

import unittest



class LinkedList():

    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

def removeDuplicatesFromLinkedList(linkedList):
    curNode = linkedList
    while curNode is not None:
        nextNode = curNode.next
        while nextNode is not None and nextNode.value == curNode.value:
            nextNode = nextNode.next
        curNode.next = nextNode
        curNode = nextNode
    return linkedList



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        original=test.getNodesInArray()
        expected = LinkedList(1).addMany([3, 4, 5, 6])
        eb=expected.getNodesInArray()
        removeDuplicatesFromLinkedList(test)
        ar = expected.getNodesInArray()
        print(original, ar,eb)
        self.assertEqual(ar, eb)


if __name__ == "__main__":
    unittest.main()