# reseto
import sys
n, k = map(int, sys.stdin.readline().strip().split())
a = [i for i in range(2, n+1)]

# k 번째로 지워지는 숫자
cnt = 0

# 이미 지워낸 수를 표시하는 배열
out = []
found = 0
for i in range(len(a)):
    if found == 1:
        break
    if a[i] not in out:
        cnt += 1
    if cnt == k:
        print(a[i])
        break
    j = 2
    while a[i] * j <= n:
        tmp = a[i] * j
        if tmp in out:
            j += 1
            continue
        if tmp not in out:
            out.append(tmp)
            cnt += 1
            j += 1
        if cnt == k:
            found = 1
            print(tmp)
            break
