'''
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''


def rotate(nums,k):
    k = k % len(nums)
    nums = reverse(0, len(nums)-1, nums)
    print(nums,1,k)
    nums = reverse(0, k-1, nums)
    print(nums,2,k)
    nums = reverse(k, len(nums)-1, nums)
    print(nums,3,k)

    return nums
    
def reverse( i, j, nums):
    while i < j:
        # tmp = nums[i]
        # nums[i] = nums[j]
        # nums[j] = tmp
        print(i,j)
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums


print(rotate([1,2,3,4,5,6,7],3))