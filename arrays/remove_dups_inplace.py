

def removeDuplicates(nums):
    if len(nums) <=1:
        return len(nums)
    i = 0  #slow-run pointer
    for j in range(1, len(nums)):
        if nums[j] == nums[i]: 
            continue 
        # capture the result
        i += 1
        if i != j:
            nums[i] = nums[j] #in place overriden        
    return nums[:i + 1]
nums = [2,2,3,3]
print(removeDuplicates(nums))


def remove_dups(lst):
  return sorted(set(lst),key=lst.index)


def remove_dups(lst):
  return [x for n,x in enumerate(lst) if x not in lst[:n]]

# below have duplicates but they are not next to each other.
from itertools import *
def unique_in_order(sequence):
	return [k for k, _ in groupby(sequence)]

def unique_in_order(sequence):
	a=[sequence[0]]
	for i in sequence:
		if a[-1]!=i:
			a.append(i)
	return a


def unique_in_order(s):
  return [x for i, x in enumerate(s) if i == 0 or s[i - 1] != s[i]]