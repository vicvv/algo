

# o(n) time| O(1) space
import unittest

def longestPeak(array):
    longestPeakLenght = 0
    i = 1

    while i < len(array) - 1:
        isPick = array[i - 1] < array[i]  and array[i] > array[i + 1]
        if not isPick:
            i += 1
            continue
        # when pick is found moving left and right to see falls on both sides
        leftIndex = i - 2
        while leftIndex >=0 and array[leftIndex] < array[leftIndex + 1]:
            leftIndex -= 1
			
        rightIndex = i + 2
        while rightIndex < len(array) and array[rightIndex] < array[rightIndex - 1]:
            rightIndex +=1

        currentLonger = rightIndex - leftIndex - 1
        longestPeakLenght = max(longestPeakLenght,currentLonger) 
        i = rightIndex  
    
    return longestPeakLenght



# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

#array = [5, 4, 3, 2, 1, 2, 1] 
array = [0,1,0]      
        
print(longestPeak(array))


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = []
        expected = 0
        self.assertEqual(longestPeak(array), expected)

    def test_case_2(self):
        array = [1, 3, 2]
        expected = 3
        self.assertEqual(longestPeak(array), expected)

    def test_case_3(self):
        array = [1, 2, 3, 4, 5, 1]
        expected = 6
        self.assertEqual(longestPeak(array), expected)

    def test_case_4(self):
        array = [5, 4, 3, 2, 1, 2, 1]
        expected = 3
        print(longestPeak(array))
        self.assertEqual(longestPeak(array), expected)

    def test_case_5(self):
        array = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
        expected = 5
        self.assertEqual(longestPeak(array), expected)

    def test_case_6(self):
        array = [5, 4, 3, 2, 1, 2, 10, 12]
        expected = 0
        self.assertEqual(longestPeak(array), expected)

    def test_case_7(self):
        array = [1, 2, 3, 4, 5, 6, 10, 100, 1000]
        expected = 0
        self.assertEqual(longestPeak(array), expected)

    def test_case_8(self):
        array = [1, 2, 3, 3, 2, 1]
        expected = 0
        self.assertEqual(longestPeak(array), expected)

    def test_case_9(self):
        array = [1, 1, 3, 2, 1]
        expected = 4
        self.assertEqual(longestPeak(array), expected)

    def test_case_10(self):
        array = [1, 2, 3, 2, 1, 1]
        expected = 5
        self.assertEqual(longestPeak(array), expected)

    def test_case_11(self):
        array = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
        expected = 9
        self.assertEqual(longestPeak(array), expected)

    def test_case_12(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longestPeak(array), expected)


# if __name__ == "__main__":
#     unittest.main()