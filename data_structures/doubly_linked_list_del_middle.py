class DoublyLinkedList:
    def __init__(self):
    	self.head = None
    	self.tail = None
    
    #add the given value to the end of the queue
    def add_back(self, val):
    	runner = self.tail
    	if runner == None:
    		self.head = Node(val)
    		self.tail = self.head # have tail point to the first node also
    		return
    
    	node = Node(val)
    	runner.next = node
    	node.prev = runner
    	self.tail = node
    	
    # remove the node in the middle of the list
    # have the function return false if the list has even number of nodes
    # def remove_middle(self):
    #     arr = []
    #     runner = self.head
    #     while runner is not None:
    #         arr.append(runner.value)
    #         runner = runner.next
        
    #     if len(arr)%2 == 0: return False   
    #     mid = len(arr) // 2 

    #     node = self.head
    #     while node is not None and node.value != arr[mid]:
    #         node = node.next
    #     if node.prev is not None:
    #         node.prev.next = node.next
    #     if node.next is not None:
    #         node.next.prev = node.prev
    #     temp = node
    #     node.next = None
    #     node.prev = None
    #     return temp.value if temp is not None else False 
    
    def remove_middle(self):
        count = 0
        node = self.head

        while node is not None:
            node = node.next
            count += 1
        
        if count%2 == 0: return False

        nodeleft = self.head
        noderight = self.tail

        while nodeleft != noderight:
            nodeleft = nodeleft.next
            noderight = noderight.prev
        
        nodeleft.prev.next = nodeleft.next
        nodeleft.next.prev = nodeleft.prev
        return nodeleft.value if nodeleft is not None else False

      	
    
    # function to print each value in the list starting from the head
    def print_forward(self):
    	runner = self.head
    	while runner != None:
    		print(runner.value, end = ' ')
    		runner = runner.next
    # have the runner start from the tail
    def print_backward(self):
    	runner = self.tail
    	while runner != None:
    		print(runner.value, end = ' ')
    		runner = runner.prev

class Node:
    def __init__(self, value):
    	self.value = value
    	self.prev = None
    	self.next = None 

dll = DoublyLinkedList()
dll.add_back(1)
dll.add_back(3)
dll.add_back(5)
dll.add_back(7)
dll.add_back(9)

dll.print_forward()
print("\n")

print(dll.remove_middle()) #to return 5

dll.print_forward() #to log 1 3 7 9
print("\n")
dll.remove_middle()

dll.print_backward() #o log 9 7 3 1

# dll.remove_middle()