
memo = {}
def factorial(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 1
    else:
        x = factorial(n - 1) * n
        memo[n] = x
        return x

print(factorial(5))

