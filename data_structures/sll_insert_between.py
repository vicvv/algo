class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add node
    def inBetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.val)
            printval = printval.next


slist = SLinkedList()
slist.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

slist.headval.next = e2
e2.next = e3

slist.inBetween(slist.headval.next,"Fri")
slist.listprint()