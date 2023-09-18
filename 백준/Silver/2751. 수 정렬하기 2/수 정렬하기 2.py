# # 수 정렬하기 2

def merge(arr, low, high):
    temp = []
    mid = (low + high) // 2
    i, j = low, (mid + 1)

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1
    for k in range(low, high + 1):
        arr[k] = temp[k - low]
    return arr

def mergeSort(arr, low, high):
    if (low >= high):
        return  # base case
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)

    sorted_array = merge(arr, low, high)
    return sorted_array


import sys
n = int(sys.stdin.readline().strip())
nums = []
for i in range(n):
    tmp = int(sys.stdin.readline().strip())
    nums.append(tmp)

mergeSort(nums, 0, n-1)
for i in range(n):
    print(nums[i])
