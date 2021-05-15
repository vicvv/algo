

'''write a function that given a string, returns its larges palindromic substring'''

'''
palindrome can be odd or even that is why in our solution we are expending from the middle:
if we found that left and righ are mattching we are moving further right and left untill 
we find the palindrom. Than we return to main function to compare the lenght.
'''

# O(n^2) time | O(1) space
string = "abaxyzzyxf" 
# res ="xyzzyx"
# def longestPalindromicSubstring(string):

#     # declering first letter of the string as a current longest palindrome
#     current_longest = [0,1]
#     # palindrome can have odd or even number of characters.
#     for i in range(len(string)):
#         odd = findLongestPalindrome(string, i - 1, i + 1)
#         even = findLongestPalindrome(string, i - 1, i)

#         longest = max(odd, even, key=lambda x: x[1] - x[0])
#         current_longest = max(current_longest, longest,key=lambda x: x[1] - x[0])

#     return string[current_longest[0] : current_longest[1]]

# def findLongestPalindrome(string, leftinx, rightindx):
#     while leftinx >= 0 and rightindx < len(string):
#         if string[leftinx] != string[rightindx]:
#             break
#         else:
#             leftinx -= 1
#             rightindx +=1
#     return [leftinx +1, rightindx]

def longestPalindromicSubstring(string):
    current_longest = [0,1]

    for i in range(1,len(string)):
        #print(string[i-1], string[i+1])
        odd = findPalindrom(string, i - 1 , i + 1)
        even = findPalindrom(string, i - 1, i)
        #print(odd, even)

        longest = max(odd,even, key=lambda x: x[1] - x[0])
        current_longest = max(current_longest, longest,key=lambda x: x[1] - x[0])
        print(longest, current_longest)
    
    return string[current_longest[0]:current_longest[1]]



def findPalindrom(string, leftind, rightind):

    while leftind >= 0  and rightind < len(string):
        if string[leftind] != string[rightind]:
            break
        else:
            leftind -= 1
            rightind += 1
    return [leftind+1, rightind]



print(longestPalindromicSubstring(string))

import unittest
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(longestPalindromicSubstring("abaxyzzyxf"), "xyzzyx")
if __name__ == "__main__":
    unittest.main()