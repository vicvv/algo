'''
Given the head of a singly linked list, group all the nodes with odd indices together 
followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
'''


class ListNode:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def add_many1(self, values):
        current = self

        for value in values:
            current.next = ListNode(value)
            current = current.next
        return self

    def add_many(self, values):
        current = self
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return self

    def oddEvenList(self):
        odd = self
        even = self.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return self

    
    def get_nodes_into_array(self):
        node = self
        array = []
        while node:
            array. append(node.value)
            node = node.next
        return array


    def __repr__(self):
        node = self
        res =[]
        while node:
            res.append(str(node.value))
            node = node.next
        res.append("None")
        return ' -> '.join(res)


import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = ListNode(0).add_many([1,2,3,4,5])
        print(test)
        test.oddEvenList()   
        expected = ListNode(0).add_many([2,4,1,3,5])
        print(test)
        self.assertEqual(test.get_nodes_into_array(), expected.get_nodes_into_array())

    # def test_case_2(self):
    #     test = ListNode().add_many([]) 
    #     test.oddEvenList()   
    #     expected = ListNode().add_many([])
    #     print(test)
    #     self.assertEqual(test.get_nodes_into_array(), expected.get_nodes_into_array())


if __name__ == "__main__":
    unittest.main()


