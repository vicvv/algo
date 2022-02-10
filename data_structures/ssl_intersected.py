
'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen =set()
        while headA is not None:
            seen.add(headA)
            headA = headA.next
            
        while headB is not None:
            if headB in seen:
                return headB
            headB= headB.next
            
        return None