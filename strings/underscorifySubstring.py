'''function  returns every instance of the substring surraunded by underscore
If 2 instances of the substr overlap each other than the unserscore should be on far
left and far right'''


# st = 'testthis is a testtest to see if testtestest it works'
# sbs = 'test'
# result : '_test_this is a _testtest_ to see if _testesttest_ it works'

# O(n*m) time | O(n) space

def underscorifySubstring(string, substring):

    # first we loking for indexes of substring start and stop
    # second we looking of end index is equal of next start index and if so we collapse
    locations = collapse(getLocations(string,substring))

    # inserting underscores into original string using the location array
    return underscorify(string, locations)

def getLocations(string, substring):
    
    locations = []
    startIdx = 0

    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx = nextIdx + 1
        else:
            break
    return locations

def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    previous = newLocations[0]

    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= previous[1]:
            previous[1] = current[1]

        else:
            newLocations.append(current)
            previous = current
    return newLocations
    

def underscorify(string, locations):
    locationsIdx = 0
    stringIdx = 0
    inBetweenUnderscores = False
    finlaChars = []

    i = 0

    while stringIdx < len(string) and locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]:
            finlaChars.append("_")
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                locationsIdx += 1        
            i = 0 if i==1 else 1
        
        finlaChars.append(string[stringIdx])
        stringIdx += 1
        
    if locationsIdx < len(locations):
        finlaChars.append("_")
    elif stringIdx < len(string):
        finlaChars.append(string[stringIdx:])
    return ''.join(finlaChars)

# st = 'testthis is a testtest to see if testtestest it works'
# sbs = 'test'
#print(underscorifySubstring(st, sbs))

import unittest
class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            underscorifySubstring("this is a test to see if it works", "test"),
            "this is a _test_ to see if it works",
        )

    def test_case_2(self):
        self.assertEqual(
            underscorifySubstring("test this is a test to see if it works", "test"),
            "_test_ this is a _test_ to see if it works",
        )

    def test_case_3(self):
        self.assertEqual(
            underscorifySubstring("testthis is a test to see if it works", "test"),
            "_test_this is a _test_ to see if it works",
        )

    def test_case_4(self):
        self.assertEqual(
           underscorifySubstring("testthis is a testest to see if testestes it works", "test"),
            "_test_this is a _testest_ to see if _testest_es it works",
        )

    def test_case_5(self):
        self.assertEqual(
           underscorifySubstring("testthis is a testtest to see if testestest it works", "test"),
            "_test_this is a _testtest_ to see if _testestest_ it works",
        )

    def test_case_6(self):
        self.assertEqual(
           underscorifySubstring("this is a test to see if it works and test", "test"),
            "this is a _test_ to see if it works and _test_",
        )

    def test_case_7(self):
        self.assertEqual(
           underscorifySubstring("this is a test to see if it works and test", "bfjawkfja"),
            "this is a test to see if it works and test",
        )

    def test_case_8(self):
        self.assertEqual(
           underscorifySubstring("ttttttttttttttbtttttctatawtatttttastvb", "ttt"),
            "_tttttttttttttt_b_ttttt_ctatawta_ttttt_astvb",
        )

    def test_case_9(self):
        self.assertEqual(underscorifySubstring("tzttztttz", "ttt"), "tzttz_ttt_z")

    def test_case_10(self):
        self.assertEqual(
           underscorifySubstring("abababababababababababababaababaaabbababaa", "a"),
            "_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_aa_b_a_b_aaa_bb_a_b_a_b_aa_",
        )

    def test_case_11(self):
        self.assertEqual(
           underscorifySubstring("abcabcabcabcabcabcabcabcabcabcabcabcabcabc", "abc"),
            "_abcabcabcabcabcabcabcabcabcabcabcabcabcabc_",
        )
if __name__ == "__main__":
    unittest.main()