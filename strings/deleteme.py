def smallestSubstringContaining(bigString, smallString):
    targetCharCounts = getCharsCount(smallString)
    sbstrBounds = getSubstringFromBounds(bigString,targetCharCounts)
    return getStringFromBounds(bigString,sbstrBounds)

def getCharsCount(string):
    charCounts = {}
    for char in string:
        increaseCharCount(char, charCounts)
    return charCounts

def getSubstringFromBounds(string, targetCharCounts):
    substBound = [0, float('inf')]
    substringCharCounts = {}
    numUniqueChars = len(targetCharCounts.keys())
    uniquCharCount = 0
    left = 0
    right = 0

    while right < len(string):
        rightChar = string[right]
        if rightChar not in targetCharCounts:
            right +=1
            continue
        increaseCharCount(rightChar, substringCharCounts)
        if substringCharCounts[rightChar] == targetCharCounts[rightChar]:            
            uniquCharCount += 1

        while uniquCharCount == numUniqueChars and left <= right:
            substBound = getCloserBounts(left, right, substBound[0], substBound[1])
            leftChar = string[left]
            if leftChar not in targetCharCounts:
                left +=1
                continue
            if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
                uniquCharCount -= 1
            decrCharCount(leftChar, substringCharCounts)
            left += 1   
        right += 1

    return substBound


def decrCharCount(char, hash):
    hash[char] =-1


def getCloserBounts(ind1, ind2, ind3, ind4):
    return [ind1, ind2] if ind2-ind1  < ind4 - ind3 else [ind3, ind4]

def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1

def getStringFromBounds(string, bounds):
    start, end = bounds
    if end == float('inf'):
        return ''
    return string[start:end+1]


print(smallestSubstringContaining("abcd$ef$axb$c$","$$abf"))
# "f$axb$" but I have abcd$ef$
import unittest

class TestProgram(unittest.TestCase):
    # def test_case_1(self):
    #     bigString = "abcdef"
    #     smallString = "fa"
    #     expected = "abcdef"
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_2(self):
    #     bigString = "abcdef"
    #     smallString = "d"
    #     expected = "d"
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_3(self):
    #     bigString = "abcdefghijklmnopqrstuvwxyz"
    #     smallString = "aajjttwwxxzz"
    #     expected = ""
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_4(self):
    #     bigString = "abzacdwejxjftghiwjtklmnopqrstuvwxyz"
    #     smallString = "aajjttwwxxzz"
    #     expected = "abzacdwejxjftghiwjtklmnopqrstuvwxyz"
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_5(self):
    #     bigString = "abzacdwejxjfxztghiwjtklmnopqrstuvwxyz"
    #     smallString = "aajjttwwxxzz"
    #     expected = "abzacdwejxjfxztghiwjt"
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_6(self):
    #     bigString = "aaaa+a$+aaa++$+++++++aaa"
    #     smallString = "a+$aaAaaaa$++"
    #     expected = ""
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_7(self):
    #     bigString = "a$fuu+afff+affaffa+a$Affab+a+a+$a$"
    #     smallString = "a+$aaAaaaa$++"
    #     expected = "affa+a$Affab+a+a+$a"
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    def test_case_8(self):
        bigString = "a$fuu+afff+affaffa+a$Affab+a+a+$a$bccgtt+aaaaA+++aaa$"
        smallString = "a+$aaAaaaa$++"
        expected = "affa+a$Affab+a+a+$a"
        self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # # def test_case_9(self):
    # #     bigString = "145624356128828193236336541277356789901"
    # #     smallString = "123"
    # #     expected = "1932"
    # #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # # def test_case_10(self):
    # #     bigString = "1456243561288281932363365412356789901!"
    # #     smallString = "123!"
    # #     expected = "2356789901!"
    # #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_11(self):
    #     bigString = "14562435612!88281932363365$412356789901"
    #     smallString = "$123!"
    #     expected = "!88281932363365$"
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_12(self):
    #     bigString = "14562435612!88281932363365$412356789901"
    #     smallString = "#!123!"
    #     expected = ""
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_13(self):
    #     bigString = "14562435612!88281932363365$412356789901"
    #     smallString = "#!333333123!"
    #     expected = ""
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # def test_case_14(self):
    #     bigString = "14562435612z!8828!193236!336!5$41!23!5!6789901#"
    #     smallString = "#!2z"
    #     expected = "z!8828!193236!336!5$41!23!5!6789901#"
    #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # # def test_case_15(self):
    # #     bigString = "14562435612z!8828!193236!336!5$41!23!5!6789901#z2!"
    # #     smallString = "#!2z"
    # #     expected = "#z2!"
    # #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)

    # # def test_case_16(self):
    # #     bigString = "abcd$ef$axb$c$"
    # #     smallString = "$$abf"
    # #     expected = "f$axb$"
    # #     self.assertEqual(smallestSubstringContaining(bigString, smallString), expected)


# if __name__ == "__main__":
#     unittest.main()
