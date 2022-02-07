
def filterRange(arr, num1, num2):
    arr = [num for num in arr if num1 < num < num2]
    return arr

import unittest

class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(filterRange([1,3,5,7,10], 4, 8) ,[5, 7])
    def test2(self):
        self.assertEqual(filterRange([1,3,5,7,10], -1, 4) ,[1, 3])
    def test3(self):
        self.assertEqual(filterRange([2,4,3,5], 2, 6) , [4, 3, 5])
    def test4(self):
        self.assertEqual(filterRange([2,4,3,5], 0, 4) ,[2, 3])
  
   
    def test5(self):
        self.assertEqual(filterRange([6,2,-3,5,7], 3, 8) ,[6, 5, 7])

if __name__ == "__main__":
    unittest.main()