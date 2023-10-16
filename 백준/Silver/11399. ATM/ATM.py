# ATM
import sys
input = sys.stdin.readline

n = int(input())
p = sorted(list(map(int, input().split())))

cur = 0
total = 0
for i in range(n):
    cur += p[i]
    total += cur

print(total)