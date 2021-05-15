# find min edits between 2 substrings

def levenshteinDistance(str1, str2):
    edits =[[x for x in range(len(str1) + 1)]for y in range(len(str2) + 1)]
    print(edits)

    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    print(edits)
    
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1])

    return edits[-1][-1]



print(levenshteinDistance( "abc","yabd"))

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(levenshteinDistance("", ""), 0)

    def test_case_2(self):
        self.assertEqual(levenshteinDistance("", "abc"), 3)

    def test_case_3(self):
        self.assertEqual(levenshteinDistance("abc", "abc"), 0)

    def test_case_4(self):
        self.assertEqual(levenshteinDistance("abc", "abx"), 1)

    def test_case_5(self):
        self.assertEqual(levenshteinDistance("abc", "abcx"), 1)

    def test_case_6(self):
        self.assertEqual(levenshteinDistance("abc", "yabcx"), 2)

    def test_case_7(self):
        self.assertEqual(levenshteinDistance("algoexpert", "algozexpert"), 1)

    def test_case_8(self):
        self.assertEqual(levenshteinDistance("abcdefghij", "1234567890"), 10)

    def test_case_9(self):
        self.assertEqual(levenshteinDistance("abcdefghij", "a234567890"), 9)

    def test_case_10(self):
        self.assertEqual(levenshteinDistance("biting", "mitten"), 4)

    def test_case_11(self):
        self.assertEqual(levenshteinDistance("cereal", "saturday"), 6)

    def test_case_12(self):
        self.assertEqual(levenshteinDistance("cereal", "saturdzz"), 7)

    def test_case_13(self):
        self.assertEqual(levenshteinDistance("abbbbbbbbb", "bbbbbbbbba"), 2)

    def test_case_14(self):
        self.assertEqual(levenshteinDistance("abc", "yabd"), 2)

    def test_case_15(self):
        self.assertEqual(levenshteinDistance("xabc", "abcx"), 2)



if __name__ == "__main__":
    unittest.main()