import sys
import heapq
input = sys.stdin.readline

n = int(input())

or_ls = []
res = 0

for i in range(n):
    tmp = int(input())
    heapq.heappush(or_ls, tmp)

while len(or_ls) > 1:
    a = heapq.heappop(or_ls)
    b = heapq.heappop(or_ls)
    res += (a + b)
    heapq.heappush(or_ls, a + b)

print(res)