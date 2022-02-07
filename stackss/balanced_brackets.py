# O(n) time | O(n) space

def balancedBrackets(string):
    opening = '([{'
    closing = ')]}'
    matching = {
                '}' : '{',
                 ')': '(',
                ']' : '['
                }

    stack =[]

    for b in string:
        if b in opening:
            stack.append(b)
        elif b in closing:
            if len(stack) == 0:
                return False
            if stack[-1] == matching[b]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


# def valid_parentheses(s):
#     stack = 0
#     for char in s:
#         if char == '(':
#             stack += 1
#         if char == ')':
#             if not stack:
#                 return False
#             else:
#                 stack -= 1
#     return not stack



#str = "([])(){}(())()()"
#str = "()()[{()})]"
#print(balancedBrackets(str))


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets("()[]{}{"), False)

    def test_case_2(self):
        self.assertEqual(balancedBrackets("(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"), False)

    def test_case_3(self):
        self.assertEqual(balancedBrackets("()()[{()})]"), False)

    def test_case_4(self):
        self.assertEqual(balancedBrackets("(()())((()()()))"), True)

    def test_case_5(self):
        self.assertEqual(balancedBrackets("{}()"), True)

    def test_case_6(self):
        self.assertEqual(balancedBrackets("()([])"), True)

    def test_case_7(self):
        self.assertEqual(balancedBrackets("((){{{{[]}}}})"), True)

    def test_case_8(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)

    def test_case_9(self):
        self.assertEqual(balancedBrackets("((({})()))"), True)

    def test_case_10(self):
        self.assertEqual(balancedBrackets("(([]()()){})"), True)

    def test_case_11(self):
        self.assertEqual(
            balancedBrackets("(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(())"),
            True,
        )

    def test_case_12(self):
        self.assertEqual(balancedBrackets("{[[[[({(}))]]]]}"), False)

    def test_case_13(self):
        self.assertEqual(balancedBrackets("[((([])([]){}){}){}([])[]((())"), False)

    def test_case_14(self):
        self.assertEqual(balancedBrackets(")[]}"), False)


if __name__ == "__main__":
    unittest.main()