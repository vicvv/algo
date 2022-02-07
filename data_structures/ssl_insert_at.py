class Slist:
    def __init__(self):
    	self.head = None
    
    def add(self, value):
    	if self.head == None:
    		self.head = Node(value)
    		return
    
    	runner = self.head
    	while runner.next != None :
    		runner = runner.next
    
    	runner.next = Node(value)
    
    def insert_at(self, val, n):

        if self.head is None and n == 0:
            self.head = Node(val)
            return self
        elif self.head and n == 0:
            newNode = Node(val)
            temp = self.head
            self.head = newNode
            self.head.next = temp
            return self
        else:
            current = self.head
            count = 0
            temp = None
            while count < n and current.next:
                temp = current
                current = current.next
                count += 1
            if count + 1 == n:
                current.next = Node(val)
            else:
                newNode = Node(val)
                temp.next = newNode
                newNode.next = current
                return self
            
            

    def print_values(self):
    	runner = self.head
    	while runner != None :
    		print(runner.value, end = ' ')
    		runner = runner.next

class Node:
    def __init__(self, value):
    	self.value = value
    	self.next = None

list = Slist()
list.add(3)
list.add(5)
list.add(7)
print("original list")
list.print_values() 

list.insert_at(10, 0)
print("\nInserted 10 at 0")
list.print_values()  
# insert 10 in the beginning of the list
print("\nInserted 15 at 2")
list.insert_at(15, 2) 
list.print_values()  
# insert 15 in the middle of the list
print("\nInserted 25 at 5")
list.insert_at(25, 5)

# insert 25 at the end of the list
list.print_values() 


# #Test Cases (0/3)
# list.print_values() #to log 10 3 15 5 7 25

# list.print_values() #to log 77 10 3 15 5 7 25
print("\n")
list.insert_at(77, 0)

list.print_values() #to log 10 3 15 5 7 25 45
print("\n")
list.insert_at(45, 6)
list.print_values()