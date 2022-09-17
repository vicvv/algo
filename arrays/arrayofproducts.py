

'''
Write a function that takes in a non-empty array of integers and returns an array of 
the same length, where each element in the output array is
equal to the product of every other number in the input array.
In other words, the value at output[i] is equal to the product of every number in 
the input array other than input[i] .
Note that you're expected to solve this problem without using division.
Sample Input
array = [5, 1, 4, 2]
Sample Output
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4
'''

# if we allow to use divide the total product on running integer we will solve it fast

# def prod(l):
#   p=1
#   for i in l:
#     p*=i
#   return p

# def arrayOfProducts(l):
#   return [int(prod(l)/i) for i in l if i!=0] 



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