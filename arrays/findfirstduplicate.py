'''
given the array of integer for 1 to n inclusinve where n is a len 
find the first dublicated integer. [2,1,5,3,3,2,4]  -->3 because 3
has the lowest index
'''

# def firstDuplicateValue(array):
#     seen = set()
#     for i in array:
#         if i in seen:
#             return i
#         seen.add(i)
#     return -1

def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return value
        array[absValue] *= -1
    return -1


print(firstDuplicateValue([2,1,5,3,3,2,4]))




import unittest

class TestClass(unittest.TestCase):
    def test1(self):
        inp = [2,1,5,3,3,2,4]
        out = 3
        self.assertEqual(firstDuplicateValue(inp), out)

# if __name__ == "__main__":
#     unittest.main()
