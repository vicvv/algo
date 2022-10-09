
#wrapper function to add one to the result

def addone(funct):
    
    def inner(*a,**b):        
        theresult = funct(*a,**b)
        return theresult + 1
    return inner

@addone
def add_values(x, y):
    return x + y

import unittest



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        result = add_values(0, 0)
        self.assertEquals(1, result)

    def test_case_2(self):
        result = add_values(9, 32)
        self.assertEquals(42, result)

    def test_case_3(self):
        result = add_values(-5, 100)
        self.assertEquals(96, result)

    def test_case_4(self):
        result = add_values(-10, 22)
        self.assertEquals(13, result)

    def test_case_5(self):
        result = add_values(76, 4)
        self.assertEquals(81, result)

    def test_case_6(self):
        result = add_values(-4, -2)
        self.assertEquals(-5, result)

if __name__ ==("__main__"):
    unittest.main()