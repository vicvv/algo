def countPrimes(n):      
    nums = list(range(n))
    for p in range(2, int(n**0.5)+1):
        print("p:",p)
        k = p**2 
        print("k:",k)
        while k < n:
            nums[k] = False
            k+=p
    print(nums)
    return len([i for i in nums[2:] if i != False])
print(countPrimes(10))