def mergeSort(array):
    if len(array) <= 1:
        return array
    auxarr = array[:]
    helper(array, 0, len(array) -1, auxarr)
    return array
	
def helper(array, startIdx, endIdx, auxarr):
	if startIdx == endIdx:
		return
	midIdx = (startIdx + endIdx) // 2	
	helper(auxarr, startIdx, midIdx, array)
	helper(auxarr, midIdx + 1, endIdx, array)	
	doMerge(array, startIdx, midIdx, endIdx, auxarr)

def doMerge(mainarray, startIdx, midIdx,endIdx, auxarr):
	k = startIdx
	i = startIdx
	j = midIdx + 1
	
	while i <= midIdx and j <= endIdx:
		if auxarr[i] <= auxarr[j]:
			mainarray[k] = auxarr[i]
			i +=1
		else:
			mainarray[k] = auxarr[j]
			j +=1
		k += 1 
		
	while i <= midIdx:
		mainarray[k] = auxarr[i]
		i +=1
		k +=1
		
	while j <= endIdx:
		mainarray[k] = auxarr[j]
		j +=1
		k +=1

print(mergeSort([8, 5, 2, 9, 5, 6, 3]))