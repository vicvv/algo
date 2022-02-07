'''
function takes in an array of unique integers and returns its powerset
'''
# O(n*2^n) time and O(n*2^n) space
import unittest

# non recursive solution
# def powerset(array):
#     mypowset =[[]]
#     for num in array:
#         for i in range(len(mypowset)):   
#             curSet = mypowset[i]
#             print("curSet:",curSet, "after append" ,curSet + [num])
#             mypowset.append(curSet + [num])
#             print("mpt",mypowset)
    
#     return mypowset


def powerset(array, idx=None):
    if idx is None:
        idx = len(array)-1
    if idx < 0:
        return [[]]

    ele = array[idx]
    subsets = powerset(array, idx-1)
    
    for i in range(len(subsets)):
        curSubset = subsets[i]
        subsets.append(curSubset + [ele])

    return subsets




array = [1,2,3]
print(powerset(array))

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = list(map(lambda x: set(x), powerset([])))
        self.assertTrue(len(output) == 1)
        self.assertTrue(set([]) in output)

    def test_case_2(self):
        output = list(map(lambda x: set(x), powerset([1])))
        self.assertTrue(len(output) == 2)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)

    def test_case_3(self):
        output = list(map(lambda x: set(x), powerset([1, 2])))
        self.assertTrue(len(output) == 4)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)

    def test_case_4(self):
        output = list(map(lambda x: set(x), powerset([1, 2, 3])))
        self.assertTrue(len(output) == 8)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)
        self.assertTrue(set([3]) in output)
        self.assertTrue(set([1, 3]) in output)
        self.assertTrue(set([2, 3]) in output)
        self.assertTrue(set([1, 2, 3]) in output)

    def test_case_5(self):
        output = list(map(lambda x: set(x), powerset([1, 2, 3, 4])))
        self.assertTrue(len(output) == 16)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)
        self.assertTrue(set([3]) in output)
        self.assertTrue(set([1, 3]) in output)
        self.assertTrue(set([2, 3]) in output)
        self.assertTrue(set([1, 2, 3]) in output)
        self.assertTrue(set([4]) in output)
        self.assertTrue(set([1, 4]) in output)
        self.assertTrue(set([2, 4]) in output)
        self.assertTrue(set([1, 2, 4]) in output)
        self.assertTrue(set([3, 4]) in output)
        self.assertTrue(set([1, 3, 4]) in output)
        self.assertTrue(set([2, 3, 4]) in output)
        self.assertTrue(set([1, 2, 3, 4]) in output)
