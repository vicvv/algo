import unittest
import math

class Vector:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return f'Vector {self.point1}, {self.point2}'
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        else:
            return self.point1 == other.point1 and self.point2 == other.point2

    def __add__(self, other):
        sumx = self.point1 + other.point1
        sumy = self.point2 + other.point2
        return Vector(sumx, sumy)

    def __sub__(self, other):
        sumx = self.point1 - other.point1
        sumy = self.point2 - other.point2
        return Vector(sumx, sumy)

    def __mul__(self,other):
        sumx = self.point1 * other.point1
        sumy = self.point2 * other.point2
        return sumx+sumy




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(hasattr(Vector, '__repr__'))
        self.assertNotEqual(repr(Vector(1, 2)), repr(Vector(2, 1)))
        self.assertNotEqual(repr(Vector(1, 2)), repr(Vector(1, 3)))
        self.assertEqual(repr(Vector(1, 2)), repr(Vector(1, 2)))

    def test_case_2(self):
        self.assertTrue(hasattr(Vector, '__eq__'))
        self.assertNotEqual(Vector(1, 2), Vector(2, 1))
        self.assertNotEqual(Vector(1, 2), Vector(1, 3))
        self.assertEqual(Vector(1, 2), Vector(1, 2))

    def test_case_3(self):
        self.assertTrue(hasattr(Vector, '__add__'))
        v1 = Vector(4, 5)
        v2 = Vector(1, 2)
        self.assertEqual(Vector(5, 7), (v1 + v2))

    def test_case_4(self):
        self.assertTrue(hasattr(Vector, '__sub__'))
        v1 = Vector(4, 5)
        v2 = Vector(1, 2)
        self.assertEqual(Vector(3, 3), (v1 - v2))

    def test_case_5(self):
        self.assertTrue(hasattr(Vector, '__mul__'))
        v1 = Vector(3, 4)
        v2 = Vector(2, 7)
        self.assertEqual(34, v1 * v2)


if __name__ == '__main__':
    unittest.main()