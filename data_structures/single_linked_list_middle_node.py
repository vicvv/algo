# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

#here add function to create a linked list from array
def createList(nodes):
    head = ListNode()
    current = head
    for v in nodes:
        toadd = ListNode(v)
        toadd.next = current.next
        current.next = toadd
    return head

def middleNode(nodes):
    head = createList(nodes)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow.val

print(middleNode([1,2,3,4,5]))