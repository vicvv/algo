

'''
write the function that takes non empty array of integer and returns the array of
integers product but any other exept the current

array = [5,1,4,2]
result = [8,40,10,20]
8 = 1*4*5
'''

# if we allow to use devide the total product on running integer we will solve it quicky.

# def arrayOfProducts(array):
#     products = [1 for i in array]
#     for i in range(len(array)):
#         runningProduct = 1
#         for j in range(len(array)):
#             if j != i:
#                 runningProduct *= array[j]
#         products[i] = runningProduct
#     return products

def arrayOfProducts(array):
    products = [ 1 for i in array]
    leftp = [1] * len(array)
    rightp = [1] * len(array)
    print(products,leftp, rightp)

    leftRunningProd = 1

    for i in range(len(array)):
        leftp[i] = leftRunningProd
        leftRunningProd *= array[i]
    rightRunningProd = 1

    for i in reversed(range(len(array))):
        rightp[i] = rightRunningProd
        rightRunningProd *= array[i]
        
    for i in range(len(array)):
        products[i] = leftp[i] * rightp[i]
        
    return products


print(arrayOfProducts([5,1,4,2]))
import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        array = [5,1,4,2]
        result = [8,40,10,20]
        self.assertEqual(arrayOfProducts(array), result)

if __name__ == "__main__":
    unittest.main()