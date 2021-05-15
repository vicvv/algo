
class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):
        
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            else:
                self.currentSize +=1
            self.cache[key] = DoublyLinkedListNode(key,value)
        else:
            self.replaceKey(key,value)
        self.updateMostRecent(self.cache[key])
            

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def getMostRecentKey(self):
        return self.listOfMostRecent.head.key
	
    def replaceKey(self, key, value):
        if key not in self.cache:
            return Exception("The key is not here")
        self.cache[key].value = value
		
    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        print(self.cache[keyToRemove])
        del self.cache[keyToRemove]
        
    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)

	
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
	
    def setHeadTo(self, node):
        if self.head == node:
            return
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node
	
	
    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print("most recent node value:", n.value)
                n = n.next


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
            
    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None


myc = LRUCache(3)
myc.insertKeyValuePair("a", 1)
myc.insertKeyValuePair("b", 2)
myc.insertKeyValuePair("c", 3)
myc.insertKeyValuePair("d", 4)

for key, values in  myc.cache.items():
    print(key, values.value)

# to print just a list
myc.listOfMostRecent.traverse_list()



import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        lruCache = LRUCache(3)
        lruCache.insertKeyValuePair("b", 2)
        lruCache.insertKeyValuePair("a", 1)
        lruCache.insertKeyValuePair("c", 3)
        self.assertEqual(lruCache.getMostRecentKey(), "c")
        self.assertEqual(lruCache.getValueFromKey("a"), 1)
        self.assertEqual(lruCache.getMostRecentKey(), "a")
        lruCache.insertKeyValuePair("d", 4)
        self.assertEqual(lruCache.getValueFromKey("b"), None)
        lruCache.insertKeyValuePair("a", 5)
        self.assertEqual(lruCache.getValueFromKey("a"), 5)


if __name__ == "__main__":
    unittest.main()


# [
#   {"arguments": ["a", 1], "method": "insertKeyValuePair"},
#   {"arguments": ["b", 2], "method": "insertKeyValuePair"},
#   {"arguments": ["c", 3], "method": "insertKeyValuePair"},
#   {"arguments": ["d", 4], "method": "insertKeyValuePair"},
#   {"arguments": ["a"], "method": "getValueFromKey"},
#   {"arguments": ["e", 5], "method": "insertKeyValuePair"},
#   {"arguments": ["a"], "method": "getValueFromKey"},
#   {"arguments": ["b"], "method": "getValueFromKey"},
#   {"arguments": ["c"], "method": "getValueFromKey"},
#   {"arguments": ["f", 5], "method": "insertKeyValuePair"},
#   {"arguments": ["c"], "method": "getValueFromKey"},
#   {"arguments": ["d"], "method": "getValueFromKey"},
#   {"arguments": ["g", 5], "method": "insertKeyValuePair"},
#   {"arguments": ["e"], "method": "getValueFromKey"},
#   {"arguments": ["a"], "method": "getValueFromKey"},
#   {"arguments": ["c"], "method": "getValueFromKey"},
#   {"arguments": ["f"], "method": "getValueFromKey"},
#   {"arguments": ["g"], "method": "getValueFromKey"}
# ]        
  

