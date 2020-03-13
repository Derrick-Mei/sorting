# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    print(f"arr: {arr}")
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    endIndex = len(arr) - 1

    while endIndex > 1:
        for i in range(endIndex):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        endIndex -= 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    for number in arr:
        if number > maximum:
            maximum = number
        if number < 0:
            return "Error, negative numbers not allowed in Count Sort"

    countingArray = [0] * (maximum+1)

    for number in arr:
        countingArray[number] += 1

    answer = []
    for index, value in enumerate(countingArray):
        answer.extend([index]*value)

    # print(f"answer: {answer}")
    return answer
