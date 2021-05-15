'''given array of distinct integers and a target sum return quadrupples that sum up to
the target sum

input = [7,6,4,-1,1,2],16
result = [[7,6,4,-1], [7,6,1,2]]

the soulution is to for loop the entire array and use 2 inner for loops. first inner for loop checks
if diff is in hash and if it is than form the quadrupple. If not than move on.
Second inner for loop checks if the sum between to nums is in hash and if it is not its add it.
We add sum to hash only for the nums that are before cur num.
'''
# O(n^2) time | O(n^2) space
array = [7,6,4,-1,1,2]
targetSum = 16

def fourNumberSum(array, targetSum):
    
    allPairsSum = {}
    quadruplets =[]

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):  
            currentSum = array[i] + array[j]    
            difference = targetSum - currentSum
            print(i,j, currentSum, difference)
            if difference in allPairsSum:
                for pair in allPairsSum[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        
        for k in range(0,i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairsSum:
                allPairsSum[currentSum] = [[array[k], array[i]]]
            else:
                allPairsSum[currentSum].append([array[k], array[i]])

    return quadruplets

print(fourNumberSum(array, targetSum))



import unittest

def sortAndStringify(array):
    return ",".join(sorted(list(map(lambda x: str(x), array))))

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = fourNumberSum([1, 2, 3, 4, 5, 6, 7], 10)
        output = list(map(sortAndStringify, output))
        quadruplets = [[1, 2, 3, 4]]
        self.assertTrue(len(output) == 1)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_2(self):
        output = fourNumberSum([7, 6, 4, -1, 1, 2], 16)
        output = list(map(sortAndStringify, output))
        quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]
        self.assertTrue(len(output) == 2)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_3(self):
        output = fourNumberSum([5, -5, -2, 2, 3, -3], 0)
        output = list(map(sortAndStringify, output))
        quadruplets = [[5, -5, -2, 2], [5, -5, 3, -3], [-2, 2, 3, -3]]
        self.assertTrue(len(output) == 3)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_4(self):
        output = fourNumberSum([-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
        output = list(map(sortAndStringify, output))
        quadruplets = [[-2, -1, 1, 6], [-2, 1, 2, 3], [-2, -1, 2, 5], [-2, -1, 3, 4]]
        self.assertTrue(len(output) == 4)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_5(self):
        output = fourNumberSum([-1, 22, 18, 4, 7, 11, 2, -5, -3], 30)
        output = list(map(sortAndStringify, output))
        quadruplets = [[-1, 22, 7, 2], [22, 4, 7, -3], [-1, 18, 11, 2], [18, 4, 11, -3], [22, 11, 2, -5]]
        self.assertTrue(len(output) == 5)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_6(self):
        output = fourNumberSum([-10, -3, -5, 2, 15, -7, 28, -6, 12, 8, 11, 5], 20)
        output = list(map(sortAndStringify, output))
        quadruplets = [
            [-5, 2, 15, 8],
            [-3, 2, -7, 28],
            [-10, -3, 28, 5],
            [-10, 28, -6, 8],
            [-7, 28, -6, 5],
            [-5, 2, 12, 11],
            [-5, 12, 8, 5],
        ]
        self.assertTrue(len(output) == 7)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_7(self):
        output = fourNumberSum([1, 2, 3, 4, 5], 100)
        output = list(map(sortAndStringify, output))
        self.assertTrue(len(output) == 0)


# if __name__ == "__main__":
#     unittest.main()