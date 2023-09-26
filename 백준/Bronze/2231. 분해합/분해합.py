# digit generator
import sys
n = int(sys.stdin.readline().strip())

# all the numbers who are smaller than n

mn = float('inf')


for i in range(1, n+1):
    tmp = str(i)
    check = i
    for j in range(len(tmp)):
        check += int(tmp[j])
    if check == n:
        mn = min(mn, i)


if mn == float('inf'):
    print(0)
else:
    print(mn)