# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

#here add function to create a linked list from array
def createList(arr):
    head = ListNode()
    current = head
    for v in arr:
        toadd = ListNode(v)
        toadd.next = current.next
        current.next = toadd
    return head

def middleNode(arr):
    head = createList(arr)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow.val

print(middleNode([1,2,3,4,5,6,7]))