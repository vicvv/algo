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
            print(node.value)
            arr.append(str(node.value))
            node = node.next
        arr.append('None')
        return ' -> '.join(arr)

#iterative solution
# def nodeSwap(head):
#     temp = LinkedList(0)
#     temp.next = head
#     prev = temp

#     while prev.next and prev.next.next:
#         first = prev.next
#         second = prev.next.next
#         first.next = second.next
#         second.next = first
#         prev.next = second
        
#         prev = first
        
#     return temp.next

def nodeSwap(head):
    if head is None or head.next is None:
        return head
    next_node = head.next
    head.next = nodeSwap(head.next.next)
    next_node.next = head
    return next_node


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = LinkedList(0).addMany([1, 2, 3, 4, 5])
        expectedNodes = [1, 0, 3, 2, 5, 4]
        output = nodeSwap(linkedList)
        self.assertEqual(output.getNodesInArray(), expectedNodes)

if __name__ == '__main__':
    unittest.main()