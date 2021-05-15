# function takes in an array and generates the greatest sum from strictly increasing subsequence
# and it includes the subsequence of nums that generate the max sum
# Time o(n2) | Space O(n)
def maxSumIncreasingSubsequence(array):
    sums = array[:]
    sequences = [None for i in array]
    maxSumIdx = 0
    for i in range(len(array)):
        curNum = array[i]
        for j in range(0,i):
            otherNum = array[j]
            if curNum > otherNum and sums[j] + curNum >= sums[i]:
                sums[i] = sums[j] + curNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildFinalSeq(array, sequences, maxSumIdx)]

def buildFinalSeq(array, sequences, curIdx):
    finalSeq = []

    while curIdx is not None:
        finalSeq.append(array[curIdx])
        curIdx = sequences[curIdx]

    return list(reversed(finalSeq))



import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSumIncreasingSubsequence([8,12,2,3,15,5,7]), [35, [8,12,15]])
    def test_case_2(self):
        self.assertEqual(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]), [110,[10,20,30,50]])

if __name__ == "__main__":
    unittest.main()