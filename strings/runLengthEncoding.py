
import unittest
def runLengthEncoding(string):
    finalString=[]
    currentCount = 1
    
    for i in range(1, len(string)):
        if string[i] != string[i-1] or currentCount ==9:
            finalString.append(str(currentCount))
            finalString.append(string[i-1])
            currentCount = 0
        currentCount += 1

    finalString.append(str(currentCount))
    finalString.append(string[-1])

    return ''.join(finalString)

#print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "AAAAAAAAAAAAABBCCCCDD"
        expected = "9A4A2B4C2D"
        actual = runLengthEncoding(string)
        self.assertEqual(actual, expected)


    def test_case_2(self):
        string = "aA"
        expected = "1a1A"
        actual = runLengthEncoding(string)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()


