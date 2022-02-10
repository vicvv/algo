
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    count = 0
    def __init__(self):
        self.head = SLNode(0)

    def add_to_front(self, data):
        
        if self.head is not None:
            temp = self.head
            self.head = SLNode(data)
            self.head.next = temp
            SList.count += 1
        else:
            self.head = SLNode(data)
            SList.count += 1
        return self

    def add_to_back(self, data):
        if self.head is None:	
            self.add_to_front(data)	
            SList.count += 1
            return self	
        new_node = SLNode(data)
        curent = self.head
        while (curent.next is not None):
            curent = curent.next
        curent.next = new_node
        SList.count += 1
        return self 


    def insert_at(self, data, position):
        if self.head is  None:	# if the list is empty
            self.add_to_front(data)	# run the add_to_front method
            SList.count += 1
            return self   
        newNode = SLNode(data)  
        previous = None
        current = self.head
        current_position = 0
        while (current_position < position) and current.next:
            previous = current
            current = current.next
            current_position += 1
        previous.next = newNode
        newNode.next = current
        SList.count += 1
        return self

  
    # remove_from_front(self) - remove the first node and return its value

    def remove_from_front(self):
        if self.head is None:
            print("The list has no element to delete")
            return self
        #if we want to print a value of deleted node from the head
        temp = self.head.value
        self.head = self.head.next
        SList.count -= 1
        #rint(temp)
        return self

    # remove_from_back(self) - remove the last node and return its value

    def remove_from_back(self):
        if self.head is None:
            print("The list has no element to delete")
            return self
        
        elif self.head.next is None:
            temp = self.head
            # self.head.next = None
            self.head = None
            SList.count -= 1
            return temp.value
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            temp = current.next.value
            current.next = None
            SList.count -= 1
            print (temp)
            return self
            
    # delete_element_by_value(self, val) - remove the first node with the given value

    def delete_element_by_value(self, value):
        if self.head is None:
            print("The list has no element to delete")
            return

        # Deleting first node if it is a first node has that value
        if self.head.value == value:
            self.head = self.head.next
            SList.count -= 1
            return self

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                break
            current = current.next

        if current.next is None:
            print("item not found in the list")
        else:
            current.next = current.next.next
            SList.count -= 1
        return self

    def print_values(self):
        if self.head is None:
            return False
        current = self.head
        #print("MY LIST:  ", end = '')
        while (current != None):
            print(current.value, end = ' ')
            current = current.next 	# set the runner to its neighbor
        return self # once the loop is done, return self to allow for chaining


my_list = SList()	# create a new instance of a list
print("\n\nCreating new linked list:  ", end ='')
my_list.add_to_front("TPP,").add_to_front("FirstToFornt,").add_to_back("VTT").print_values()
print("\nTotal Nodes Count in the list:", my_list.count)

print("\nInserting new node at positon 2 and 3:")
my_list.insert_at('PPL,',2).insert_at('COT,',3).print_values()
print("\nTotal Nodes Count in the list:", my_list.count)

print("\n**********************\n")
print("After deleting the last element: ", end='')
my_list.remove_from_back().print_values()
print("\nTotal Nodes Count in the list:", my_list.count)



print("\nRemoving first element.....")
my_list.remove_from_front().print_values()

print ("\nDelete element by given value")

my_list.delete_element_by_value("fun").print_values()
print("\nTotal Nodes Count in the list:", my_list.count)
print("\nvvvv","*"*50)


my_list.remove_from_back().print_values()
print("\nTotal Nodes Count in the list:", my_list.count)
my_list.remove_from_back().print_values()
print("\nTotal Nodes Count in the list:", my_list.count)
