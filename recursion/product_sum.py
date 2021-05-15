'''
the product sum of [x,y] is x+y
the product sum of [x,[y,z]] is x + 2y +2z
'''


def productSum(array, multipl = 1):
    mys = 0
    for num in array:  
        print(num)      
        if type(num) == list:
            mys += (productSum(num, multipl + 1))
            #print("mys = ",mys)
        else:       
            mys += num
            #print("mys", mys)
    return mys * multipl

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print("ans", productSum(array))


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [1, 2, 3, 4, 5]
        self.assertEqual(productSum(test), 15)

    def test_case_2(self):
        test = [1, 2, [3], 4, 5]
        self.assertEqual(productSum(test), 18)

    def test_case_3(self):
        test = [[1, 2], 3, [4, 5]]
        self.assertEqual(productSum(test), 27)

    def test_case_4(self):
        test = [[[[[5]]]]]
        self.assertEqual(productSum(test), 600)

    def test_case_5(self):
        test = [
            9,
            [2, -3, 4],
            1,
            [1, 1, [1, 1, 1]],
            [[[[3, 4, 1]]], 8],
            [1, 2, 3, 4, 5, [6, 7], -7],
            [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7],
            [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]],
            -3,
        ]
        self.assertEqual(productSum(test), 1351)

    def test_case_6(self):
        test = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        self.assertEqual(productSum(test), 12)

# if __name__ == "__main__":
#     unittest.main()
