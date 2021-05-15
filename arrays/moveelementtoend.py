'''
given the array of integers and an integer the function moves all instances of 
the integer to the end of the array. The function performs it in place and does not 
need to maintain the order of the elements in array.
'''
# if order have to be preserved use below
# return [nonZero for nonZero in arr if nonZero!=0] + [Zero for Zero in arr if Zero==0] 

import unittest

array = [2,1,2,2,2,3,4,2]
toMove = 2

# result [1,3,4,2,2,2,2,2] . 1,3,4 could be in differnt order
# O(n) time| O(1) space where n is a number of elements in array
def moveElementToEnd(array, toMove):

    # setting 2 pointers
    i = 0
    j = len(array) - 1

    
    while i < j:

        # if the end pointer equal to toMove I move the pointer inwards
        while i < j and array[j] == toMove:
            j -=1
        
        # if start pointer equal to toMove I do the swap
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i +=1
    return array
          

print(moveElementToEnd(array, toMove))

class Test(unittest.TestCase):
    def test_case_1(self):
        array = []
        toMove = 3
        expected = []
        output = moveElementToEnd(array, toMove)
        self.assertEqual(output, expected)

    def test_case_2(self):
        array = [1, 2, 4, 5, 6]
        toMove = 3
        expected = [1, 2, 4, 5, 6]
        output = sorted(moveElementToEnd(array, toMove))
        self.assertEqual(output, expected)

    def test_case_3(self):
        array = [3, 3, 3, 3, 3]
        toMove = 3
        expected = [3, 3, 3, 3, 3]
        output = moveElementToEnd(array, toMove)
        self.assertEqual(output, expected)

    def test_case_4(self):
        array = [3, 1, 2, 4, 5]
        toMove = 3
        expectedStart = [1, 2, 4, 5]
        expectedEnd = [3]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:4])
        outputEnd = output[4:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

    def test_case_5(self):
        array = [1, 2, 4, 5, 3]
        toMove = 3
        expectedStart = [1, 2, 4, 5]
        expectedEnd = [3]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:4])
        outputEnd = output[4:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

    def test_case_6(self):
        array = [1, 2, 3, 4, 5]
        toMove = 3
        expectedStart = [1, 2, 4, 5]
        expectedEnd = [3]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:4])
        outputEnd = output[4:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

    def test_case_7(self):
        array = [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        toMove = 5
        expectedStart = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        expectedEnd = [5, 5, 5, 5, 5, 5]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:11])
        outputEnd = output[11:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

    def test_case_8(self):
        array = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
        toMove = 5
        expectedStart = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        expectedEnd = [5, 5, 5, 5, 5, 5]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:11])
        outputEnd = output[11:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

    def test_case_9(self):
        array = [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12]
        toMove = 5
        expectedStart = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        expectedEnd = [5, 5, 5, 5, 5, 5]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:11])
        outputEnd = output[11:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

    def test_case_10(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)



if __name__ == "__main__":
    unittest.main()
