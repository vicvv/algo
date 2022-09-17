'''
Given an array of positive integers nums and a positive integer target, return 
the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''


def minSubArrayLen(target,nums):
  minLen, total, start = float('inf'),0,0
  for i in range(len(nums)):
    total +=nums[i]
    while total >= target:
      minLen, total,start = min(minLen, i-start+1),total - nums[start], start + 1
  return 0 if minLen == float('inf') else minLen

print(minSubArrayLen(7,[2,3,1,2,4,3]))