class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    def __init__(self):
        self.head = None
        self.count = 0

    def addfront(self, val):
        self.count +=1
        nn = Node(val)
        nn.next = self.head
        self.head = nn

    def printlist(self):
        runner = self.head
        while runner:
            print(runner.value, end = " ")
            runner = runner.next

mylist = Slist()
mylist.addfront(3)
mylist.addfront(4)
mylist.addfront(5)
mylist.printlist()