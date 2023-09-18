# 세 수
import sys
a, b, c = map(int, sys.stdin.readline().split())
ls = [a, b, c]

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

quickSort(ls, 0, 2)

print(ls[1])
