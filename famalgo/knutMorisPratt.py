# O(n+m) time | O(m) space

def knuthMorrisPrattAlgorithm(string, substring):
  pattern = findPattern(substring)  
  return kmpHelper(string, substring, pattern)



def findPattern(substring):
    pattern = [ -1 for i in range(len(substring))]
    left = 0
    right = 1

    while right < len(substring) - 1:
        if substring[left] == substring[right]:
            pattern[right] = left
            right +=1
            left += 1
        elif left > 0:
            left = pattern[left - 1] + 1
        else:
            right += 1
            
    return pattern



def kmpHelper(string, substring, pattern):

    strIdx = 0
    subStrIdx = 0

    while strIdx + len(substring) - subStrIdx <= len(string):
        if string[strIdx] == substring[subStrIdx]:
            if subStrIdx == len(substring) - 1:
                return True
            subStrIdx +=1
            strIdx +=1

        elif subStrIdx > 0:
            subStrIdx = pattern[subStrIdx - 1] + 1
        else:
            strIdx += 1
    return False


string ='testwafwafawfawfawfawfawfawfawfa'
substring ='fawfawfawfawfa'
print(knuthMorrisPrattAlgorithm(string, substring))


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(knuthMorrisPrattAlgorithm("testwafwafawfawfawfawfawfawfawfa", "fawfawfawfawfa"), True)

    def test_case_2(self):
        self.assertEqual(
            knuthMorrisPrattAlgorithm("tesseatesgawatewtesaffawgfawtteafawtesftawfawfawfwfawftest", "test"),
            True,
        )

    def test_case_3(self):
        self.assertEqual(knuthMorrisPrattAlgorithm("aaabaabacdedfaabaabaaa", "aabaabaaa"), True)

    def test_case_4(self):
        self.assertEqual(knuthMorrisPrattAlgorithm("abxabcabcaby", "abcaby"), True)

    def test_case_5(self):
        self.assertEqual(knuthMorrisPrattAlgorithm("decadaafcdf", "daf"), False)

    def test_case_6(self):
        self.assertEqual(knuthMorrisPrattAlgorithm("aefoaefcdaefcdaed", "aefcdaed"), True)

    def test_case_7(self):
        self.assertEqual(knuthMorrisPrattAlgorithm("aefoaefcdaefcdaed", "aefcaefaeiaefcd"), False)

    def test_case_8(self):
        self.assertEqual(knuthMorrisPrattAlgorithm("aefcdfaecdaefaefcdaefeaefcdcdeae", "aefcdaefeaefcd"), True)

    def test_case_9(self):
        self.assertEqual(knuthMorrisPrattAlgorithm("bccbefbcdabbbcabfdcfe", "abc"), False)

    def test_case_10(self):
        self.assertEqual(knuthMorrisPrattAlgorithm("adafccfefbbbfeeccbcfd", "ecb"), False)

    def test_case_11(self):
        self.assertEqual(
            knuthMorrisPrattAlgorithm("testwherethefullstringmatches", "testwherethefullstringmatches"), True
        )
if __name__ == "__main__":
    unittest.main()