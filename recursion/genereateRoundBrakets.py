# this  is from leetcode



def generateParenthesis(n):
    matchingperents = []
    dfs(n - 1, n, '(', matchingperents)
    return matchingperents

def dfs( left, right, s, result,):
    if (left == 0 and right == 0):
        result.append(s)

    if (left > 0):
        dfs(left - 1, right, s + '(', result)

    if (right > 0 and left < right):
        dfs(left, right - 1, s + ')', result)
            

print(generateParenthesis(3))
