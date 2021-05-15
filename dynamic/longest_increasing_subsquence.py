

import unittest

def longestIncreasingSubsequence(array):
    sequences = [None for x in array]
    indices = [None for x in range(len(array) + 1)]
    length = 0
    for i, num in enumerate(array):
        newlength = binarySearch(1, length, indices, array,num)
        sequences[i] = indices[newlength -1]
        indices[newlength] = i
        length = max(length, newlength)
    return buildSequence(array,sequences, indices[length])
        
		
def binarySearch(start, end, indices, array,num):
    if start > end:
        return start
    mid = (start + end)//2
    if array[indices[mid]] < num:
        start = mid + 1
    else:
        end = mid - 1
    return binarySearch(start, end, indices, array,num)
		
		

def buildSequence(array,sequences, currIndex):
    seq =[]
    while currIndex is not None:
        seq.append(array[currIndex])
        currIndex = sequences[currIndex]
    return list(reversed(seq))

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            longestIncreasingSubsequence([5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]), [-24, 2, 3, 5, 6, 35]
        )
if __name__ == "__main__":
    unittest.main()