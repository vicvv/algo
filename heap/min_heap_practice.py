
class MinHeap:
    def __init__(self, array):       
        self.heap = self.buildHeap(array)

	# O(n) time |O(1) space
    def buildHeap(self, array):
        # grabbing final ele of array and getting its parrent
        firstParrentIdx = (len(array) - 1) // 2 
        for currentIdx in reversed(range(firstParrentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array
	# O(log(n) time |O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx  = currentIdx * 2 +1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx*2 + 2 if currentIdx *2+2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
                
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx,idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx *2+1
            else:
                break
            
	# O(log(n) time |O(1) space
    def siftUp(self, currentIndex,  heap):
        parrentIdx = (currentIndex -1) // 2
        while currentIndex > 0 and heap[currentIndex] < heap[parrentIdx]:
            self.swap(currentIndex, parrentIdx, heap)
            currentIndex = parrentIdx
            parrentIdx =(currentIndex -1)//2
            

    def peek(self):
        return self.heap[0]

    # remove root value
    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0,len(self.heap)-1,self.heap)
        return valueToRemove
        

    def insert(self, value):
        #. add the value to the end of the array
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
        
	
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
    
    def printHeap(self):
        for i in self.heap:
            print(self.heap[i], end = ' ')

minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
minHeap.insert(76)

print(minHeap.peek())
minHeap.remove()
print(minHeap.peek())

import unittest
def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False
    return True




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
        minHeap.insert(76)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), -5)
        self.assertEqual(minHeap.remove(), -5)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 2)
        self.assertEqual(minHeap.remove(), 2)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 6)
        minHeap.insert(87)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))

# if __name__ == "__main__":
#     unittest.main()