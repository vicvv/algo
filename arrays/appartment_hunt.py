# O(br)time | O(br) space

def apartmentHunting(blocks, reqs):
    minDistFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
    #print("min",minDistFromBlocks)
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistFromBlocks)
    #print("max",maxDistancesAtBlocks)

    return getIdxAtMinValue(maxDistancesAtBlocks)

def getMinDistances(blocks, req):
    minDist = [0 for block in blocks]
    closestReqIndex = float("inf")

    for i in range(len(blocks)):
        if blocks[i][req]:

            closestReqIndex = i
        minDist[i] = distBetween(i,closestReqIndex)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIndex = i
        minDist[i] = min(minDist[i],distBetween(i, closestReqIndex))
    
    return minDist


def getMaxDistancesAtBlocks(blocks, minDistFromBlocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesAtBlock = list(map(lambda distances: distances[i], minDistFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
    return maxDistancesAtBlocks
    

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minval = float('inf')
    for i in range(len(array)):
        curVal = array[i]
        if curVal < minval:
            minval = curVal
            idxAtMinValue = i
    return idxAtMinValue




def distBetween(i,j):
    return abs(i-j)

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        blocks = [
            {"gym": False, "school": True, "store": False},
            {"gym": True, "school": False, "store": False},
            {"gym": True, "school": True, "store": False},
            {"gym": False, "school": True, "store": False},
            {"gym": False, "school": True, "store": True},
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(apartmentHunting(blocks, reqs), 3)

    def test_case_2(self):
        blocks = [
            {"gym": False, "office": True, "school": True, "store": False},
            {"gym": True, "office": False, "school": False, "store": False},
            {"gym": True, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": True},
        ]
        reqs = ["gym", "office", "school", "store"]
        self.assertEqual(apartmentHunting(blocks, reqs), 2)

    def test_case_3(self):
        blocks = [
            {"gym": False, "office": True, "school": True, "store": False},
            {"gym": True, "office": False, "school": False, "store": False},
            {"gym": True, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": False},
            {"gym": False, "office": False, "school": True, "store": True},
        ]
        reqs = ["gym", "office", "school", "store"]
        self.assertEqual(apartmentHunting(blocks, reqs) in [2, 3], True)

    def test_case_4(self):
        blocks = [
            {"foo": True, "gym": False, "kappa": False, "office": True, "school": True, "store": False},
            {"foo": True, "gym": True, "kappa": False, "office": False, "school": False, "store": False},
            {"foo": True, "gym": True, "kappa": False, "office": False, "school": True, "store": False},
            {"foo": True, "gym": False, "kappa": False, "office": False, "school": True, "store": False},
            {"foo": True, "gym": True, "kappa": False, "office": False, "school": True, "store": False},
            {"foo": True, "gym": False, "kappa": False, "office": False, "school": True, "store": True},
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(apartmentHunting(blocks, reqs) in [4, 5], True)

    def test_case_5(self):
        blocks = [
            {"gym": True, "school": True, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": True, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": False, "store": True},
            {"gym": True, "school": False, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": False, "store": False},
            {"gym": False, "school": True, "store": False},
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(apartmentHunting(blocks, reqs), 2)

    def test_case_6(self):
        blocks = [
            {"gym": True, "pool": False, "school": True, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": True, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": False, "store": True},
            {"gym": True, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": False, "store": False},
            {"gym": False, "pool": False, "school": True, "store": False},
            {"gym": False, "pool": True, "school": False, "store": False},
        ]
        reqs = ["gym", "pool", "school", "store"]
        self.assertEqual(apartmentHunting(blocks, reqs), 7)

    def test_case_7(self):
        blocks = [
            {"gym": True, "office": False, "pool": False, "school": True, "store": False},
            {"gym": False, "office": False, "pool": False, "school": False, "store": False},
            {"gym": False, "office": True, "pool": False, "school": True, "store": False},
            {"gym": False, "office": True, "pool": False, "school": False, "store": False},
            {"gym": False, "office": False, "pool": False, "school": False, "store": True},
            {"gym": True, "office": True, "pool": False, "school": False, "store": False},
            {"gym": False, "office": False, "pool": True, "school": False, "store": False},
            {"gym": False, "office": False, "pool": False, "school": False, "store": False},
            {"gym": False, "office": False, "pool": False, "school": False, "store": False},
            {"gym": False, "office": False, "pool": False, "school": True, "store": False},
            {"gym": False, "office": False, "pool": True, "school": False, "store": False},
        ]
        reqs = ["gym", "pool", "school", "store"]
        self.assertEqual(apartmentHunting(blocks, reqs), 4)

if __name__ == "__main__":
    unittest.main()
