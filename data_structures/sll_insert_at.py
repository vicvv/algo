
class Node:
    def __init__(self, value):
    	self.value = value
    	self.next = None

class Sslst:
    def __init__(self):
        self.head = None
        self.size = 0
    
    # def add(self, value):
    #     if self.head == None:
    #         self.head = Node(value)
    #         return

    #     runner = self.head
    #     while runner.next:
    #         runner = runner.next

    #     nodeToAdd = Node(value)
    #     nodeToAdd.next = runner.next
    #     runner.next = nodeToAdd
    #     self.count +=1
    
    def add_at_head(self, value):
        self.addAtIndex(0,value)

    def add_at_tail(self, value):
        self.addAtIndex(self.size, value)
    
    
    def addAtIndex(self, index, val):
        #print(self.size, index == self.size)
        if index > self.size:
            return       
        if index < 0: index = 0 
        self.size += 1
        to_add = Node(val)
        
        if self.head is None:
            self.head = to_add
            return self
        elif self.head and index == 0:
            temp = self.head
            self.head = to_add
            self.head.next = temp
            return self
        else:
            pred = self.head
            print("index",index)
            for _ in range(index-1):
                #print(pred.value)
                pred = pred.next 
                       
            to_add.next = pred.next
            pred.next = to_add

    # def addAtIndex(self, index, val):
    #     #print(index, val)
    #     if index < 0: 
    #         index = 0
    #     if index > self.size:
    #         return 

    #     self.size += 1
    #     if self.head is None and index == 0:
    #         self.head = Node(val)
    #         return self
    #     elif self.head and index == 0:
    #         newNode = Node(val)
    #         temp = self.head
    #         self.head = newNode
    #         self.head.next = temp
    #         return self
    #     else:
    #         current = self.head
    #         count = 0
    #         temp = None
    #         while count < index and current.next:
    #             temp = current
    #             current = current.next
    #             count += 1
    #         if count + 1 == index:
    #             current.next = Node(val)
    #         else:
    #             newNode = Node(val)
    #             temp.next = newNode
    #             newNode.next = current
    #             return self
            
            

    def print_values(self):
        runner = self.head
        while runner != None :
            print(runner.value, end=' ')
            runner = runner.next
        print()



slst = Sslst()
slst.add_at_head(10)
slst.print_values() 
slst.add_at_head(1)
# slst.print_values() 
slst.add_at_head(3)
# slst.print_values() 
slst.addAtIndex(0,9)
print("size",slst.size)
slst.print_values() 
slst.addAtIndex(4,2)
slst.print_values() 

slst.add_at_tail(8)
slst.print_values() 
#slst.addAtIndex(12,3)
# slst.addAtIndex(0,10)
# print("\nInserted 10 at 0")
# slst.print_values()  
# insert 10 in the beginning of the slst
# print("\nInserted 15 at 2")
# slst.addAtIndex(15, 2) 
slst.print_values()  
# # insert 15 in the middle of the slst
# print("\nInserted 25 at 5")
# slst.addAtIndex(25, 5)

# # insert 25 at the end of the slst
# slst.print_values() 


# # #Test Cases (0/3)
# # slst.print_values() #to log 10 3 15 5 7 25

# # slst.print_values() #to log 77 10 3 15 5 7 25
# print("\n")
# slst.insert_at(77, 0)

# slst.print_values() #to log 10 3 15 5 7 25 45
# print("\n")
# slst.insert_at(45, 6)
# slst.print_values()