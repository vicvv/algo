class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    slow=fast=head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    reversed_second_half = reverseLinkedList(slow)
    first_half_node = head

    while reversed_second_half:
        if reversed_second_half.value != first_half_node.value:
            return False
        reversed_second_half = reversed_second_half.next
        first_half_node = first_half_node.next
    return True


def reverseLinkedList(head):
    previous_node, current_node = None, head

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = LinkedList(0)
        head.next = LinkedList(1)
        head.next.next = LinkedList(2)
        head.next.next.next = LinkedList(2)
        head.next.next.next.next = LinkedList(1)
        head.next.next.next.next.next = LinkedList(0)
        expected = True
        actual = linkedListPalindrome(head)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()