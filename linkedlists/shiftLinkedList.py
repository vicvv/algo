def shiftLinkedList(head, k):
    listTail = head
    listLen = 1
    while listTail.next is not None:
        listTail = listTail.next
        listLen +=1

    offset = abs(k) % listLen
    if offset == 0:
        return head
    newTailPosition = listLen - offset if k > 0 else offset
    newTail = head

    for i in range(1, newTailPosition):
        newTail = newTail.next
        
    newhead = newTail.next
    newTail.next = None
    listTail.next = head
    return newhead
	


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

import unittest


def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(3)
        head.next.next.next.next = LinkedList(4)
        head.next.next.next.next.next = LinkedList(5)
        result = shiftLinkedList(head, 2)
        array = linkedListToArray(result)

        expected = [4, 5, 0, 1, 2, 3]
        self.assertEqual(expected, array)
    
    def test_case_2(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(3)
        head.next.next.next.next = LinkedList(4)
        head.next.next.next.next.next = LinkedList(5)
        result = shiftLinkedList(head, -2)
        array = linkedListToArray(result)

        expected = [2, 3, 4, 5, 0, 1]
        self.assertEqual(expected, array)

if __name__ == "__main__":
    unittest.main()
