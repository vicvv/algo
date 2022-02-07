
# addQueue() This operation adds a new node after rear and moves rear to the next node.
# deQueue() This operation removes the front node and moves front to the next node.
# Python3 program to demonstrate linked list 
# based implementation of queue 

# A linked list (LL) node 
# to store a queue entry 
class Node: 
	
	def __init__(self, value): 
		self.value = value
		self.next = None

class Queue: 	
	def __init__(self): 
		self.front = self.last = None
    
	def isEmpty(self): 
		return self.front is None
     	
	#Method to add an item to the queue 
	def EnQueue(self, item): 
		temp = Node(item) 
		if self.last == None: 
			self.front = self.last = temp 
			return
		self.last.next = temp 
		self.last = temp 
    
	# Method to remove an item from queue 
	def DeQueue(self): 	
		if self.isEmpty(): 
			return None
		temp = self.front 
		self.front = self.front.next
		# if(self.front == None): 
		# 	self.last = None
		return temp.value 

# Driver Code 
if __name__== '__main__': 
	q = Queue() 
	q.EnQueue(10) 
	q.EnQueue(20) 
	print("Dequeued item is " ,q.DeQueue() )
	print("Dequeued item is " ,q.DeQueue() )
	#q.EnQueue(30) 
	#q.EnQueue(40) 
	#q.EnQueue(50) 
	print("Dequeued item is " ,q.DeQueue() )
	print("Dequeued item is " ,q.DeQueue() )
	print("Dequeued item is " ,q.DeQueue() )
	print("Dequeued item is " ,q.DeQueue() )
	print("Dequeued item is " ,q.DeQueue() )

	
	print("Dequeued item is " , q.DeQueue()) 
	
