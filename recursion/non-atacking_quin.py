'''Write a function that takes in a positive integer n and returns the number of nonattacking placements of n queens on an n x n chessboard.
A non-attacking placement is one where no queen can attack another queen in a single
turn. In other words, it's a placement where no queen can move to the same position as
another queen in a single turn.
In chess, queens can move any number of squares horizontally, vertically, or diagonally in a
single turn.
+--+--+--+--+
| |Q | | |
+--+--+--+--+
| | | |Q |
+--+--+--+--+
|Q | | | |
+--+--+--+--+
| | |Q | |
+--+--+--+--+
The chessboard above is an example of a non-attacking placement of 4 queens on a 4x4
chessboard. For reference, there are only 2 non-attacking placements of 4 queens on a 4x4
chessboard.'''

# Lower Bound: O(n!) time | O(n) space - where n is the input number
def nonAttackingQueens(n):
    # Each index of `columnPlacements` represents a row of the chessboard,
    # and the value at each index is the column (on the relevant row) where
    # a queen is currently placed.
    columnPlacements = [0] * n
    return getNumberOfNonAttackingQueenPlacements(0, columnPlacements, n)

def getNumberOfNonAttackingQueenPlacements(row, columnPlacements, boardSize):
    if row == boardSize:
        return 1
    validPlacements = 0
    for col in range(boardSize):
        if isNonAttackingPlacement(row, col, columnPlacements):
            columnPlacements[row] = col
            validPlacements += getNumberOfNonAttackingQueenPlacements(row + 1, columnPlacements, boardSize)
    return validPlacements
# As 'row' tends to 'n', this becomes an O(n)-time operation.
def isNonAttackingPlacement(row, col, columnPlacements):
    for previousRow in range(row):
        columnToCheck = columnPlacements[previousRow]
        sameColumn = columnToCheck == col
        onDiagonal = abs(columnToCheck - col) == row - previousRow
        if sameColumn or onDiagonal:
            return False
    return True

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = 4
        expected = 2
        actual = nonAttackingQueens(input)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()