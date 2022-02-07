def replaceElements(arr):
    
    finMax = arr[-1]
    # for i in range(len(arr) - 2,-1,-1):
    for i in reversed(range(len(arr)-2)):
        temp = arr[i]
        arr[i] = finMax
        finMax = max(finMax,temp)

    print(arr)

   



def replaceElements1(arr):
        n = len(arr)
        max_sofar = arr[-1] # start with the last element
        arr[-1] = -1
        # Greedily replace the current item with the maximum value sofar
        for i in range(n-2,-1,-1): # iterative from right to left
            cur = arr[i]
            arr[i] = max_sofar
            max_sofar = max(max_sofar, cur)
        return arr

print(replaceElements([17,18,5,4,6,1]))
#ans [18,6,6,6,1,-1]