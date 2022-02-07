
def binarySearch(array, target):
    return bshelper(array, target, 0, len(array)-1)

def bshelper(array, target, left, right):
    if left > right:
        return -1
    mid = (right + left) >> 1
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return bshelper(array, target, left, mid-1)
    else:
        return bshelper(array, target, mid+1,right)
