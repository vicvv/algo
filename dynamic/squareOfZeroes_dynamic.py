def squareOfZeroes(matrix):
    infoMatrix = preComputeNumOfZeroes(matrix)
    lastIndex = len(matrix) - 1
    return hasSquareOfZeroes(infoMatrix, 0, 0,lastIndex, lastIndex, {})

def hasSquareOfZeroes(infoMatrix, r1,c1, r2, c2,cache):
	if r1 >= r2 or c1 >= c2:
		return False
	key = str(r1) + "-" + str(c1) + "-" + str(r2) + "-" + str(c2)
	
	if key in cache:
		return cache[key]
	cache[key] = (
		isSquareOfZeroes(infoMatrix,r1,c1, r2, c2)
		or hasSquareOfZeroes(infoMatrix,r1 + 1,c1 + 1, r2 -1, c2 -1,cache)
		or hasSquareOfZeroes(infoMatrix,r1,c1 +1, r2-1, c2,cache)
		or hasSquareOfZeroes(infoMatrix,r1 +1,c1, r2, c2-1,cache)
		or hasSquareOfZeroes(infoMatrix,r1 +1,c1+1, r2, c2,cache)
		or hasSquareOfZeroes(infoMatrix,r1,c1, r2 - 1, c2 -1 ,cache)
	)
	return cache[key]
	
def isSquareOfZeroes(infoMatrix, r1, c1, r2, c2):
    squareLength = c2 - c1 + 1
    hasTopBorder = infoMatrix[r1][c1]['numZeroesRight'] >= squareLength
    hasLeftBorder = infoMatrix[r1][c1]['numZeroesBelow'] >= squareLength
    hasBottomBorder = infoMatrix[r2][c1]['numZeroesRight'] >= squareLength
    hasRightBorder = infoMatrix[r1][c2]['numZeroesBelow'] >= squareLength
    return hasTopBorder and hasLeftBorder and hasBottomBorder and hasRightBorder

def preComputeNumOfZeroes(matrix):
    infoMatrix = [[x for x in row] for row in matrix]

    n = len(matrix)
    lastIndex = n - 1

    for row in range(n):
        for col in range(n):
            numZeroes = 1 if matrix[row][col] == 0  else 0
            infoMatrix[row][col] = {
                'numZeroesBelow': numZeroes,
                'numZeroesRight': numZeroes,
            }
    for row in reversed(range(n)):
        for col in reversed(range(n)):
            if matrix[row][col] == 1:
                continue
            if row < lastIndex:
                infoMatrix[row][col]['numZeroesBelow'] += infoMatrix[row + 1][col]['numZeroesBelow']
            if col < lastIndex:
                infoMatrix[row][col]['numZeroesRight'] += infoMatrix[row][col+1]['numZeroesRight']
    return infoMatrix
        

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 1],
        ]
        self.assertEqual(squareOfZeroes(matrix), True)

if __name__ == "__main__":
    unittest.main()