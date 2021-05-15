

'''the function takes in an array on integer and returns an array of len 2
representing the smallest and the largest num in the largest range on number

'''


# O(n) time | O(n) space
def largestRange(array):
    myh = {x:True for x in array}
    myrange= []
    longetLen = 0

    for num in array:
        if not num in myh:
            continue
        myh[num] = False
        curlen = 1
        left = num - 1
        right = num + 1
        while left in myh:
            myh[left] = False
            curlen +=1
            left -= 1
        while right in myh:
            myh[right] = False
            curlen += 1
            right +=1

        if longetLen < curlen:
            longetLen = curlen
            myrange = [left + 1, right - 1]
    return myrange
        

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array))



import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(largestRange([1]), [1, 1])

    def test_case_2(self):
        self.assertEqual(largestRange([1, 2]), [1, 2])

    def test_case_3(self):
        self.assertEqual(largestRange([4, 2, 1, 3]), [1, 4])

    def test_case_4(self):
        self.assertEqual(largestRange([4, 2, 1, 3, 6]), [1, 4])

    def test_case_5(self):
        self.assertEqual(largestRange([8, 4, 2, 10, 3, 6, 7, 9, 1]), [6, 10])

    def test_case_6(self):
        self.assertEqual(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])

    def test_case_7(self):
        self.assertEqual(
            largestRange([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]),
            [10, 19],
        )

    def test_case_8(self):
        self.assertEqual(
            largestRange(
                [0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]
            ),
            [-1, 19],
        )

    def test_case_9(self):
        self.assertEqual(
            largestRange(
                [
                    0,
                    -5,
                    9,
                    19,
                    -1,
                    18,
                    17,
                    2,
                    -4,
                    -3,
                    10,
                    3,
                    12,
                    5,
                    16,
                    4,
                    11,
                    7,
                    -6,
                    -7,
                    6,
                    15,
                    12,
                    12,
                    2,
                    1,
                    6,
                    13,
                    14,
                    -2,
                ]
            ),
            [-7, 7],
        )

    def test_case_10(self):
        self.assertEqual(
            largestRange(
                [
                    0,
                    -5,
                    9,
                    19,
                    -1,
                    18,
                    17,
                    2,
                    -4,
                    -3,
                    10,
                    3,
                    12,
                    5,
                    16,
                    4,
                    11,
                    7,
                    -6,
                    -7,
                    6,
                    15,
                    12,
                    12,
                    2,
                    1,
                    6,
                    13,
                    14,
                    -2,
                ]
            ),
            [-7, 7],
        )

    def test_case_11(self):
        self.assertEqual(
            largestRange(
                [
                    -7,
                    -7,
                    -7,
                    -7,
                    8,
                    -8,
                    0,
                    9,
                    19,
                    -1,
                    -3,
                    18,
                    17,
                    2,
                    10,
                    3,
                    12,
                    5,
                    16,
                    4,
                    11,
                    -6,
                    8,
                    7,
                    6,
                    15,
                    12,
                    12,
                    -5,
                    2,
                    1,
                    6,
                    13,
                    14,
                    -4,
                    -2,
                ]
            ),
            [-8, 19],
        )

if __name__ =="__main__":
    unittest.main()
