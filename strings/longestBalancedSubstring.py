# find the len of the longest balanced substring
# space|time O(n) | O(n)

def longestBalancedSubstring(string):
    maxLen =0
    arr =[-1]

    for i in range(len(string)):
        if string[i] =='(':
            arr.append(i)
        else:
            arr.pop()
            if len(arr) ==0:
                arr.append(i)
            else:
                curBalancedSubstrStartIndex = arr[-1]
                curLen = i -curBalancedSubstrStartIndex
                maxLen = max(maxLen, curLen)

    return maxLen


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "(()))("
        expected = 4
        actual = longestBalancedSubstring(string)
        self.assertEqual(actual, expected)

if __name__ =='__main__':
    unittest.main()