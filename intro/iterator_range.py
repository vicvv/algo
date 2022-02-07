
# range iterator

import unittest

class Range:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current= self.start
        return self

    def __next__(self):
        if self.step > 0  and self.current >= self.end:
            raise StopIteration
        if self.step < 0  and self.current <= self.end:
            raise StopIteration
        
        #getting ready for the next iteration
        self.current += self.step
        # here we are accessing and returnting a current value
        return self.current -self.step
        


# iter = Range(1, 5, 1)
# print(iter.__next__)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        iter = Range(1, 5, 1)
        self.assertTrue(hasattr(iter, "__iter__"))

    def test_case_2(self):
        iter = Range(1, 5, 1)
        self.assertEqual([1, 2, 3, 4], list(iter))

    # def test_case_3(self):
    #     iter = Range(1, 1000000, 1)
    #     iter.__iter__()
    #     item = iter.__next__()
    #     self.assertEqual(1, item)

    # def test_case_4(self):
    #     iter = Range(1, 10, 2)
    #     self.assertEqual([1, 3, 5, 7, 9], list(iter))

    # def test_case_5(self):
    #     iter = Range(0, 21, 5)
    #     lst = []
    #     for i in iter:
    #         lst.append(i)
    #     expected = [0, 5, 10, 15, 20]
    #     self.assertEqual(expected, lst)

    # def test_case_6(self):
    #     iter = Range(-2, -5, -1)
    #     self.assertEqual([-2, -3, -4], list(iter))

    # def test_case_7(self):
    #     iter = Range(0, 5, -1)
    #     self.assertEqual([], list(iter))

    # def test_case_8(self):
    #     iter = Range(-2, -5, 1)
    #     self.assertEqual([], list(iter))


if __name__ == "__main__":
    unittest.main()