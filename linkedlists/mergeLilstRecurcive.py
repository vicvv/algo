# merge 2 soreted linked lists

# time O(n+m) | space O(1)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    pass

# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class LinkedListTest(LinkedList):
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


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        list1 = LinkedListTest(2).addMany([6, 7, 8])
        list2 = LinkedListTest(1).addMany([3, 4, 5, 9, 10])
        output = mergeLinkedLists(list1, list2)
        expectedNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(output.getNodesInArray(), expectedNodes)

if __name__ == "__main__":
    unittest.main()