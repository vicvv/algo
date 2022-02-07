class Stack:
    def __init__(self):
    	self.head = None
    	self.tail = None
    
    #add the given value to the end of the stack
    def push(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = self.tail = newNode
            return self
        temp = self.head
        self.head = newNode
        self.head.next = temp
        return self
        
   
    # remove & return value at front of stack.
    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp.value if temp is not None else self
    
    #return the value at front of the stack, without removing it
    def top(self):
        return self.head.value if self.head is not None else self #False???

    
    # return whether given value is found within the stack
    def contains(self, val):
        node = self.head
        while node is not None and node.value !=val:
            node = node.next
        return node is not None
    
    # returns whether our stack contains no values
    def isEmpty(self):
        return self.head is None

    
    # returns the number of values in our stack.
    def size(self):
        count = 0
        node = self.head
        while node is not None:
            node = node.next
            count +=1
        return count
    	
    def print(self):
        runner = self.head
        while runner != None:
            print(runner.value, end =' ')
            runner = runner.next

class Node:
    def __init__(self, value):
    	self.value = value
    	self.next = None

stack = Stack()
print(stack.isEmpty())
stack.push("Peter")
stack.push("Ben")
stack.push("Parker")
print(stack.isEmpty(), '\n')
print('stak size: ',stack.size()) #to return 3
print('#to log Parker Ben Peter')
stack.print() 

print("\n")
print('pop to return Parker:', stack.pop() )

stack.print() #to log Ben Peter
print(stack.size()) #to return 3
print('top:', stack.top()) # to return Parker
print(stack.isEmpty()) #to return False




