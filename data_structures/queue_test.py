class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Q:
    def __init__(self):
        self.first = self.last = None

    def isEmpty(self):
        return self.first is  None

    def enQ(self, value):
        nn = Node(value)

        if self.first is None:
            self.last = self.first = nn
            return self
        
        self.last.next = nn
        self.last = nn

    def deQ(self):
        if self.first is None:
            return False
        temp = self.first
        self.first = self.first.next
        return temp.value

q = Q()

q.enQ(1)
q.enQ(2)
q.enQ(3)
q.enQ(4)

print(q.deQ())
print(q.deQ())
print(q.deQ())
print(q.deQ())
print(q.deQ())
print(q.deQ())




