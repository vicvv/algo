
#something wrong with this

class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index>=self.size:
            return -1
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.val

    def addAtHead(self, val):
        self.head = self.addAtIndex(0, val)
        self.size += 1

    def addAtTail(self, val):
        if self.size==0:
            self.head = LinkedNode(val)
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = LinkedNode(val)
        self.size += 1

    def addAtIndex(self, index, val):
        if index<=self.size:
            if index==0:
                self.head = LinkedNode(val, self.head)
            else:
                temp = self.head
                prev = self.head
                for i in range(index):
                    prev = temp
                    temp = temp.next
                prev.next = LinkedNode(val, temp)
            self.size += 1
        

    def deleteAtIndex(self, index):
        if index<self.size:
            if index==0:
                self.head = self.head.next
            else:
                temp = self.head
                prev = self.head
                for i in range(index):
                    prev = temp
                    temp = temp.next
                prev.next = temp.next
            self.size -= 1
            
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedNode(value)
            current = current.next
        return self
    
    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes
    
    
#test = MyLinkedList.addMany([1, 2, 3, 4, 5]) 
test = MyLinkedList.addAtHead(5)    
            
            
'''
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
'''