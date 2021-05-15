
def largestDivisibleSubset(nums):
    # If the array is empty just return an empty list
    if not nums:
        return []
    # We first sort the array so that all divisors 
    # of a number are before it.
    nums.sort()
    
    # To store count of divisors of all elements (will make sanse if you try [4, 8, 10, 240]. 
    divCount = [1 for _ in nums]
    
    maxIdx = 0
    # For building largestDivisibleSubset
    sequence = [None for _ in nums]
    # Loop through all elements of list
    for i in range(len(nums)):
        current = nums[i] #Take current number
        #Loop throuh all elements before i
        for j in range(i):
            other = nums[j] #take number before
            if current % other == 0: #Check if they are divisible
                #Just because they are devisible, doesn't mean it's a best solution. 
                # This is where divCount comes to play, we check best possible solution
                if divCount[i] < divCount[j] + 1:
                    divCount[i] = divCount[j] + 1
                    sequence[i] = j
                
        if divCount[i] > divCount[maxIdx]:
            maxIdx = i

    return buildSequence(nums, sequence, maxIdx)

#Simple building sequence..sequence list contains all pointers to previous numbers.. maxIdx is a start
def buildSequence(nums, sequence, idx):
    seq = []
    while idx is not None:
        seq.append(nums[idx])
        idx = sequence[idx]
    return list(reversed(seq))