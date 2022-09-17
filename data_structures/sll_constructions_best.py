
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        #self.head = ListNode(0)  # sentinel node as pseudo-head
        self.head = ListNode()
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size += 1
        # find tempecessor of the node to be added
        temp = self.head
        for _ in range(index):
            temp = temp.next
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = temp.next
        temp.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        # find tempecessor of the node to be deleted
        temp = self.head
        for _ in range(index):
            temp = temp.next
            
        # delete temp.next 
        temp.next = temp.next.next

    def print_values(self):
        if self.head is None:
            return False
        current = self.head
        #print("MY LIST:  ", end = '')
        while (current != None):
            print(current.val, end = ' ')
            current = current.next 	# set the runner to its neighbor
        print()
        return self # once the loop is done, return self to allow for chaining

#object representation function. called as class name
    def __repr__(self):
        node = self.head
        res = []
        while node is not None:
            res.append(str(node.val))
            node = node.next
        res.append("None")
        return " -> ".join(res)



# MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(0)
obj.addAtHead(1)
obj.addAtTail(10)
obj.addAtIndex(1,1)
obj.addAtIndex(2,2)
obj.addAtIndex(3,3)
obj.print_values()
obj.deleteAtIndex(1)
obj.print_values()
print(obj)
print(obj.size)
obj.addAtIndex(5,2)
print(obj)
