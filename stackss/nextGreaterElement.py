
# return array of next grater values.


'''

  Write a function that takes in an array of integers and returns a new array
  containing, at each index, the next element in the input array that's greater
  than the element at that index in the input array.

  In other words, your function should return a new array where outputArray[i]
  is the next element in the input array that's greater than inputArray[i]
  If there's no such next greater element for a particular index, the value at that 
  index in the output array should be -1. Your function should treat the imput array as
  circlular.


  One approach is to push onto the stack the indices of elements for which you
  haven't yet found the next greater element. If you go with this index
  approach, you need to loop through the array twice (since it's circular) and
  compare the value of the current element in the array to the one represented
  by the index on top of the stack. If the element on the top of the stack is
  smaller than the current element, then the current element is next greater
  element for the top-of-stack element, and you can pop the index off the top of
  the stack and use it to store the current element in the correct position in
  your result array. You then continue to pop elements off the top of the stack
  until the current element is no longer greater than the top-of-stack element.
  At this point, you add the index of the current element to the top of the
  stack, and you continue iterating through the array, repeating the same
  process
'''


def nextGreaterElement(array):
    result=[-1]*len(array)
    stack=[]

    for i in range(2*len(array)):
        indx = i%len(array)
        while len(stack)>0 and array[stack[-1]]< array[indx]:
            top = stack.pop()
            result[top]=array[indx]
        stack.append(indx)
    return result



import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 5, -3, -4, 6, 7, 2]
        expected = [5, 6, 6, 6, 7, -1, 5]
        actual = nextGreaterElement(input)
        self.assertEqual(actual, expected)

if __name__=='__main__':
    unittest.main()