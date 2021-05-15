'''
write a function that takes string and returns string reverced:
"tim is great" ==> "great is team"
we are not alowed to use split or reverse
'''

def reverseWordsInString(string):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        character = string[idx]
        
        if character == " ":
            words.append(string[startOfWord:idx])
            startOfWord = idx
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx
            
    words.append(string[startOfWord:])

    reverseWords(words)
    return "".join(words)

def reverseWords(words):
    start, end = 0, len(words)-1
    while start < end:
        words[start], words[end] = words[end], words[start]
        start += 1
        end -=1
            

print(reverseWordsInString("tim is great"))
print(reverseWordsInString("AlgoExpert is the best!"))

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "AlgoExpert is the best!"
        expected = "best! the is AlgoExpert"
        actual = reverseWordsInString(input)
        self.assertEqual(actual, expected)

# if __name__ == "__main__":
#     unittest.main()
