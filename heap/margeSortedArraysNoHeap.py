def mergeSortedArrays(arrays):
    print(arrays)
    sortedList = []
    elementIndexes = [0 for array in arrays]
    while True:
        smallestItems = []
        for arrayIdx in range(len(arrays)):
            releventArray = arrays[arrayIdx]
            elementIdx = elementIndexes[arrayIdx]
            if elementIdx == len(releventArray ):
                continue
            smallestItems.append({"arrayIndex": arrayIdx, "num":releventArray[elementIdx]})
        if len(smallestItems) == 0:
            break
        nextItem = getMinValue(smallestItems)
        sortedList.append(nextItem["num"])
        elementIndexes[nextItem["arrayIndex"]] += 1
    return sortedList

def getMinValue(items):
    minValueIndex = 0
    for i in range(1, len(items)):
        if items[i]["num"] < items[minValueIndex]["num"]:
            minValueIndex = i
    return items[minValueIndex]


import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        arrays = [
            [1, 5, 9, 21],
            [-1, 0],
            [-124, 81, 121],
            [3, 6, 12, 20, 150],
        ]
        output = mergeSortedArrays(arrays)
        self.assertEqual(output, [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150])
if __name__ == "__main__":
    unittest.main()