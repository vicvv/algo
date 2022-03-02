
'''
Write a function that takes in the head of a Singly Linked List and
returns a boolean representing whether the linked list's nodes
form a palindrome. Your function shouldn't make use of any
auxiliary data structure.
A palindrome is usually defined as a string that's written the
same forward and backward. For a linked list's nodes to form a
palindrome, their values must be the same when read from left
to right and from right to left. Note that single-character strings
are palindromes, which means that single-node linked lists form
palindromes.
Each LinkedList node has an integer value as well as a
next node pointing to the next node in the list or to None /
null if it's the tail of the list.
You can assume that the input linked list will always have at least
one node; in other words, the head will never be None / null .
'''

import unittest
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    is_palindrome_result =  is_palindrome(head, head)
    return is_palindrome_result.others_equal


def is_palindrome(leftnode, rightnode):
    if rightnode is None:
        return LinkedListInfo(True, leftnode)

    recursive_calles_results = is_palindrome(leftnode, rightnode.next)
    leftnodetocompare = recursive_calles_results.leftnodetocompare
    others_equal = recursive_calles_results.others_equal

    recurciveisequal = others_equal and leftnodetocompare.value == rightnode.value
    nextleftnodetocompare = leftnodetocompare.next

    return LinkedListInfo(recurciveisequal, nextleftnodetocompare)

class LinkedListInfo:
    def __init__(self, others_equal, leftnodetocompare):
        self.others_equal= others_equal
        self.leftnodetocompare = leftnodetocompare
    
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