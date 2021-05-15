

def numbersInPi(pi, numbers):
    numbersTable = {number:True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return minSpaces if minSpaces != float('inf') else -1

def getMinSpaces(pi,ntable,cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    
    minSpaces = float('inf')
    
    for i in range(idx, len(pi)):
        prefix = pi[idx:1+i]
        if prefix in ntable:
            minSpacesInSuffix = getMinSpaces(pi,ntable, cache, i+1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return minSpaces


import unittest


PI = "3141592653589793238462643383279"


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
        self.assertEqual(numbersInPi(PI, numbers), 2)
       


if __name__ == "__main__":
    unittest.main()