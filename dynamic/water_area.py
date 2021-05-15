
# given an array of positive integers where each non-zero integer represents the height of the pilar
# with width 1. Imagine water being poured over all of the pilars. Writhe the function that returs water 
# area

#O(n) time | O(n) space

def waterArea(heights):
    maxes = [0 for x in heights]

    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax,height)

    rightMax = 0
    
    for i in reversed(range(len(heights))):
        height = heights[i]
        minheights = min(rightMax, maxes[i])
        if minheights > height:
            maxes[i] =  minheights - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax,height)

    return sum(maxes)



           
heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]        
print(waterArea(heights), end = '')

# import unittest

# class TestProgram(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]), 48)

# if __name__ == "__main__":
#     unittest.main()