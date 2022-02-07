# write the function that returns n(th) fibonachi number. 
# For example getNthFib(6) will return 5 because if we print the
# sequense we will get (0,1,1,2,3,5) and 5 is the 6th element in the sequence

# iterative solution:

# O(n) time | O(1) space
# def getNthFib(n):
#     lasttwo = [0,1]
#     count = 3
#     while count <= n:
#         nextfib = lasttwo[0] + lasttwo[1]
#         lasttwo[0] = lasttwo[1]
#         lasttwo[1] = nextfib
#         count +=1
#     return lasttwo[1] if n >1 else lasttwo[0]

# using memoisation
# O(n) time | O(n) space
# def getNthFib(n,memoize = {1:0,2:1}):
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = getNthFib(n-1) + getNthFib(n-2)
#         return memoize[n]
    

    
# ---naive solution 

# O(2^N) time because we have unnessaeary calls | O(n) space 

#           fib(6)
#          /      \
#       fib(5)    fib(4)
#       /   \     /    \
#     fib(4) fib(3)    fib(2)

# as we can see above fib(5) fib(4) are both calling fib(3) so the
# calculation done twice over


# def getNthFib(n):
#     if n <= 1:
#         return 0
#     if n == 2:
#         return 1
#     else:
#         return getNthFib(n-1) + getNthFib(n-2)

# Tabulated (bottom up) version 
def getNthFib(n): 
	f = [0]*(n+1) 
	if n>0: f[1] = 1
	for i in range(2 , n+1): 
		f[i] = f[i-1] + f[i-2] 

	return f[n-1] 

# fup from edabit:
# def getNthFib(n):
#     x, y = 0, 1
#     for i in range(n):
#         x, y = y, x+y
#     return x



import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(getNthFib(1), 0)

    def test_case_2(self):
        self.assertEqual(getNthFib(2), 1)

    def test_case_3(self):
        self.assertEqual(getNthFib(3), 1)

    def test_case_4(self):
        self.assertEqual(getNthFib(4), 2)

    def test_case_5(self):
        self.assertEqual(getNthFib(5), 3)

    def test_case_6(self):
        self.assertEqual(getNthFib(6), 5)

    def test_case_7(self):
        self.assertEqual(getNthFib(7), 8)

    def test_case_8(self):
        self.assertEqual(getNthFib(8), 13)

    def test_case_9(self):
        self.assertEqual(getNthFib(9), 21)

    def test_case_10(self):
        self.assertEqual(getNthFib(10), 34)

    def test_case_11(self):
        self.assertEqual(getNthFib(11), 55)

    def test_case_12(self):
        self.assertEqual(getNthFib(12), 89)

    def test_case_13(self):
        self.assertEqual(getNthFib(13), 144)

    def test_case_14(self):
        self.assertEqual(getNthFib(14), 233)

    def test_case_15(self):
        self.assertEqual(getNthFib(15), 377)

    def test_case_16(self):
        self.assertEqual(getNthFib(16), 610)

    def test_case_17(self):
        self.assertEqual(getNthFib(17), 987)

    def test_case_18(self):
        self.assertEqual(getNthFib(18), 1597)
    def test_case_19(self):
        self.assertEqual(getNthFib(0), 0)

if __name__ == "__main__":
    unittest.main()