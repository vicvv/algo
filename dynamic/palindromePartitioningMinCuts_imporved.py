# function returns the minimum number or cuts needed to perform in order to make a palindrom
# from the input string.

def palindromePartitioningMinCuts(string):
    palindroms = [[False for i in string] for j in string]

    for i in range(len(string)):
        palindroms[i][i] = True

    for length in range(2, len(string) + 1):  
        for i in range(0, len(string) - length + 1):
            j = i + length - 1
            if length == 2:
                palindroms[i][j] = string[i] == string[j]
            else:
                palindroms[i][j] = string[i] == string[j] and palindroms[i+1][j-1]

    
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

   


import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(palindromePartitioningMinCuts("noonabbad"), 2)

if __name__ == "__main__":
    unittest.main()
