class Slist:
    def __init__(self):
        self.head = None
        
    def add(self, value):       
        if self.head is None:
            self.head = Node(value)
            return
        runner = self.head
        while runner.next != None :
            runner = runner.next

        runner.next = Node(value)

    def remove_from_back(self):
        if self.head is None:
            return False
        if self.head.next is None:
            temp = self.head.value
            self.head = None
            return temp
        else:
            runner = self.head
            while runner.next is not None:
                runner = runner.next

            temp = runner.value
            runner = None
            return temp

        
    def print_values(self):
        runner = self.head
        #print(runner.value)
        while runner is not  None :
            print(runner.value, end = ' ')
            runner = runner.next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

list = Slist()
list.add(3)
list.add(5)



print(list.remove_from_back()) #to return 5

print("what left in the list")
list.print_values()


print(list.remove_from_back()) #to return 3

print("what left in the list")
list.print_values()


# print(list.remove_from_back())

# list.remove_from_back() #to return False

# list.remove_from_back()

# list.remove_from_back()
# print("what left in the list")
# list.print_values()



