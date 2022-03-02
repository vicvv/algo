'''
Zip Linked List
You're given the head of a Singly Linked List of arbitrary length k . Write a
function that zips the Linked List in place (i.e., doesn't create a brand new
list) and returns its head.

A Linked List is zipped if its nodes are in the following order, where k is the
length of the Linked List:

Each LinkedList node has an integer value as well as a next node
pointing to the next node in the list or to None / null if it's the tail of the
list. You can assume that the input Linked List will always have at least one
node; in other words, the head will never be None / null .

O(n) time | O(1) space - where n is the length of the input Linked List
'''

import unittest
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

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

    def __repr__(self):
        node = self
        arr =[]
        while node.next:
            arr.append(str(node.value))
            node = node.next
        arr.append('None')
        return ' -> '.join(arr)

def zipLinkedList(linkedList):
    print(linkedList)
    if linkedList.next is None or linkedList.next.next is None:
        return linkedList
    first_half_head = linkedList
    second_half_head = splitLinkedList(linkedList)
    reversedsecond_half_head = reverseLinkedList(second_half_head)
    return interweaveLinkedLists(first_half_head, reversedsecond_half_head)

def splitLinkedList(linkedList):
    print("in_split:", linkedList)
    slow = linkedList
    fast = linkedList
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    second_half_head = slow.next
    slow.next = None
    print("second_half", second_half_head)
    return second_half_head

def interweaveLinkedLists(linkedList1, linkedList2):
    linked_list1_iter = linkedList1
    linked_list2_iter = linkedList2
    while linked_list1_iter is not None and linked_list2_iter is not None:
        linked_list1_iter_next = linked_list1_iter.next
        linked_list2_iter_next = linked_list2_iter.next
        linked_list1_iter.next = linked_list2_iter
        linked_list2_iter.next = linked_list1_iter_next
        linked_list1_iter = linked_list1_iter_next
        linked_list2_iter = linked_list2_iter_next
    return linkedList1


def reverseLinkedList(linkedList):
    previous, current = None, linkedList
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = LinkedList(1).addMany([2, 3, 4, 5, 6])
        print(head)
        expected = [1, 6, 2, 5, 3, 4]
        actual = zipLinkedList(head).getNodesInArray()
        print(head)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()