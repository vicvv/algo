
'''Write a ContinuousMedianHandler class that supports:
The continuous insertion of numbers with the insert method.
The instant (O(1) time) retrieval of the median of the numbers that have been inserted thus far with the
getMedian method.
The getMedian method has already been written for you. You simply have to write the insert method.
The median of a set of numbers is the "middle" number when the numbers are ordered from smallest to
greatest. If there's an odd number of numbers in the set, as in {1, 3, 7} , the median is the number in the
middle ( 3 in this case); if there's an even number of numbers in the set, as in {1, 3, 7, 8} , the median
is the average of the two middle numbers ( (3 + 7) / 2 == 5 in this case)
'''
# log(N) time | O(N) space

# class ContinuousMedianHandler:
#     def __init__(self):
#         self.lowers = Heap(MAX_HEAP_FUNCT,[])
#         self.greaters = Heap(MIN_HEAP_FUNCT,[])
#         self.median = None

#     def insert(self, number):
#         if not self.lowers.length or number < self.lowers.peek():
#             self.lowers.insert(number)
#         else:
#             self.greaters.insert(number)
#         self.rebalanceHeaps()
#         self.updateMedian()
		
#     def rebalanceHeaps(self):
#         if self.lowers.length - self.greaters.length == 2:
#             self.greaters.insert(self.lowers.remove())
#         elif self.greaters.length - self.lowers.length == 2:
#             self.lowers.insert(self.greaters.remove())
        
#     def updateMedian(self):
#         if self.lowers.length == self.greaters.length:
#             self.median = (self.lowers.peek() + self.greaters.peek()) / 2
#         elif self.lowers.length > self.greaters.length:
#             self.median = self.lowers.peek()
#         else:
#             self.median = self.greaters.peek()
                    

#     def getMedian(self):
#         return self.median
	

	
# class Heap:
#     def __init__(self, comparisonFunc, array):
#         self.heap = self.buildHeap(array)
#         self.comparisonFunc = comparisonFunc
#         self.length = len(self.heap)

#     def buildHeap(self,array):
#         firstParrentIndex = (len(array) - 2)//2
#         for currentIndex in reversed(range(firstParrentIndex + 1)):
#             self.siftDown(currentIndex, len(array) - 1, array)
#         return array
            
#     def siftDown(self, currentIndex, endIndex, heap):
#         childOneIndex = 2*currentIndex + 1
#         while childOneIndex <= endIndex:
#             childTwoIndex = 2*currentIndex + 2 if 2*currentIndex + 2 <= endIndex else -1
#             if childTwoIndex != 1:
#                 if self.comparisonFunc(heap[childTwoIndex], heap[childTwoIndex]):
#                     indexToSwap = childTwoIndex           
#                 else: 
#                     indexToSwap = childOneIndex
#             if self.comparisonFunc(heap[indexToSwap],heap[currentIndex]):
#                 self.swap(indexToSwap, currentIndex, heap)
#                 currentIndex = indexToSwap
#                 childOneIndex = 2*currentIndex + 1
#             else:
#                 return			
            
#     def siftUp(self, currentIndex, heap):
#         parrentIndex = (currentIndex - 1)//2
#         while currentIndex > 0 :
#             if self.comparisonFunc(heap[currentIndex], heap[parrentIndex]):
#                 self.swap(currentIndex, parrentIndex, heap)
#                 currentIndex = parrentIndex
#                 parrentIndex = (currentIndex -1)//2
#             else:
#                 return

#     def peek(self):
#         return self.heap[0]


#     def remove(self):
#         self.swap(0, len(self.heap) - 1, self.heap)
#         valueToRemove = self.heap.pop()
#         self.length -=1
#         self.siftDown(0, len(self.heap) - 1, self.heap)
#         return valueToRemove

#     def insert(self, value):
#         self.heap.append(value)
#         self.length += 1
#         self.siftUp(self.length - 1, self.heap)


#     def swap(self, i, j, heap):
#         heap[i], heap[j] = heap[j], heap[i]
		
# def MAX_HEAP_FUNCT(a,b):
# 	return a > b

# def MIN_HEAP_FUNCT(a,b):
# 	return a < b

class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = Heap(MIN_HEAP_FUNC, [])
        self.median = None

    # O(log(n)) time | O(n) space
    def insert(self, number):
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())

    def updateMedian(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def getMedian(self):
        return self.median

class Heap:
    def __init__(self, comparisonFunc, array):
        self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1:
                if self.comparisonFunc(heap[childTwoIdx], heap[childOneIdx]):
                    idxToSwap = childTwoIdx
                else:
                    idxToSwap = childOneIdx
            else:
                idxToSwap = childOneIdx
            if self.comparisonFunc(heap[idxToSwap], heap[currentIdx]):
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return


    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0:
            if self.comparisonFunc(heap[currentIdx], heap[parentIdx]):
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, self.length - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.length - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.length - 1, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

def MAX_HEAP_FUNC(a, b):
    return a > b
def MIN_HEAP_FUNC(a, b):
    return a < b





import unittest


test = ContinuousMedianHandler()


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test.insert(5)
        self.assertEqual(test.getMedian(), 5)
        test.insert(10)
        self.assertEqual(test.getMedian(), 7.5)

    def test_case_2(self):
        test.insert(100)
        self.assertEqual(test.getMedian(), 10)
        test.insert(200)
        self.assertEqual(test.getMedian(), 55)

    def test_case_3(self):
        test.insert(6)
        self.assertEqual(test.getMedian(), 10)
        test.insert(13)
        self.assertEqual(test.getMedian(), 11.5)

    def test_case_4(self):
        test.insert(14)
        self.assertEqual(test.getMedian(), 13)
        test.insert(50)
        self.assertEqual(test.getMedian(), 13.5)

    def test_case_5(self):
        test.insert(51)
        self.assertEqual(test.getMedian(), 14)
        test.insert(52)
        self.assertEqual(test.getMedian(), 32)

    def test_case_6(self):
        test.insert(1000)
        self.assertEqual(test.getMedian(), 50)
        test.insert(10000)
        self.assertEqual(test.getMedian(), 50.5)

    def test_case_7(self):
        test.insert(10001)
        self.assertEqual(test.getMedian(), 51)
        test.insert(10002)
        self.assertEqual(test.getMedian(), 51.5)

    def test_case_8(self):
        test.insert(10003)
        self.assertEqual(test.getMedian(), 52)
        test.insert(10004)
        self.assertEqual(test.getMedian(), 76)

    def test_case_9(self):
        test.insert(75)
        self.assertEqual(test.getMedian(), 75)
        test.insert(80)
        self.assertEqual(test.getMedian(), 77.5)
if __name__ == "__main__":
    unittest.main()

