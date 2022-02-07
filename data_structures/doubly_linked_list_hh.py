class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # add the given value to the end of the queue
    def push(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = self.tail = newNode
            self.head.prev = None
            self.tail.next = None
            return self
        # here is when we want to add to tail
        # newNode.prev = self.tail
        # self.tail.next = newNode
        # self.tail = newNode
        # return self
        self.head.prev = newNode    
        newNode.next = self.head
        newNode.prev = None
        self.head = newNode
        return self
 
    # remove & return value at front of queue.
    def pop(self):
        if self.head is None:
            return self
        if self.head != self.tail:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            return temp.value
        else:
            temp = self.head
            self.head = self.tail = None
            return temp.value
   
    #return the value at front of the queue, without removing it
    def front(self):
        return self.head.value if self.head is not None else False
   
    # return whether given value is found within the queue
    def back(self, val):
        return self.tail.value if self.tail is not None else False

    # returns whether our queue contains no values
    def contains(self, val):
        # if self.head is None:
        #     return False
        node = self.head
        while node is not None and node.value != val:
            node = node.next
        return node is not None

    
    # returns the number of values in our queue.
    def size(self):
        node,count = self.head,0
        #count = 0
        while node is not None:
            node = node.next
            count += 1

        return count
  

    def print_forward(self):
        runner = self.head
        while runner != None:
            print(runner.value, end = ' ')
            runner = runner.next
        
    def print_backward(self):
        runner = self.tail
        while runner != None:
            print(runner.value, end = ' ')
            runner = runner.prev
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
		    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

dll = DoublyLinkedList()
print(dll.size())
dll.push("James")
dll.push("Bond")
dll.push("007")



print("print_forward to log '007 Bond James'") ; dll.print_forward() 
print("\n")

print("\nprint_backward #to log 'James Bond 007'"); dll.print_backward() 
print("\n")
print("\npop to return 007:", dll.pop())
print("\n")

print('\nprint_forward #to log "Bond James"'); dll.print_forward() 
print("\n")

dll.pop()

print('\n #to return 007:dll.front ',  dll.front())
print("\n")

print('\n#to return James:ddl.back',dll.back("James") )
print("\n")

print('\n#to return "False"', dll.contains("008"), )
print("\n")

print( '#to return True',dll.contains("007"))
print("\n")

print('#to return "3"',dll.size(), )
print("\n")

print('#to return "2"', dll.size() )
print("\n")

print(dll.pop())
print('\n#to log "James"'); dll.print_backward()
print("\ncurrent size:" ,dll.size())
dll.pop()
dll.pop()
dll.pop()
dll.pop()
print("\nwhat's in the list still"); dll.print_backward()
 

import unittest

# class TestProgram(unittest.TestCase):
#     dll = DoublyLinkedList()
#     dll.push("James")
#     dll.push("Bond")
#     dll.push("007")
#     def test1(self):
#         self.assertEqual(dll(),)