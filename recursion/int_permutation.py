import unittest

'''# upper bound: O(n^2*n!) time | O(n*n!)space
'''
        

# O(n * n!) time | same space
def getPermutations(array):
    permutation = []
    permutationHelper (0,array, permutation)
    return permutation

def permutationHelper(i, array, permutation):
    if i == len(array) - 1:
        permutation.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i,j)
            permutationHelper(i+1,array, permutation)
            swap(array, i,j)
def swap(array,i,j):
    array[i], array[j] = array[j], array[i]
    


arr = [1, 2, 3]
print(getPermutations(arr))

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        perms = getPermutations([])
        self.assertTrue(len(perms) == 0)

    def test_case_2(self):
        perms = getPermutations([1])
        self.assertTrue(len(perms) == 1)
        self.assertTrue([1] in perms)

    def test_case_3(self):
        perms = getPermutations([1, 2])
        self.assertTrue(len(perms) == 2)
        self.assertTrue([1, 2] in perms)
        self.assertTrue([2, 1] in perms)

    def test_case_4(self):
        perms = getPermutations([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)

    def test_case_5(self):
        perms = getPermutations([1, 2, 3, 4])
        self.assertTrue(len(perms) == 24)
        self.assertTrue([1, 2, 3, 4] in perms)
        self.assertTrue([1, 2, 4, 3] in perms)
        self.assertTrue([1, 3, 2, 4] in perms)
        self.assertTrue([1, 3, 4, 2] in perms)
        self.assertTrue([1, 4, 3, 2] in perms)
        self.assertTrue([1, 4, 2, 3] in perms)
        self.assertTrue([2, 1, 3, 4] in perms)
        self.assertTrue([2, 1, 4, 3] in perms)
        self.assertTrue([2, 3, 1, 4] in perms)
        self.assertTrue([2, 3, 4, 1] in perms)
        self.assertTrue([2, 4, 1, 3] in perms)
        self.assertTrue([2, 4, 3, 1] in perms)
        self.assertTrue([3, 1, 2, 4] in perms)
        self.assertTrue([3, 1, 4, 2] in perms)
        self.assertTrue([3, 2, 1, 4] in perms)
        self.assertTrue([3, 2, 4, 1] in perms)
        self.assertTrue([3, 4, 1, 2] in perms)
        self.assertTrue([3, 4, 2, 1] in perms)
        self.assertTrue([4, 1, 2, 3] in perms)
        self.assertTrue([4, 1, 3, 2] in perms)
        self.assertTrue([4, 2, 1, 3] in perms)
        self.assertTrue([4, 2, 3, 1] in perms)
        self.assertTrue([4, 3, 1, 2] in perms)
        self.assertTrue([4, 3, 2, 1] in perms)

if __name__ == "__main__":
    unittest.main()