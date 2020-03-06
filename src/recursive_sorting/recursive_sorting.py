# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Count How Many Combined Elements There Are
    elements = len(arrA) + len(arrB)
    # Make an array of set length (faster to assign values than to continually append items)
    merged_arr = [0] * elements
    # TO-DO

    # Index Holders
    index = 0
    a_index = 0
    b_index = 0

    # While both arrays have elements reassign the lowest value of the 0th index to the index place holder
    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] < arrB[b_index]:
            merged_arr[index] = arrA[a_index]
            index += 1
            a_index += 1
        else:
            merged_arr[index] = arrB[b_index]
            b_index += 1
            index += 1

    # append the remainder of arrA
    while a_index < len(arrA):
        merged_arr[index] = arrA[a_index]
        index += 1
        a_index += 1

    # append the remainder of arrB
    while b_index < len(arrB):
        merged_arr[index] = arrB[b_index]
        index += 1
        b_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    # base case
    if len(arr) > 1:
        middle = len(arr) // 2

        leftArr = merge_sort(arr[:middle])
        rightArr = merge_sort(arr[middle:])

        return merge(leftArr, rightArr)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
