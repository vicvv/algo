'''
Algorithm:

Initiate sentinel node as ListNode(0) and set it to be the new head: sentinel.next = head.
Initiate two pointers to track the current node and its predecessor: curr and prev.
While curr is not a null pointer:
Compare the value of the current node with the value to delete.
In the values are equal, delete the current node: prev.next = curr.next.
Otherwise, set predecessor to be equal to the current node.
Move to the next node: curr = curr.next.
Return sentinel.next.


'''
class ListNode:
    def __init__(self, val= None, next=None):
        self.val = val
        self.next = next

    def addvalues(self, values):
        current = self
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return self

    # def removeElementsByValue(self,v):
    #     sentinel = ListNode(0)
    #     sentinel.next = self

    #     prev, current = sentinel, self
    #     while current:
    #         if current.val == v:
    #             prev.next = current.next
    #         else:
    #             prev = current
    #         current = current.next

    #     return self

    def removeElementsByValue(self,v):
        sentinel = ListNode(0)
        sentinel.next = self      
        prev, curr = sentinel, self
        while curr:
            if curr.val == v:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next       
        return self

    def __repr__(self):
        node = self
        res =[]
        while node:
            res.append(str(node.val))
            node = node.next
        res.append("None")
        return ' -> '.join(res)

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.val)
            current = current.next
        return nodes
 
import unittest


class TestClass(unittest.TestCase):
    def test_case_1(self):
        test = ListNode().addvalues([1,2,3,4,5,6,5,6,7,7,7,7]) 
        test.removeElementsByValue(6)   
        expected = ListNode().addvalues([1,2,3,4,5,5,7,7,7,7])
        print(test)
        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())

    def test_case_2(self):
        test = ListNode().addvalues([7,7,7,7]) 
        test.removeElementsByValue(7)   
        expected = ListNode().addvalues([])
        print(test)

        self.assertEqual(test.getNodesInArray(), expected.getNodesInArray())
            
            

if __name__ == "__main__":
    unittest.main()
