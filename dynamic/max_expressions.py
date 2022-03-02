'''Write a function that takes in an array of integers and returns the
largest possible value for the expression
array[a] - array[b] + array[c] - array[d] , where a ,
b , c , and d are indices of the array and a < b < c < d .
If the input array has fewer than 4 elements, your function should
return 0 .
Sample Input
array = [3, 6, 1, -3, 2, 7]
Sample Output
4
// Choose a = 1, b = 3, c = 4, and d = 5
// -> 6 - (-3) + 2 - 7 = 4
'''


# O(n^4) time | O(1) space - where n is the length of the array
def maximizeExpression(array):
    if len(array) < 4:
        return 0
    maximumValueFound = float("-inf")
    for a in range(len(array)):
        aValue = array[a]
        for b in range(a + 1, len(array)):
            bValue = array[b]
            for c in range(b + 1, len(array)):
                cValue = array[c]
                for d in range(c + 1, len(array)):
                    dValue = array[d]
                    expressionValue = evaluateExpression(aValue, bValue, cValue, dValue)
                    maximumValueFound = max(expressionValue, maximumValueFound)
    return maximumValueFound

def evaluateExpression(a, b, c, d):
    return a - b + c - d


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [3, 6, 1, -3, 2, 7]
        expected = 4
        actual = maximizeExpression(input)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()