

def removeKthNodeFromEnd(head, n):
    first = second = head
    counter = 1
    while counter <=n:
        second = second.next
        counter +=1
    if second is  None:
        # # the 2 lines is in case if n is greater than the len of the list
        # # and in this case we remove first node
        # head.value, head.next = head.next.value, head.next.next
        # return

        # if we do not want to remove the firtst node because n > len of the list
        return head.next
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next

# LEET solution
    # first = second = head
    # count = 1
    # while second.next:
    #     second = second.next
    #     if count> n:
    #         first = first.next
    #     count +=1
    # if count == n:
    #     return head.next
    # first.next = first.next.next
    # return head



import unittest


class StartLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


linkedListClass = StartLinkedList


class LinkedList(linkedListClass):
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
        test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = LinkedList(0).addMany([1, 2, 3, 4, 5, 7, 8, 9])
        removeKthNodeFromEnd(test, 4)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())

   
    def test_case_2(self):
        test = LinkedList(0).addMany([1])
        expected = LinkedList(0).addMany([])
        removeKthNodeFromEnd(test, 1)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())


if __name__ == '__main__':
    unittest.main()