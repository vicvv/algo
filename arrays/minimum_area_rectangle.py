'''Minimum Area Rectangle
You're given an array of points plotted on a 2D graph (the xyplane). 
Write a function that returns the minimum area of any
rectangle that can be formed using any 4 of these points such that
the rectangle's sides are parallel to the x and y axes (i.e., only
rectangles with horizontal and vertical sides should be
considered--no rectangles with diagonal sides). If no rectangle can
be formed, your function should return 0 .
The input array will contain points represented by arrays of two
integers [x, y] . The input array will never contain duplicate
points.'''

# O(n^2) time | O(n) space - where n is the number of points
def minimumAreaRectangle(points):
    columns = initializeColumns(points)
    minimumAreaFound = float("inf")
    edgesParallelToYAxis = {}
    sortedColumns = sorted(columns.keys())
    for x in sortedColumns:
        yValuesInCurrentColumn = columns[x]
        yValuesInCurrentColumn.sort()
        for currentIdx, y2 in enumerate(yValuesInCurrentColumn):
            for previousIdx in range(currentIdx):
                y1 = yValuesInCurrentColumn[previousIdx]
                pointString = str(y1) + ":" + str(y2)
                if pointString in edgesParallelToYAxis:
                    currentArea = (x - edgesParallelToYAxis[pointString]) * (y2 - y1)
                    minimumAreaFound = min(minimumAreaFound, currentArea)
                edgesParallelToYAxis[pointString] = x
    return minimumAreaFound if minimumAreaFound != float("inf") else 0
    
def initializeColumns(points):
    columns = {}
    for point in points:
        x, y = point
        if x not in columns:
            columns[x] = []
        columns[x].append(y)
    return columns

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 5], [5, 1], [4, 2], [2, 4], [2, 2], [1, 2], [4, 5], [2, 5], [-1, -2]]
        expected = 3
        actual = minimumAreaRectangle(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()