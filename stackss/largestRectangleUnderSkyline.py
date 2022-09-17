'''
Largest Rectangle Under Skyline
Write a function that takes in an array of positive integers representing the heights of 
adjacent buildings and returns the area of the largest
rectangle that can be created by any number of adjacent buildings, including just one building. 
Note that all buildings have the same width of
1 unit.
For example, given buildings = [2, 1, 2] , the area of the largest rectangle that can be created is 3 , 
using all three buildings. Since the
minimum height of the three buildings is 1 , you can create a rectangle that has a height of 1 and a 
width of 3 (the number of buildings).
You could also create rectangles of area 2 by using only the first building or the last building, 
but these clearly wouldn't be the largest
rectangles. Similarly, you could create rectangles of area 2 by using the first and second building 
or the second and third building.
To clarify, the width of a created rectangle is the number of buildings used to create the rectangle, 
and its height is the height of the smallest
building used to create it.
Note that if no rectangles can be created, your function should return 0 .
Sample Input
buildings = [1, 3, 3, 2, 4, 1, 5, 3, 2]
'''




def largestRectangleUnderSkyline(b):
    stack=[]
    maxA=0
    for i, height in enumerate(b+[0]):
        while stack and b[stack[-1]] >= height:
            curHeight = b[stack.pop()]
            width = i if len(stack)==0 else i-stack[-1]-1
            maxA = max(maxA, curHeight*width)
            print("h:",curHeight,"w:",width,i, "maxA",maxA, stack)
        stack.append(i)
        print('stack:',stack)

    return maxA

print(largestRectangleUnderSkyline([1, 3, 3, 2, 4, 1, 5, 3, 2]))

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 3, 3, 2, 4, 1, 5, 3, 2]
        expected = 9
        actual = largestRectangleUnderSkyline(input)
        self.assertEqual(actual, expected)

# if __name__ == '__main__':
#     unittest.main()