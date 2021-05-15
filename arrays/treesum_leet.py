
# finds unique 3sums pairs
def threeSum(nums):   
    if len(nums) == 0: return []
    nums.sort()
    seen = {}
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            cursum = nums[i] + nums[j] + nums[k]
            if cursum < 0:
                j +=1
            elif cursum > 0:
                k -=1
            else:
                seen[(nums[i],nums[j],nums[k])] = i
                j +=1
                k -=1

    return [list(key) for key in seen.keys()]