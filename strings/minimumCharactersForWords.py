'''
Write a function that takes in an array of words and returns the smallest array of characters 
needed to form all of the words. The characters
don't need to be in any particular order.
For example, the characters ["y", "r", "o", "u"] are needed to form the words ["your", "you", "or", "yo"] .
Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.
Sample Input
words = ["this", "that", "did", "deed", "them!", "a"]
Sample Output
["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
// The characters could be ordered differently.
'''

#time|space : O(n*l)|O(c)
# n is a number of words, l is the len of the longest word, c is the number of unique chars

def minimumCharactersForWords(words):
    maxReqChars ={}

    for word in words:
        charFreq = findCharFreq(word)
        updateMaxReqChars(charFreq,  maxReqChars)
    print(maxReqChars)
    return makeArray(maxReqChars)

def updateMaxReqChars(charFreq,  maxReqChars):
    for c in charFreq:
        if c in maxReqChars:
            maxReqChars[c] = max(maxReqChars[c], charFreq[c])
        else:
            maxReqChars[c] = charFreq[c]

def findCharFreq(word):
    return {c:word.count(c) for c in word}

def makeArray(maxReqChars):
    chars =[]
    for ch in maxReqChars:
        fr = maxReqChars[ch]
        for _ in range(fr):
            chars.append(ch)
    return chars


import unittest


class TestClass(unittest.TestCase):
    def test1(self):
        words = ["this", "that", "did", "deed", "them!", "a"]
        expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
        actual = minimumCharactersForWords(words)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()