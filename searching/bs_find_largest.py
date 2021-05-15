def findLargestNum(nums):
    largest, left, right = nums[0], 0, len(nums) - 1
    while not left > right:
        largest = max(largest, nums[left])
        largest = max(largest, nums[right])
        left +=1
        right -=1
    return largest

print(findLargestNum([3,1,5,2,8,4,12,0,5]))



    # largest, left, right = nums[0], 1, len(nums)-1
    # while left<=right:
    #     if nums[left]>largest:
    #         largest = nums[left]
    #     if nums[right]>largest:
    #         largest = nums[right]
    #     left += 1
    #     right -= 1
    # return largest