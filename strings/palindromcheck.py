'''find if string is palindrome'''


# O(n) time and O(1) space using pointers
def isPalindrome(string):
    # Write your code here.

    i = 0
    j = len(string) - 1

    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    
    return True

# O(n) time | O(n) space using recursion
def iisPalindrome(string, i = 0):
  
    j = len(string) - i - 1
    return True if i >= j else string[i] == string[j] and iisPalindrome(string, i+1)


    # Write your code here.



string = 'abcdcba'
print(isPalindrome(string))
print(iisPalindrome(string))