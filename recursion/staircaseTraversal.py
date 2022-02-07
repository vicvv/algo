import unittest

# #O(k^n) time | O(n) space, n in a height
# # the worst time space recurcive solution
# def staircaseTraversal(height, maxSteps):
#     return numberOfStepsToTop(height, maxSteps)


# def numberOfStepsToTop(height, maxSteps):
#     if height <=1:
#         return 1

#     numOfSteps = 0
#     for step in range(1, min(height, maxSteps) +1):
#         numOfSteps += numberOfStepsToTop(height-step, maxSteps)

#     return numOfSteps

# #with memoise
# def staircaseTraversal(height, maxSteps):
#     return numberOfStepsToTop(height, maxSteps, {0:1,1:1})


# def numberOfStepsToTop(height, maxSteps,memo):
#     if height in memo:
#         return memo[height]

#     numOfSteps = 0
#     for step in range(1, min(height, maxSteps) +1):
#         numOfSteps += numberOfStepsToTop(height-step, maxSteps, memo)
#         memo[height]=numOfSteps

#     print(memo)
#     return numOfSteps

# # dymamic way

# def staircaseTraversal(height, maxSteps):
#     waysToTops = [0]*(height+1)
#     waysToTops[0]=1
#     waysToTops[1]=1

#     for currentHeight in range(2, height+1):
#         step = 1
#         while step <= maxSteps and step <= currentHeight:
#             waysToTops[currentHeight] = waysToTops[currentHeight] +waysToTops[currentHeight-step]
#             step +=1
            
#     return waysToTops[height] 

#sliding window way

def staircaseTraversal(height, maxSteps):
    currentNumberOfWays = 0
    waysToTop =[1]

    for currentHeight in range(1, height+1):
        startOfPreviousWindow = currentHeight - maxSteps - 1
        endOfWindow = currentHeight -1
        print(startOfPreviousWindow, endOfWindow)

        if startOfPreviousWindow >=0:
            currentNumberOfWays -= waysToTop[startOfPreviousWindow]

        currentNumberOfWays += waysToTop[endOfWindow]
        waysToTop.append(currentNumberOfWays)
    return waysToTop[height]


#print(staircaseTraversal(4,2)
    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal(stairs, maxSteps)
        self.assertEqual(actual, expected)


if __name__ =='__main__':
    unittest.main()