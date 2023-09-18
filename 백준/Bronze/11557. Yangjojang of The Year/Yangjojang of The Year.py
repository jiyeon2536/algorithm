# yangjojang of the year
def quickSort(A, left, right):
    if left < right:
        pivot_index = partition(A, left, right)
        quickSort(A, left, pivot_index - 1)
        quickSort(A, pivot_index + 1, right)


def partition(A, left, right):
    i = left
    j = right
    pivot = A[i][1]
    while i <= j:
        while i <= j and A[i][1] <= pivot:
            i += 1
        while i <= j and A[i][1] >= pivot:
            j -= 1
        if i < j :
            A[i], A[j] = A[j], A[i]

    A[left], A[j] = A[j], A[left]
    return j


import sys
input = sys.stdin.readline
t = int(input().strip())
for tc in range(t):
    n = int(input().strip())
    schools = []
    for i in range(n):
        name, bottle = input().strip().split()
        schools.append((name, int(bottle)))

    quickSort(schools, 0, n-1)
    print(schools[-1][0])