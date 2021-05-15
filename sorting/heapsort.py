
# you begin with building max heap and then we reposition root value
# by sifting it down

def heapSort(array):
    buildMaxHeap(array)
    print("max heap:",array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)
    print("Sorted Array", array)
    return array

def buildMaxHeap(array):
	firstParentIdx = len(array) - 2 // 2
	for curentIdx in reversed(range(firstParentIdx + 1)):
		siftDown(curentIdx , len(array) - 1, array)
		
def siftDown(curentIdx , endIdx, heap):
	childOneIdx = curentIdx  * 2 + 1
	while childOneIdx <= endIdx:
		childTwoIdx = curentIdx  * 2 + 2 if curentIdx  * 2 + 2 <= endIdx else - 1
		if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
			idxToSwap = childTwoIdx
		else:
			idxToSwap = childOneIdx
		if heap[idxToSwap] > heap[curentIdx]:
			swap(curentIdx ,idxToSwap, heap)
			curentIdx  = idxToSwap
			childOneIdx = curentIdx  *2 + 1
		else:
			return
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(heapSort([1]), [1])
    def test_case_2(self):
        self.assertEqual(heapSort([8, 5, 2, 9, 5, 6, 3]),[2, 3, 5, 5, 6, 8, 9])

if __name__ == "__main__":
    unittest.main()