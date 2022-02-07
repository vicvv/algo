import math

class Hash:
    #when initialized, creates N buckets in the array.  Have it store an empty singly linked list
    def __init__(self, n):
        self.buckets = []
        self.total_buckets = n
        
        for _ in range(0, n):
            self.buckets.append(SSL())
       
    # based on the key, have it return the appropriate index to look
    def hash_function(self, key):
        number = self._generate_hash(key)
        rnumber = number%self.total_buckets
        return rnumber
    
    def add(self, key, value):
        number = self.hash_function(key)       
        mylist = self.buckets[number]
        mylist.add(key,value)
   
    def retrieve(self,key):
        number = self.hash_function(key)
        mylist = self.buckets[number]
        return mylist.retrieve(key)

    # generates a hash number given a string
    def _generate_hash(self, strr):
    	hash = 0
    	if len(strr) == 0:
    		return hash
    	for i in range(0, len(strr)):
    		char = ord(strr[i])
    		hash = ((hash<<5)-hash)+char
    		hash = hash & hash # Convert to 32bit integer
    	return hash

class SSL:
    def __init__(self):
    	self.head = None
    
    def add(self, key, value):
        if self.head == None:
            self.head = Node(key, value)
            return self.head
        runner = self.head
        while runner is not None:
            runner = runner.next
        runner.next = Node(key,value)
    
    def retrieve(self, key):
        runner = self.head
        while runner is not None:
            if runner.key == key:
                return runner.value
            runner= runner.next
        return False
class Node:
    def __init__(self, key, value):
    	self.next = None
    	self.key = key
    	self.value = value
# create a hash map with 256 buckets
hash_map = Hash(256)


print(hash_map.hash_function("hackerhero")) # to return 136

hash_map.add('name', 'Michael')

print(hash_map.retrieve('name') ) # to return Michael
print(hash_map.retrieve('phone') ) # to return False
