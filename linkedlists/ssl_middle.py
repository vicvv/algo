
class LinkedList:
    def __init__(self,value=0,next =None):
        self.next = None
        self.value = value
        
    def add(self, values):
        current = self
        #replace default value
        current.value = values[0]
        while current.next is not None:
            current = current.next
            
        for value in values[1:]:
            current.next = LinkedList(value)
            current = current.next
        # add the node with the last value in array
        #current.next = LinkedList(values[-1])
        return self
    
    def getNodesToArray(self):
        nodes =[]
        current = self
        while current.next is not None:
            nodes.append(current.value)
            current = current.next
        return nodes
    
    def __repr__(self) -> str:
        arr =[]
        node = self
        while node is not None:
            arr.append(str(node.value))
            node = node.next
        arr.append("None")
        return '-->'.join(arr)
    
    def find_mid(self):
        slow = self; fast = self
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.value
    
    
ssl = LinkedList()  
ssl.add([1,2,3,4,5])
print(ssl.getNodesToArray())
print(ssl)
print(ssl.find_mid())

