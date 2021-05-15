#O(nm) time | O(nm) space


def longestCommonSubsequence(str1, str2):
    #lcs = [[[None, 0, None, None] for x in range(len(str1) +1)] for y in range(len(str2) + 1)]
    lcs = [[[None, 0, None, None] for x in range(len(str1) +1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) +1):
            if str2[i-1] == str1[j-1]:
                #lcs[i][j] = [str2[i-1], lcs[i-1][j-1][1], i-1, j-1]
                lcs[i][j] = [str2[i-1], lcs[i-1][j-1][1] + 1 , i-1, j-1 ]
            else:
                if lcs[i - 1][j][1] > lcs[i][j-1][1]:
                    lcs[i][j] = [None, lcs[i-1][j][1], i-1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j-1][1], i, j-1 ]
    return buildSequence(lcs)

def buildSequence(lcs):
    print(lcs)
    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1

    while i!=0 and j!=0:
        currentVal = lcs[i][j]
        if currentVal[0] is not None:
            sequence.append(currentVal[0])
        i = currentVal[2]
        j = currentVal[3]

    return list(reversed(sequence))
    

import unittest
class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(longestCommonSubsequence("ZXVVYZW","XKYKZPW"),['X', 'Y', 'Z', 'W'])
    def test10(self):
        self.assertEqual(longestCommonSubsequence("ABCDEFGHIJKLMNOPQRSTUVWXYZ","CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAGTUV"),['C', 'D', 'E', 'G', 'H', 'J', 'K', 'L', 'T', 'U', 'V'])
    def test3(self):
        self.assertEqual(longestCommonSubsequence("baa","aabcc"),['a', 'a'])
if __name__ == "__main__":
    unittest.main()