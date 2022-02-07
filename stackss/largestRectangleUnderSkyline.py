
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