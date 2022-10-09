
'''
Poligon is an abstract class. Inherit it in Triangle and Rectangle. 
Inherit Rectangle in Square. Implement required methods. Remember
that Polygon is not an inteface.
'''

import math

class Polygon:
    def get_area(self):
        raise NotImplementedError("get_area() Method should be implemented")
    def get_sides(self):
        raise NotImplementedError("get_sides() Method should be implemented")
    def get_perimeter(self):
        return sum(self.get_sides())

class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        r = math.sqrt(
            semi_perimeter *
            (semi_perimeter - self.side1) *
            (semi_perimeter - self.side2) *
            (semi_perimeter - self.side3)
        )
        return round(r,2)

    def get_sides(self):
        return [self.side1, self.side2, self.side3]


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_sides(self):
        return [self.width, self.height]*2


class Square(Rectangle):
    def __init__(self,slen):
        super().__init__(slen, slen)
        


# Use this function in your solution.
def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )


# Use this function in your solution.
def get_rectangle_area(width, height):
    return width * height



# triangle = Triangle(2,5,6)
# print(triangle.get_area())
# print(triangle.get_perimeter())

# square = Square(4)
# print (square.get_area())


import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        with self.assertRaises(NotImplementedError):
            Polygon().get_sides()
        with self.assertRaises(NotImplementedError):
            Polygon().get_area()
        with self.assertRaises(NotImplementedError):
            Polygon().get_perimeter()

    def test_case_2(self):
        triangle = Triangle(1, 1, 1)
        self.assertEqual(3, triangle.get_perimeter())
        rect = Rectangle(2, 3)
        self.assertEqual(10, rect.get_perimeter())
        square = Square(3)
        self.assertEqual(12, square.get_perimeter())

    def test_case_3(self):
        triangle = Triangle(1, 5, 6)
        self.assertEqual([1, 5, 6], sorted(triangle.get_sides()))
        rect = Rectangle(2, 3)
        self.assertEqual([2, 2, 3, 3], sorted(rect.get_sides()))
        square = Square(3)
        self.assertEqual([3, 3, 3, 3], sorted(square.get_sides()))

    def test_case_4(self):
        triangle = Triangle(2, 5, 6)
        self.assertAlmostEqual(4.68, triangle.get_area(), delta=0.01)
        rect = Rectangle(2, 3)
        self.assertEqual(6, rect.get_area())
        square = Square(5)
        self.assertEqual(25, square.get_area())
