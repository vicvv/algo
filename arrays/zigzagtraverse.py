


def zigzagTraverse(array):
    h = len(array) - 1
    w = len(array[0]) - 1
    col = 0
    row = 0
    result = []
    goingDown = True

    while not isOutOfBounds(col, row, h, w):
        result.append(array[row][col])
        if goingDown:
            if col == 0 or row == h:
                goingDown = False
                if row == h:
                    # we are on the last row and we go right
                    col +=1
                else:
                    # we go down
                    row +=1
            else:
                # goin down
                row += 1
                col -= 1
        else:
            if row == 0 or col == w:
                goingDown = True
                if col == w:
                    # we are on the last column and we go one row down
                    row +=1
                else:
                    # we are moving right
                    col +=1
            else:
                # going up
                row -= 1
                col += 1
    return result


def isOutOfBounds(col, row, h, w):
    return row < 0 or row > h or col < 0  or col > w


array = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
print(zigzagTraverse(array))


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [[1]]
        self.assertEqual(zigzagTraverse(test), [1])

    def test_case_2(self):
        test = [[1, 2, 3, 4, 5]]
        self.assertEqual(zigzagTraverse(test), [1, 2, 3, 4, 5])

    def test_case_3(self):
        test = [[1], [2], [3], [4], [5]]
        self.assertEqual(zigzagTraverse(test), [1, 2, 3, 4, 5])

    def test_case_4(self):
        test = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 10]]
        self.assertEqual(zigzagTraverse(test), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_case_5(self):
        test = [[1, 3, 4, 7, 8], [2, 5, 6, 9, 10]]
        self.assertEqual(zigzagTraverse(test), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_case_6(self):
        test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
        self.assertEqual(zigzagTraverse(test), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_case_7(self):
        test = [[1, 3, 4, 10, 11], [2, 5, 9, 12, 19], [6, 8, 13, 18, 20], [7, 14, 17, 21, 24], [15, 16, 22, 23, 25]]
        self.assertEqual(
            zigzagTraverse(test),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
        )

    def test_case_8(self):
        test = [
            [1, 3, 4, 10, 11, 20],
            [2, 5, 9, 12, 19, 21],
            [6, 8, 13, 18, 22, 27],
            [7, 14, 17, 23, 26, 28],
            [15, 16, 24, 25, 29, 30],
        ]
        self.assertEqual(
            zigzagTraverse(test),
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
            ],
        )

    def test_case_9(self):
        test = [
            [1, 3, 4, 10, 11],
            [2, 5, 9, 12, 20],
            [6, 8, 13, 19, 21],
            [7, 14, 18, 22, 27],
            [15, 17, 23, 26, 28],
            [16, 24, 25, 29, 30],
        ]
        self.assertEqual(
            zigzagTraverse(test),
            [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
            ],
        )

if __name__ == "__main__":
    unittest.main()