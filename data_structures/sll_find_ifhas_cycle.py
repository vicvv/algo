# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head is None:
#             return False
#         slow = head
#         fast = head.next
#         while slow !=fast:
#             if fast is None or fast.next is None:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True

class StartLinkedList:
    def __init__(self, value=None):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = StartLinkedList(0)

    def addMany(self, values):
        current = self.head
        # while current.next is not None:
        #     current = current.next
        for value in values:
            current.next = StartLinkedList(value)
            current = current.next
        return self

    def __repr__(self):
        runner = self.head
        res=[]
        while runner:
            res.append(str(runner.value))
            runner = runner.next
        return ' -> '.join(res)
        

obj=LinkedList().addMany([1,2,3,4])
print(obj.head.value)
print(obj)

def hascycles(head):
    seenobjects = set()
    while head is not None:
        if head is seenobjects:
            return True
        seenobjects.add(head)
        head = head.next
    return False


def hascyles2(head):
    if head is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

print(hascycles(obj.head))

def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False






            

