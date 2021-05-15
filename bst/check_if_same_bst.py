def sameBsts(arrayOne, arrayTwo):
    
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0 and  len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False
	
    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightOne = getBiggerOrEqual(arrayOne)
    rightTwo = getBiggerOrEqual(arrayTwo)
	
    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)


def getSmaller(array):
    arr = []
    for i in range (1,len(array)):
        if array[i] < array[0]:
            arr.append(array[i])
    return arr

def getBiggerOrEqual(array):
    bigger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])
    return bigger

# array1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
# array2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]

# print(sameBsts(array1,array1))

import unittest
class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11],[10, 8, 5, 15, 2, 12, 11, 94, 81]), True)

if __name__ == "__main__":
    unittest.main()