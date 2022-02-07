class PriorityQueue:
    def __init__(self):
    	self.head = None
    #add the given value to the end of the queue
    def add(self, value, priority):
        newNode = Node(value,priority)
        if self.head is None:
            self.head = newNode
            return 
        elif self.head is not None and self.head.priority < priority:
            newNode.next = self.head
            self.head = newNode

        else:
            node = self.head
            prev = node
            while node.next is not None and node.priority > priority:
                prev = node
                node = node.next
            node = newNode
            node.next = prev.next
            prev.next = node
            
        return self
        

    
    def print(self):
        runner = self.head
        while runner != None:
        	print(runner.value)
        	runner = runner.next

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

p_queue = PriorityQueue()
p_queue.add("eat healthy", 5)
p_queue.add("buy a gift for a friend's birthday party next week", 3)
p_queue.add("take a shower", 8)
p_queue.add("take the test today!", 10)

p_queue.print()

#p_queue.print() 
# -take the test today! 
# -take a shower 
# -eat healthy 
# -buy a gift for a friend's birthday party next week