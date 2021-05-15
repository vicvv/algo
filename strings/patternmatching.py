
# you are given 2 string: one is xy kind of string and other is the 
# actuall string. find relationship and patters between the strings
# write the function to check if normal string matches the xy string
# return empty array if match isnot found
'''
example: pattern ="xxyxxy"
string = "gogopowerrangergogopowerranger"

answer : "go powerranger"
'''
# space O(n+m)| time O(N^2 + M). N^2 happends in main function

def patternMatcher(pattern, string):
    
    if len(pattern) > len(string):
        return []
    # if input pattern starts with y we need to make sure we reverse y and x so
    # the pattern starts with x and we are consitent with our code
    #     
    newPattern = getNewPattern(pattern)
    
    didSwitch = newPattern[0] != pattern[0]

    counts = {'x':0, 'y':0}
    
    firstYpos = getCountsAndFirstYpossition(newPattern, counts)
   
    
    if counts["y"] != 0:
        for lenofX in range(1,len(string)):
            lenofY = (len(string) - lenofX * counts['x'])/counts['y']
            
            if lenofY <=0  or lenofY % 1 != 0:
                continue
            lenofY = int(lenofY)
            
            yIdx = firstYpos * lenofX
            x = string[:lenofX]

            y = string[yIdx:yIdx+lenofY]
           
            potentialMatch = map(lambda char: x if char == 'x' else y , newPattern)
            nn = ''.join(potentialMatch)
           
            if string == nn:
                return [x,y] if not didSwitch else [y,x]

    # what if count y == 0?
    else:
        lenofX = len(string)/counts['x']
        lenofX = int(lenofX)
        if lenofX % 1 == 0:
            x = string[:lenofX]
            potentialMatch = map(lambda char: x, newPattern)
            if string == ''.join(potentialMatch):
                return [x, ''] if not didSwitch else ['',x]
    return []

# here we will get the counts of x an y and the first position of y

def getCountsAndFirstYpossition(pattern, counts):
    firstYposition = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == 'y' and firstYposition is None:
            firstYposition = i
    return firstYposition



# we make sure that our pattern always starts with x so if first letter is y
# we will switch y to x and vice versa

#simplifying the algo and return new pattern where x turned to y and vversa'
def getNewPattern(pattern):
    # patternLetters = list(pattern)
    # if pattern[0] == 'x':
    #     return patternLetters
    # else:
    #     #return list(map(lambda char:  "x" if char == 'y' else 'y', patternLetters))
    #     return ["y" if i=="x" else "x" for i in pattern]
    return list(pattern) if pattern[0] == "x" else ["y" if i=="x" else "x" for i in pattern]



pattern ="xxyxxy"
string = "gogopowerrangergogopowerranger"

print(patternMatcher(pattern,string))

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(patternMatcher("xyxy", "abab"), ["a", "b"])

    def test_case_2(self):
        self.assertEqual(patternMatcher("yxyx", "abab"), ["b", "a"])

    def test_case_3(self):
        self.assertEqual(patternMatcher("yxx", "yomama"), ["ma", "yo"])

    def test_case_4(self):
        self.assertEqual(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"), ["go", "powerranger"])

    def test_case_5(self):
        self.assertEqual(patternMatcher("yyxyyx", "gogopowerrangergogopowerranger"), ["powerranger", "go"])

    def test_case_6(self):
        self.assertEqual(
            patternMatcher(
                "xyxxxyyx", "baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom"
            ),
            ["baddaddoom", "baddaddoomi"],
        )

    def test_case_7(self):
        self.assertEqual(
            patternMatcher(
                "yxyyyxxy", "baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom"
            ),
            ["baddaddoomi", "baddaddoom"],
        )

    def test_case_8(self):
        self.assertEqual(patternMatcher("xxyxyy", "testtestwrongtestwrongtest"), [])

    def test_case_9(self):
        self.assertEqual(
            patternMatcher(
                "xyxxxyyx", "baddaddoombaddadoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom"
            ),
            [],
        )

    def test_case_10(self):
        self.assertEqual(patternMatcher("xyx", "thisshouldobviouslybewrong"), [])

    def test_case_11(self):
        self.assertEqual(patternMatcher("xxxx", "testtesttesttest"), ["test", ""])

    def test_case_12(self):
        self.assertEqual(patternMatcher("yyyy", "testtesttesttest"), ["", "test"])

if __name__ == "__main__":
    unittest.main()