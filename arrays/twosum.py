
'''function takes in non empty array of distinct integers and a sum target
If any of two numbers sum up to the target append them into new array'''

array = [3,5,-4,8,11,1,-1,6]
targetSum = 10
#result = [-1,11]

import unittest


# my solution
'''
def twoNumberSum(array, targetSum):
    h={array[i]:i for i in range(len(array))}
    na =[]
    for num in array:
        if targetSum - num in h and targetSum - num != i:
            na.append(targetSum - i)
    return na
'''

'''def twoSum(self, nums, target):
        # mapping value to index {3: 0, 2: 1, 4: 2}              
        mapping = {n:i for i, n in enumerate(nums)}
        print(mapping)
        
        for i, num in enumerate(nums):
            diff = mapping.get(target - num)
            print(i,diff)
            
            if diff and diff != i:
                return [i, diff]
'''
'''
# to return indexes assuming that array is not sorter
def twoSum(nums, target):
        mydict = {nums[x]:x for x in range(len(nums))}
       
        for i in range(len(nums)):
            keyexists = mydict.get(target - nums[i])
            if keyexists and keyexists != i:
                return [i, keyexists]
        return [] 
'''

# solution with 2 loops
# O(n^2) time | O(1) space
'''
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        for j in range(i + 1,len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i],array[j]]
    return []
'''

'''
# in case we have more than one pair.
from itertools import combinations

def all_pairs(lst,target):
  return [sorted([i[0],i[1]]) for i in list(combinations(lst,2)) if i[0] + i[1] == target]
  
print(all_pairs([2, 4, 5, 3, 1], 7))
print(all_pairs([5, 3, 9, 2, 1], 3))
print(all_pairs([8, 7, 7, 2, 4, 6], 14))
print(all_pairs([8, 7, 2, 4, 6], 14))


# with enumerate
def all_pairs(lst,target):
  res = []; lst.sort()
  for i, n in enumerate(lst):
    if target - n in lst [i+1:]:
      res.append([n, target -n])
  return sorted(res)
print(all_pairs([2, 4, 5, 3, 1], 7))
print(all_pairs([5, 3, 9, 2, 1], 3))
print(all_pairs([8, 7, 7, 2, 4, 6], 14))
print(all_pairs([8, 7, 2, 4, 6], 14))

'''

# solution with a hash table
# O(n) time | O(n) space

def twoNumberSum(array, targetSum):
    myh = {}
    for num in array:
        if targetSum - num in myh:
            return[targetSum-num, num]
        else:
            myh[num] = True
    return []

# array = [3,5,-4,8,11,1,-1,6]
# targetSum = 10

array = [3,2,4]
targetSum = 6
# solution with left and right pointer
# O(nlog(n)) time | O(1) space

def twoNumberSum1(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:

        currentsum = array[left] + array[right]   
        if currentsum < targetSum:
            left +=1
        elif currentsum > targetSum:
            right -=1
        else:
            return [array[left], array[right]]
    
    return []

print(twoNumberSum(array, targetSum))


# Add, edit, or remove tests in this file.
# Treat it as your playground!

class Test(unittest.TestCase):
    def test_case_1(self):
        output = sorted(twoNumberSum([4, 6], 10))
        self.assertEqual(output, [4, 6])

    def test_case_2(self):
        output = sorted(twoNumberSum([4, 6, 1], 5))
        self.assertEqual(output, [1, 4])

    def test_case_3(self):
        output = sorted(twoNumberSum([4, 6, 1, -3], 3))
        self.assertEqual(output, [-3, 6])

    def test_case_4(self):
        output = sorted(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
        self.assertEqual(output, [-1, 11])

    def test_case_5(self):
        output = sorted(twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))
        self.assertEqual(output, [8, 9])


if __name__ == "__main__":
    unittest.main()