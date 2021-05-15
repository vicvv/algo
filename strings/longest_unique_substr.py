'''find the longest substring of unique characters'''


# O(n) time | O(max(N,A) space) due to stroring in hash(N) and storing unique(A) chars)
instr = "clementisacap"
# res = "mentisac"


def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0,1]
    startindex = 0

    for i, char in enumerate(string, 1):
        if char in lastSeen:
            startindex = max(startindex, lastSeen[char])
        if longest[1] - longest[0] < i  - startindex:
            longest = [startindex, i]
        lastSeen[char] = i
    return string[longest[0]: longest[1]]

print(longestSubstringWithoutDuplication(instr))