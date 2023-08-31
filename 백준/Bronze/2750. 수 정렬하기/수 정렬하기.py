# 수 정렬하기
import sys
n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]

# 버블 정렬 해보자
def bubblesort(a, N):   # 배열, 총 길이
    for j in range(N-1, 0, -1):
        for k in range(N-1):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]


bubblesort(lst, n)

for _ in range(n):
    print(lst[_])

