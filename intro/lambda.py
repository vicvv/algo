

add_values = lambda x,y,z: x+y+z
max_length = lambda s1,s2 : max(len(s1), len(s2))
create_set = lambda l1, l2 : set(l1 + l2)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


new_list = map(str, filter(lambda x : x%2 ==0, map(lambda x: x**2, lst)))
print('\n'.join(list(new_list)))


print(add_values(1, 2, 3))
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        result = add_values(1, 2, 3)
        self.assertEquals(6, result)

    def test_case_2(self):
        result = add_values(2, 4, 3)
        self.assertEquals(9, result)

    def test_case_3(self):
        result = add_values(2, 0, 0)
        self.assertEquals(2, result)

    def test_case_4(self):
        result = add_values(-2, -4, 2)
        self.assertEquals(-4, result)

    def test_case_5(self):
        result = add_values(1.5, 2.3, 8.1)
        self.assertAlmostEqual(11.9, result)

    def test_case_6(self):
        result = max_length("", "")
        self.assertEqual(0, result)

    def test_case_7(self):
        result = max_length("hello", "tim")
        self.assertEqual(5, result)

    def test_case_8(self):
        result = max_length("no", "yes")
        self.assertEqual(3, result)

    def test_case_9(self):
        result = max_length("         ", "testing")
        self.assertEqual(9, result)

    def test_case_10(self):
        result = create_set([1, 2, 3], [2, 3])
        self.assertEqual(set([1, 2, 3]), result)

    def test_case_11(self):
        result = create_set([], [])
        self.assertEqual(set([]), result)

    def test_case_12(self):
        result = create_set([], [2, 3])
        self.assertEqual(set([2, 3]), result)

    def test_case_13(self):
        result = create_set([1, 2, 3, 4], [4, 5, 6])
        self.assertEqual(set([1, 2, 3, 4, 5, 6]), result)