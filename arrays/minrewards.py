# this is a problem with local min and max 
# O(n)time complexity | O(n) space comlexity
# find a local min and do inscrements from there.

# def minRewards(scores):
#     rewards = [1 for _ in scores]
#     localMins = getLocalMinIdx(scores)
#     print(localMins)
#     for localMinIdx in localMins:
#         expandFromLocalMins(localMinIdx,scores,rewards)
#     print(rewards)
#     return sum(rewards)
        
# def expandFromLocalMins(localMinIdx,scores,rewards):
	
# 	leftIdx = localMinIdx - 1
# 	while leftIdx >=0 and scores[leftIdx] > scores[leftIdx + 1]:
# 		rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1]  + 1 )
# 		leftIdx -=1
# 	rightIdx = localMinIdx + 1
# 	while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
# 		rewards[rightIdx] = rewards[rightIdx - 1] + 1	
# 		rightIdx +=1 

# def getLocalMinIdx(array):
# 	if len(array) == 1:
# 		return [0]
# 	mymins = []
# 	for i in range(len(array)):
# 		if i == 0 and array[i] < array[i+1]:
# 			print(array[i], array[i+1])
# 			mymins.append(i)
# 		if i == len(array) - 1 and array[i] < array[i-1]:
# 			mymins.append(i)
# 		if i == 0 or i == len(array) - 1:
# 			continue
# 		if array[i] < array[i + 1] and array[i] < array[i-1]:
# 			mymins.append(i)	
# 	return mymins


# this one is the same as below but I understand it better
def minRewards(scores):
    rewards = [1 for _ in scores]
    
    for i in range(len(scores) - 1):
        if scores[i] < scores[i+1]:
            rewards[i+1] = rewards[i] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i+1] < scores[i]:
            print(i, i+1, scores[i], scores[i+1])
            rewards[i] = max(rewards[i], rewards[i+1] +1)
    
    print(rewards)
    
    return sum(rewards)


# # O(n) time| O(n) space

# def minRewards(scores):
#     myrew = [1]*len(scores)
    
#     for num in range(1,len(scores)):
#         if scores[num] > scores[num - 1]:
#             myrew[num] = myrew[num - 1] + 1
    
#     for num in reversed(range(len(scores) - 1)):
#         if scores[num] > scores[num + 1]:
#             myrew[num] = max(myrew[num], myrew[num + 1] + 1)
    
#     return sum(myrew)

# # naive solution
# def minRewards(scores):
#     rewards = [1 for _ in scores]

#     for i in range(1, len(scores)):
#         j = i-1
#         if scores[i] > scores[j]:
#             rewards[i] = rewards[j] + 1
#         else:
#             while j >= 0 and scores[j] > scores[j+1]:
#                 rewards[j] = max(rewards[j], rewards[j+1] +1)
#                 j -= 1
#     print(rewards)
#     return sum(rewards)

   
array = [8, 4, 2, 1, 3, 6, 7, 9, 5]

#[4,3,2,1,2,3,4,5,1]
# 1,0,-1,0,1,2,3,2]
print(minRewards(array))

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minRewards([1]), 1)

    def test_case_2(self):
        self.assertEqual(minRewards([5, 10]), 3)

    def test_case_3(self):
        self.assertEqual(minRewards([10, 5]), 3)

    def test_case_4(self):
        self.assertEqual(minRewards([4, 2, 1, 3]), 8)

    def test_case_5(self):
        self.assertEqual(minRewards([0, 4, 2, 1, 3]), 9)

    def test_case_6(self):
        self.assertEqual(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)

    def test_case_7(self):
        self.assertEqual(minRewards([2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]), 52)

    def test_case_8(self):
        self.assertEqual(minRewards([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]), 15)

    def test_case_9(self):
        self.assertEqual(
            minRewards(
                [
                    800,
                    400,
                    20,
                    10,
                    30,
                    61,
                    70,
                    90,
                    17,
                    21,
                    22,
                    13,
                    12,
                    11,
                    8,
                    4,
                    2,
                    1,
                    3,
                    6,
                    7,
                    9,
                    0,
                    68,
                    55,
                    67,
                    57,
                    60,
                    51,
                    661,
                    50,
                    65,
                    53,
                ]
            ),
            93,
        )

if __name__ =="__main__":
    unittest.main()