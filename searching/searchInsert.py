
# return index of target or virtual index of target if target does not exists.

def searchInsert(nums,target):
    left = 0
    right = len(nums)-1
    
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(left)
    return left
        
            

import unittest

class TestProgram (unittest.TestCase):
    def test1(self):
        self.assertEqual(searchInsert([1,3,4,7,8],2),1)
    def test2(self):
        self.assertEqual(searchInsert([1,3,5,6],2),1)
    def test3(self):
        self.assertEqual(searchInsert([1,3,5,6],7),4)
    def test4(self):
        self.assertEqual(searchInsert([1,3,5,6],0),0)
    def test5(self):
        self.assertEqual(searchInsert([1,2,3,4,5,10],2),1)
    def test7(self):
        self.assertEqual(searchInsert([1,2,3,4,5,10],12),6)

if __name__ == "__main__":
    unittest.main()