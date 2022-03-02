'''

  Write a function that takes in an array of integers and returns an array of
  the same length, where each element in the output array corresponds to the
  number of integers in the input array that are to the right of the relevant
  index and that are strictly smaller than the integer at that index.

''' 


import unittest

rightSmallerThan=lambda ar:[sum(1 for j in range(i,len(ar)) if ar[i] > ar[j]) for i in range(len(ar))]



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [8, 5, 11, -1, 3, 4, 2]
        expected = [5, 4, 4, 0, 1, 1, 0]
        actual = rightSmallerThan(array)
        self.assertEqual(expected, actual)

if __name__=="__main__":
    unittest.main()
