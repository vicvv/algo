class Queue:
    def __init__(self):
    	self.head = None
    	self.tail = None

    #add the given value to the end of the queue   
    def enqueue(self, val):
        newNode = Node(val)
        
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    
    # remove & return value at front of queue.
    def dequeue(self):
        if self.head is None:
            return False       
        temp = self.head
        self.head = self.head.next
        return temp.value        

    #return the value at front of the queue, without removing it
    def front(self):
        return self.head.value if self.head is not None else False
    
    # return whether given value is found within the queue
    def contains(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return True
            node = node.next
        return node is not None

     # returns whether our queue contains no values
    def isEmpty(self):
        return self.head == None
    # returns the number of values in our queue.
    def size(self):
        count = 0
        if self.head == None:
            return count
    
        node = self.head
        while node is not None:
            node = node.next
            count +=1
        return count


    def print(self):
            runner = self.head
            while runner != None :
                print(runner.value)
                runner = runner.next

class Node:
    def __init__(self, value):
    	self.value = value
    	self.next = None

queue = Queue()
print("Is empty?", queue.isEmpty())
print(queue.contains('V'))
queue.enqueue("Michael")
queue.enqueue("Joseph")
queue.enqueue("Sarah")
print("to log Michael Joseph Sarah", end ='')
queue.print() #to log Michael Joseph Sarah
queue.dequeue()
print("to log Joseph Sarah")
queue.print() #to log Joseph Sarah

queue.dequeue()

print("to log Sarah")
queue.print() #to log Sarah
print(queue.contains("Sarah")) #to return True

queue.dequeue()
queue.dequeue()
print(queue.size()) #to return 0
queue.dequeue()
queue.dequeue()
queue.dequeue()
print("Starting over")
print(queue.size())
queue.enqueue("Michael")
queue.enqueue("Joseph")
queue.enqueue("Sarah")
print(queue.size())
queue.print() #to log Michael Joseph Sarah

print(queue.front()) #to return Michael

queue.isEmpty() #to return False

queue.contains("Mike") #to return False

queue.contains("Sarah") #to return True

queue.dequeue() #to return Michael