
'''
You're given two Linked Lists of potentially unequal length. Each
Linked List represents a non-negative integer, where each node
in the Linked List is a digit of that integer, and the first node in
each Linked List always represents the least significant digit of
the integer. Write a function that returns the head of a new
Linked List that represents the sum of the integers represented
by the two input Linked Lists.
Each LinkedList node has an integer value as well as a
next node pointing to the next node in the list or to None /
null if it's the tail of the list. The value of each
LinkedList node is always in the range of 0 - 9 .
Note: your function must create and return a new Linked List,
and you're not allowed to modify either of the input Linked Lists.

O(max(n, m)) time | O(max(n, m)) space - where n is the
length of the first Linked List and m is the length of the
second Linked List

'''


import unittest

# O(max(n, m)) time | O(max(n, m)) space - where n
# first Linked List and m is the length of the seco
def sumOfLinkedLists(linkedListOne, linkedListTwo):
 # This variable will store a dummy node whose .
 # attribute will point to the head of our new L
    newLinkedListHeadPointer = LinkedList(0)
    currentNode = newLinkedListHeadPointer
    carry = 0
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne is not None or nodeTwo is not None or carry !=0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo + carry
        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode = newNode
        carry = sumOfValues // 10
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None
    return newLinkedListHeadPointer.next


class LinkedList:
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


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        ll1 = LinkedList(2).addMany([4, 7, 1])
        ll2 = LinkedList(9).addMany([4, 5])
        expected = LinkedList(1).addMany([9, 2, 2])
        actual = sumOfLinkedLists(ll1, ll2)
        self.assertEqual(getNodesInArray(actual), getNodesInArray(expected))

if __name__ == "__main__":
    unittest.main()