
def new_range(x,y,z):
    for i in range(x,y,z):
        yield i


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        iter = new_range(1, 5, 1)

    def test_case_2(self):
        iter = new_range(1, 5, 1)
        self.assertEqual([1, 2, 3, 4], list(iter))

    def test_case_3(self):
        iter = new_range(1, 1000000, 1)
        iter.__iter__()
        item = iter.__next__()
        self.assertEqual(1, item)

    def test_case_4(self):
        iter = new_range(1, 10, 2)
        self.assertEqual([1, 3, 5, 7, 9], list(iter))

    def test_case_5(self):
        iter = new_range(0, 21, 5)
        lst = []
        for i in iter:
            lst.append(i)
        expected = [0, 5, 10, 15, 20]
        self.assertEqual(expected, lst)

    def test_case_6(self):
        iter = range(-2, -5, -1)
        self.assertEqual([-2, -3, -4], list(iter))

    def test_case_7(self):
        iter = range(0, 5, -1)
        self.assertEqual([], list(iter))

    def test_case_8(self):
        iter = range(-2, -5, 1)
        self.assertEqual([], list(iter))

if __name__ == '__main__':
    unittest.main()