#O(nm*min(n,m)) time | O(nm*min(n,m)) space

def longestCommonSubsequence(str1, str2):
    lcs = [[[]for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1,len(str2) + 1):
        for j in range(1,len(str1) + 1):
            if str2[i - 1] == str1[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + [str2[i-1]]
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j -1], key = len)
    return lcs[-1][-1]



import unittest
class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(longestCommonSubsequence("ZXVVYZW","XKYKZPW"),['X', 'Y', 'Z', 'W'])
    def test10(self):
        self.assertEqual(longestCommonSubsequence("ABCDEFGHIJKLMNOPQRSTUVWXYZ","CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAGTUV"),['C', 'D', 'E', 'G', 'H', 'J', 'K', 'L', 'T', 'U', 'V'])
    def test3(self):
        self.assertEqual(longestCommonSubsequence("aab","baa"),['a', 'a'])
if __name__ == "__main__":
    unittest.main()