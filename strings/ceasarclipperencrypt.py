'''given a non-empty string or lowercase letter and positive integer k
shift every letter by k position in the alphabeth. z shifts to the beginnig of the alphabeth'''

# O(n) time | O(n) space
# def caesarCipherEncryptor(str, key):
#     import string
#     # Write your code here.
#     mylist = list(string.ascii_lowercase)
#     result =[]
#     for i in str:
#         if i in mylist:
#             myletter = mylist[(mylist.index(i) + key)%26]
#             result.append(myletter)
#     print(result)
#     return ''.join(result)
# ---------
# def caesarCipherEncryptor(string, key):
#     newLetters = []
#     newKey = key%26

#     for letter in string:
#         newLetters.append(getNewKey(letter, newKey))
#     return ''.join(newLetters)

# def getNewKey(letter, newKey):
# 	newLetterCode = ord(letter) + newKey
# 	if newLetterCode <= 122:
# 		return chr(newLetterCode)
# 	else:
# 		return chr(96 + newLetterCode%122)

def caesarCipherEncryptor(string, key):
    newLetter = []
    newKey = key %26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetter.append(getNewLetter(letter, newKey, alphabet))
    return ''.join(newLetter)

def getNewLetter(letter, newKey, alphabet):
	newLetterCode = alphabet.index(letter) + newKey
	return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]

string = "xyz"
key = 54
#result = "zab"
print(caesarCipherEncryptor(string, key))


import unittest

class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(caesarCipherEncryptor("abc",0),"abc")
    def test2(self):
        self.assertEqual(caesarCipherEncryptor("xyz",54),"zab")

if __name__ == "__main__":
    unittest.main()
