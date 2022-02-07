
#recurcively sorted stack
#time O(n2)
#space O(n)
def sortStack(stack):
    if len(stack)==0: 
        return stack
    else:
        top = stack.pop()   
        sortStack(stack)

    insertInSortedOrder(stack,top)

    return stack

def insertInSortedOrder(stack,value):
	if len(stack)==0 or stack[-1] <= value:
		stack.append(value)
		return
	else:
		top = stack.pop()
		insertInSortedOrder(stack,value)
		stack.append(top)
	
    
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [-5, 2, -2, 4, 3, 1]
        expected = [-5, -2, 1, 2, 3, 4]
        actual = sortStack(input)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()