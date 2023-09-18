# # 수 정렬하기 - 메모리 제한
import sys
n = int(sys.stdin.readline().strip())
nums = dict()
for i in range(n):
    tmp = int(sys.stdin.readline().strip())
    if tmp in nums:
        nums[tmp] += 1
    else:
        nums[tmp] = 1

key_ls = sorted(nums.keys())

for i in key_ls:
    for j in range(nums[i]):
        print(i)












# def quickSort(A, left, right):
#     if left < right:
#         pivot_index = partition(A, left, right)
#         quickSort(A, left, pivot_index - 1)
#         quickSort(A, pivot_index + 1, right)
#
# def partition(A, left, right):
#     i = left
#     j = right
#     pivot = A[i]
#     while i <= j:
#         while i <= j and A[i] <= pivot:
#             i += 1
#         while i <= j and A[j] >= pivot:
#             j -= 1
#         if i < j:
#             A[i], A[j] = A[j], A[i]
#
#     A[left], A[j] = A[j], A[left]
#     return j
#
# import sys
# n = int(sys.stdin.readline().strip())
# ls = []
# for i in range(n):
#     tmp = int(sys.stdin.readline().strip())
#     ls.append(tmp)
#
# quickSort(ls, 0, n-1)
# for i in range(n):
# #     print(ls[i])
# def merge(arr, low, high):
#     temp = []
#     mid = (low + high) // 2
#     i, j = low, mid + 1
#     while i <= mid and j <= high:
#         if arr[i] <= arr[j]:
#             temp.append(arr[i])
#             i += 1
#         else:
#             temp.append(arr[j])
#             j += 1
#
#     while i <= mid:
#         temp.append(arr[i])
#         i += 1
#     while j <= high:
#         temp.append(arr[j])
#         j += 1
#     for k in range(low, high + 1):
#         arr[k] = temp[k - low]
#
#     return arr
#
# def mergeSort(arr, low, high):
#     if (low >= high):
#         return
#     mid = (low + high) // 2
#
#     mergeSort(arr, low, mid)
#     mergeSort(arr, mid + 1, high)
#
#     sorted_array = merge(arr, low, high)
#     return sorted_array
#
#
# import sys
# n = int(sys.stdin.readline().strip())
# ls = []  # 다 받는게 아니라 받고 처리하고 해야함
# for i in range(n):
#     tmp = int(sys.stdin.readline().strip())
#     ls.append(tmp)
#
# mergeSort(ls, 0, n-1)
# for i in range(n):
#     print(ls[i])

