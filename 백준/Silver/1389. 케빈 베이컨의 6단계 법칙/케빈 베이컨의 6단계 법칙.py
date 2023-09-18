# 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())
friends = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    if b not in friends[a]:
        friends[a].append(b)
        friends[b].append(a)
need_visit = deque()

sm_ls = []
for i in range(1, n+1):
    visited = [0 for _ in range(n + 1)]
    need_visit.append(i)
    visited[i] = 1
    while need_visit:
        tmp = need_visit.popleft()
        for j in friends[tmp]:
            if visited[j] == 0:
                visited[j] = visited[tmp] + 1
                need_visit.append(j)
    sm_ls.append((sum(visited), i))


sm_ls = sorted(sm_ls, key = lambda x : x[1])
sm_ls = sorted(sm_ls, key= lambda x : x[0])


print(sm_ls[0][1])


