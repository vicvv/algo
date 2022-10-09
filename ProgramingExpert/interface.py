
'''
interface can not have its own methods. All method in interface must me impletented
in class that inherits the interface.
'''

import unittest
import math


class ShapeInterface:
    def get_area(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError()


# Write your code here.
class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length**2

    def get_perimeter(self):
        return 4*self.side_length


class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        #return math.pi*2*self.radius
        return math.pi * (self.radius**2)

    def get_perimeter(self):
        return math.pi*2*self.radius
        #return math.pi * (self.radius**2)




#from program import ShapeInterface, Square, Circle


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        shape = Square(4)
        self.assertEqual(16, shape.get_area())
        self.assertEqual(16, shape.get_perimeter())

    def test_case_2(self):
        shape = Square(3)
        self.assertEqual(9, shape.get_area())
        self.assertEqual(12, shape.get_perimeter())

    def test_case_3(self):
        shape = Square(1)
        self.assertEqual(1, shape.get_area())
        self.assertEqual(4, shape.get_perimeter())

    def test_case_4(self):
        shape = Circle(4)
        self.assertEqual(math.pi * (4 ** 2), shape.get_area())
        self.assertEqual(2 * math.pi * 4, shape.get_perimeter())

    def test_case_5(self):
        shape = Circle(3)
        self.assertEqual(math.pi * (3 ** 2), shape.get_area())
        self.assertEqual(2 * math.pi * 3, shape.get_perimeter())

    def test_case_6(self):
        shape = Circle(1)
        self.assertEqual(math.pi * (1 ** 2), shape.get_area())
        self.assertEqual(2 * math.pi * 1, shape.get_perimeter())


if __name__ == '__main__':
    unittest.main()