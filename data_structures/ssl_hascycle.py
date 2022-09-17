'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the index 
of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list
'''

from audioop import lin2adpcm
from cProfile import run
from ssl import HAS_SNI
from attr import has

from requests import head


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add_many(self, lst):
        self.head = ListNode(lst[0])
        current = self.head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return self
    
    def __repr__(self):
        runner = self.head
        res =[]
        while runner:
            res.append(str(runner.val))
            runner = runner.next
        return '-->'.join(res)
    
def hasCycles(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
        


test = LinkedList()
test.add_many([1,2,3,4,5])
print(test.head.val)
print(hasCycles(test.head))
obj = LinkedList() 
obj.add_many([3,2,0,-4, 2]) 
print(hasCycles(obj.head))         
            
            