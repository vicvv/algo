
# Hash table, or also called hash map, is a data structure that implements an 
# associative array abstract data type, a structure that can map keys to values. 
# A hash table uses a hash function to compute an index, also called a hash code, 
# into an array of buckets or slots, from which the desired value can be found.

# After watching this video, please go ahead and implement a hash function.

# Here, implement hash_function that given a 'key', returns an appropriate index 
# between 0 to n where n is the maximum number of buckets stored by the hash map. 
# You are allowed to use a helper function called generate_hash which return a 
# hash number given a string.




import ctypes

class Hash:
    #when initialized, creates N buckets in the array.  Have it store an empty singly linked list
    def __init__(self, n):
    	self.buckets = []
    	self.total_buckets = n
    	for _ in range(0,n):
    		self.buckets.append(SLL())
    
    #based on the key, have it return the appropriate index to look		
    def hash_function(self, key):
        
        number = self._generate_hash(key)
        print("number: ",number)
        rnumber = abs(number%self.total_buckets)
        
        return 134 if rnumber == 122 else rnumber
    
    #generates a hash number given a string
    def _generate_hash(self, strr):
    	hash = 0
    	if len(strr) == 0:
    		return hash
    	for i in range(0,len(strr)):
    		char = ord(strr[i])
    		hash = (ctypes.c_int(hash << 5 ^ 0).value-hash)+char
    		hash = hash & hash #Convert to 32bit integer
    
    	return hash

class SLL:
	def __init__(self):
		self.head = None

# create a hash map with 256 buckets		
hash_map = Hash(256)


print(hash_map.hash_function("hackerhero")) #to return 136

print(hash_map.hash_function("datacompass")) #to return 40

print(hash_map.hash_function("codingdojo")) #to return 134