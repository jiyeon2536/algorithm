# 수 찾기
import sys
n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().strip().split())))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))


def binarysearch(a, start, end, key):
    middle = (start + end) // 2
    if a[middle] == key:
        print(1)
        return
    elif start >= end:
        print(0)
        return
    else:
        if a[middle] > key:
            end = middle - 1
        elif a[middle] < key:
            start = middle + 1
        return binarysearch(a, start, end, key)


for i in range(m):
    binarysearch(a, 0, n-1, nums[i])
