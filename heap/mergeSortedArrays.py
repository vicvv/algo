def mergeSortedArrays(arrays):
    sortedList = []
    smallestItems = []
    for arrayIndex in range(len(arrays)):
        smallestItems.append({"arrayIndex":arrayIndex, "elementIndex" : 0, "num": arrays[arrayIndex][0]})
    minHeap = MinHeap(smallestItems)
    while not minHeap.isEmpty():
        # remove method always gives us min value
        smallestItem = minHeap.remove()
        arrayIndex,elementIndex, num = smallestItem["arrayIndex"] ,smallestItem["elementIndex"], smallestItem["num"]
        sortedList.append(num)
        if elementIndex == len(arrays[arrayIndex]) -1:
            continue
        minHeap.insert({"arrayIndex":arrayIndex, "elementIndex" : elementIndex +1, "num": arrays[arrayIndex][elementIndex + 1]})
    return sortedList		

class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
    def isEmpty(self):
        return len(self.heap) == 0
    # O(n) time |O(1) space
    def buildHeap(self, array):
        # grabbing final ele of array and getting its parrent
        firstParrentIdx = (len(array) - 2) // 2 
        for currentIdx in reversed(range(firstParrentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array
    # O(log(n) time |O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx  = currentIdx * 2 +1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx*2 + 2 if currentIdx *2+2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx]["num"] < heap[childOneIdx]["num"]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
                
            if heap[idxToSwap]["num"] < heap[currentIdx]["num"]:
                self.swap(currentIdx,idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx *2+1
            else:
                break
            
    # O(log(n) time |O(1) space
    def siftUp(self, currentIndex,  heap):
        parrentIdx = (currentIndex -1) // 2
        while currentIndex > 0 and heap[currentIndex]["num"] < heap[parrentIdx]["num"]:
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



import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrays = [
            [1, 5, 9, 21],
            [-1, 0],
            [-124, 81, 121],
            [3, 6, 12, 20, 150],
        ]
        output = mergeSortedArrays(arrays)
        self.assertEqual(output, [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150])
if __name__ == "__main__":
    unittest.main()