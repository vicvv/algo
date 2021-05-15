# write a function that takes Cartesian coordinates and find all requtengles that lie 
# between them

# def rectangleMania(coords):
#     coordSet = set([(coord[0], coord[1]) for coord in coords])
#     rectangleCount = 0
#     for i in range(len(coords)):
#         for j in range(len(coords)):
#             coordOne = coords[i]
#             coordTwo = coords[j]
#             if coordOne == coordTwo:
#                 continue
#             if (coordOne[0] > coordTwo[0]) and (coordOne[1] > coordTwo[1]):
#                 if (coordOne[0], coordTwo[1]) in coordSet and (coordTwo[0], coordOne[1]) in coordSet:
#                     rectangleCount += 1
#     return rectangleCount


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
        self.assertEqual(rectangleMania(coords), 6)

if __name__ == "__main__":
    unittest.main()
