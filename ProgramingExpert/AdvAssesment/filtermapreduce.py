import unittest

#positive_even_squares=lambda *args: [j**2 for i in args for j in i if j%2 == 0 and j>0]

def positive_even_squares(*args):
    positive_even_nums = []

    for lst in args:
        print(lst)
        filtered_list = filter(lambda x: x > 0 and x % 2 == 0, lst)
        positive_even_nums.extend(filtered_list)

    squares = map(lambda x: x ** 2, positive_even_nums)
    return list(squares)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        args = [[-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10]]
        expected = [4, 16, 36, 100]
        result = positive_even_squares(*args)
        self.assertEqual(result, expected)

    def test_case_2(self):
        args = [[1], [2], [3], [4], [5]]
        expected = [4, 16]
        result = positive_even_squares(*args)
        self.assertEqual(result, expected)

    def test_case_3(self):
        args = []
        expected = []
        result = positive_even_squares(*args)
        self.assertEqual(result, expected)

    def test_case_4(self):
        args = [[], [], []]
        expected = []
        result = positive_even_squares(*args)
        self.assertEqual(result, expected)

    def test_case_5(self):
        args = [[], [12], []]
        expected = [144]
        result = positive_even_squares(*args)
        self.assertEqual(result, expected)

    def test_case_6(self):
        args = [[-1, 2, 4, 5], [1, 1, 1, 1, 2, 3], [4, 5], [1, 1], [-1, -4, -8, 0, 2], [2]]
        expected = [4, 16, 4, 16, 4, 4]
        result = positive_even_squares(*args)
        self.assertEqual(result, expected)

    def test_case_7(self):
        args = [[-1, -2, -3, -4], [1, 2, 3, 4], [-4, -4, -5, -6], [2, 4], [10, 10, 10]]
        expected = [4, 16, 4, 16, 100, 100, 100]
        result = positive_even_squares(*args)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()