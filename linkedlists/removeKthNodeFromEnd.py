# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    count = 1
    while count <=k:
        second = second.next
        count +=1
    if second is None:
        head.value, head.next = head.next.value, head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
    

import unittest


class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListClass = StartLinkedList
if hasattr(LinkedList,"LinkedList"):
    linkedListClass = LinkedList


class LinkedListTest(linkedListClass):
    def addMany(self, values):
        current = self
        # while current.next is not None:
        #     current = current.next
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


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedListTest(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = LinkedListTest(0).addMany([1, 2, 3, 4, 5, 7, 8, 9])
        removeKthNodeFromEnd(test, 4)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())


if __name__ == "__main__":
    unittest.main()