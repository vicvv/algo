# function returns the minimum number or cuts needed to perform in order to make a palindrom
# from the input string.

#O(n^3) time | O(n^2) space
def palindromePartitioningMinCuts(string):
   
    palindroms = [[False for i in string] for j in string]
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            palindroms[i][j] = isPalindrom(string[i:j+1])
    cuts = [float('inf') for i in string]

    for i in range(len(string)):
        if palindroms[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] +1
            for j in range(1, i):
                if palindroms[j][i] and cuts[j-1] +1 < cuts[i]:
                    cuts[i] = cuts[j-1] +1
    return cuts[-1]


def isPalindrom(string):
    left = 0
    right = len(string) -1

    while left < right:
        if string[left] != string[right]:
            return False
        left +=1
        right -=1
    return True

import unittest




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(palindromePartitioningMinCuts("noonabbad"), 2)

if __name__ == "__main__":
    unittest.main()
