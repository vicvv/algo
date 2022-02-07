#return a clean path
#space|time: o(n)|o(n)

def shortenPath(path):
    # edge case to see if we are dealing with apsolute path
    isPathStartsWithRoot = path[0]=='/'
    tokens = filter(isValidToken, path.split('/'))
    stack =[]
    if isPathStartsWithRoot:
        stack.append("")
    
    
    for token in tokens:
        #edge case to see if we are dealing with relative path
        if token =='..':
            if len(stack)==0 or stack[-1]== '..':
                stack.append(token)
            elif stack[-1] !='':
                stack.pop()
        else:
            stack.append(token)
    if len(stack)==1 and stack[0]=='':
        return '/'
    return '/'.join(stack)
def isValidToken(token):
    return token != '.' and len(token)>0

import unittest

class TestProgram(unittest.TestCase):
    def testcase1(self):
        expected = "/foo/bar/baz"
        result = shortenPath("/foo/../test/../test/../foo//bar/./baz")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()