class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SLL:
    
    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self
    
    def print_values(self):
        current = self.head
        print("MY LIST:  ", end = '')
        while (current != None):
            print(current.value, end = ' ')
            current = current.next 	# set the runner to its neighbor
        return self # once the loop is done, return self to allow for chaining


    def middleNode(self):
        fast = self.head
        slow = self.head
        if self.head:
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
        return slow.value

myl = SLL()
myl.add_to_front(6).add_to_front(5).add_to_front(4).add_to_front(3).add_to_front(2).add_to_front(1).print_values()
print()
print(myl.middleNode())


        