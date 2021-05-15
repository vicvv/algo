
# iterative solution
# def squareOfZeroes(matrix):
#     n = len(matrix)
#     for topRow in range(n):
#         for leftCol in range(n):
#             squareLen = 2
#             while squareLen <= n - leftCol and squareLen <= n - topRow:
#                 bottonRow = topRow + squareLen - 1
#                 rightCol = leftCol + squareLen - 1
#                 if isSquareOfZeros(matrix, topRow, leftCol, bottonRow, rightCol):
#                     return True
#                 squareLen += 1
#    return False


# recursive solution with cache
def squareOfZeroes(matrix):
    lastIndex = len(matrix) - 1
    return hasSquareOfZeroes(matrix, 0,0, lastIndex, lastIndex,{})

def hasSquareOfZeroes(matrix, r1,c1, r2, c2,cache):
	if r1 >= r2 or c1 >= c2:
		return False
	key = str(r1) + "-" + str(c1) + "-" + str(r2) + "-" + str(c2)
	
	if key in cache:
		return cache[key]
	cache[key] = (
		isSquareOfZeros(matrix,r1,c1, r2, c2)
		or hasSquareOfZeroes(matrix,r1 + 1,c1 + 1, r2 -1, c2 -1,cache)
		or hasSquareOfZeroes(matrix,r1,c1 +1, r2-1, c2,cache)
		or hasSquareOfZeroes(matrix,r1 +1,c1, r2, c2-1,cache)
		or hasSquareOfZeroes(matrix,r1 +1,c1+1, r2, c2,cache)
		or hasSquareOfZeroes(matrix,r1,c1, r2 - 1, c2 -1 ,cache)
	)
	return cache[key]

def isSquareOfZeros(matrix, r1, c1, r2, c2):
    for row in range(r1, r2+1):
        if matrix[row][c1] != 0 or matrix[row][c2] != 0:
            return False
    for col in range(c1, c2+1):
        if matrix[r1][col] != 0 or matrix[r2][col] != 0:
            return False
    return True
		

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