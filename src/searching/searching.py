# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for element in arr:
        if element == target:
            return target

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    middle = (low + high) // 2
    if arr[middle] == target:
        return target
    elif target < arr[middle]:
        high = middle - 1
    elif target > arr[middle]:
        low = middle + 1

    return -1  # not found


