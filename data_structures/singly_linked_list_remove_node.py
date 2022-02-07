#Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next
class SLL:
    def __init__(self):
        self.node = None

    def addfront(self, val):
        nn = ListNode(val)
        nn.next = self.node
        self.node = nn
    
    
def removeElements(head, val):
    start = ListNode(0)
    start.next = head
    prev, cur = start, head
    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
            
    return start.next

def printlist(node):
    runner = node
    while runner:
        print(runner.val, end = " ")
        runner = runner.next

#1->2->6->3->4->5->6
sl = ListNode()
sll = SLL()
sll.addfront(6)
printlist(sl)
sll.addfront(5)
sll.addfront(4)
sll.addfront(3)
sll.addfront(6)
sll.addfront(2)
sll.addfront(1)
print("printing list: ")
printlist(sl)
print("\n")



res = removeElements(sl,6)

printlist(res)