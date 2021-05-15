def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
	kvalues = [[0 for x in range(0,capacity + 1)] for y in range(len(items) +1)]
	for i in range(1,len(items) +1):
		curW = items[i - 1][1]
		curValue = items[i - 1][0]
		for c in range(0, capacity + 1):
			if curW > c:
				kvalues[i][c] = kvalues[i-1][c]
			else:
				kvalues[i][c] = max(
					kvalues[i-1][c], kvalues[i-1][c-curW] + curValue)
	return [kvalues[-1][-1], getkItems(kvalues,items)]	
	
def getkItems(kvalues,items):
    seq = []
    i = len(kvalues) - 1
    c = len(kvalues[0]) - 1

    while i >0:
        if kvalues[i][c] == kvalues[i-1][c]:
            i -=1
        else:
            seq.append(i - 1)			
            c -= items[i-1][1]
            i -=1
        if c == 0:
            break
    return list(reversed(seq))
        

import unittest

class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]],10), [10,[1,3]])

if __name__ == "__main__":
    unittest.main()