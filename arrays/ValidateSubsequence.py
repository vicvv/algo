
# O(n) time and O(1) space

'''
given two non-empty arrays of integers, write a function
that determines whether the second array is subsequence of first"
'''

# def isValidSubsequence(array, sequence):
#     arrIdx = 0
#     seqIdx = 0
#     while arrIdx < len(array) and seqIdx < len(sequence):
#         if array[arrIdx] == sequence[seqIdx]:
#             seqIdx += 1
#         arrIdx +=1
#     return seqIdx == len(sequence)


# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if value == sequence[seqIdx]:
            seqIdx +=1
    return seqIdx == len(sequence)


import unittest
class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10]), True)
    def test2(self):
        self.assertEqual(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, -1, -6, 10]), False)

if __name__ == "__main__":
    unittest.main()


