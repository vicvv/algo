# find min edits between 2 substrings

def levenshteinDistance(str1, str2):
    small = str1 if len(str1) <len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2

    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) +1)]

    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:   
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i
        for j in range(1,len(small) + 1 ):
            #print(big[i - 1],small[j - 1])
            if big[i - 1] == small[j - 1]:
                currentEdits[j] = previousEdits[j - 1]
                
            else:
                currentEdits[j] = 1 + min( currentEdits[j-1], previousEdits[j], previousEdits[j - 1])
    return evenEdits[-1] if len(big)%2 == 0 else oddEdits[-1]


print(levenshteinDistance( "abc","abc"))
# answer 2
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