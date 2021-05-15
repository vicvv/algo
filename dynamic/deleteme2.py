def largestDivisibleSubset(nums):
    if not nums:
        return nums
    nums.sort()
    dp = [1 for i in range(len(nums))]
    res = []
    for i in range(1, len(nums)):
        for j in range(i):
            
            if nums[i] % nums[j] == 0:
                print(nums[i], nums[j], "--", dp[i],i,dp[i+j],j+1,j)
                #print(i,j, nums[i], nums[j], end = ' ')
                dp[i] = max(dp[i], dp[j] + 1)
                print(dp)
    
    for i in range(1, max(dp) + 1):
        print(dp.index(i))
        res.append(nums[dp.index(i)])
        
    return res
print("result:")
print(largestDivisibleSubset([1,2,3,4,5,7]))