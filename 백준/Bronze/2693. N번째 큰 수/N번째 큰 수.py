# nth largest value
def quickSort(A, left, right):
    if left < right:
        pivot_index = partition(A, left, right)
        quickSort(A, left, pivot_index - 1)
        quickSort(A, pivot_index + 1, right)

def partition(A, left, right):
    i = left
    j = right
    pivot = A[i]
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[left], A[j] = A[j], A[left]
    return j

import sys
p = int(sys.stdin.readline().strip())
for i in range(p):
    ls = list(map(int, sys.stdin.readline().strip().split()))

    quickSort(ls, 0, 9)
    print(ls[-3])