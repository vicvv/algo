# O(2^(n+m)) time | O(n+m) space
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    return intHelper(one, two, three, 0,0)

def intHelper(one, two, three, i, j):
	k = i + j
	if k == len(three):
		return True
	if i < len(one) and one[i] == three[k]:
		if intHelper(one, two, three, i + 1, j):
			return True
		
	if j < len(two) and two[j] == three[k]:
		return intHelper(one, two, three, i, j+1 )
	
	return False

import unittest
class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjob"), True)

    def test2(self):
        self.assertEqual(interweavingStrings("algoexpert", "your-dream-job", "your-algodream-expertjoe"), False)


if __name__ == "__main__":
    unittest.main()