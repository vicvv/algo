'''
Given the number of pairs of parentheses, return an array of strings, 
where each string represents a different valid way to order those parentheses. 
Example: given 2, return ["()()", "(())"].
'''
'''
len(printParenthesis(4)) to return 14
len(printParenthesis(6)) to return 132
len(printParenthesis(7)) to return 429
'''

def printParenthesis(num):
    ans = []
    start = ''
    helper(start, 0, 0, num, ans)
    return len(ans)

def helper(start, left, right, num, ans):
    if left == num and right == num:
    #if len(start) == 2 * num:
        ans.append(start)
        return
    
    if left < num:
        helper(start+'(', left+1, right,num,ans)
    if right < left:
        helper(start+')', left, right+1,num,ans)


import unittest

class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(printParenthesis(4),14)
    def test2(self):
        self.assertEqual(printParenthesis(6),132)
    def test3(self):
        self.assertEqual(printParenthesis(7),429)

if __name__ == "__main__":
    unittest.main()