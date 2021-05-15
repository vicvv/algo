def insSort(array):
    for i in range(1,len(array)):
        j = i
        while j < len(array):
            if array[j-1] > array[i]:
                print(array[j-1], array[i])
                swap(j-1, i, array)
            j -=1
    return array
                

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
print(insSort([3,1,5]))