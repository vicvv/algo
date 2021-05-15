def find_primes(n):
    nums = list(range(n))
    for i in range(2, int(n**0.5 )+ 1):
        badnum = i**2
        while badnum < n:
            nums[badnum] = False
            badnum += i
    return [ i for i in nums if i]
print(find_primes(10))