# write a function that will take 3 strings and try to find out if first string can be
# made of second + thirid

# O(nm) timne | O(nm) space

def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    cache = [[None for j in range(len(two) + 1)] for i in range(len(one)+ 1)]
    return intHelper(one, two, three, 0,0, cache)

def intHelper(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]
    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = intHelper(one, two, three, i + 1, j, cache)
        if 	cache[i][j]:
            return True
        
    if j < len(two) and two[j] == three[k]:
        cache[i][j] =  intHelper(one, two, three, i, j+1, cache )
        return cache[i][j]

    cache[i][j] = False
    return False


import unittest
class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjob"), True)

    def test2(self):
        self.assertEqual(interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjoe"), False)


if __name__ == "__main__":
    unittest.main()