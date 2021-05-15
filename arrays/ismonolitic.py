def isMonolitic(array):
    isDecr = True
    isIncr = True
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            isIncr = False
        if array[i] > array[i-1]:
            isDecr = False
   
    return len(array) if isIncr else 0

print(isMonolitic([0,1,0]))
