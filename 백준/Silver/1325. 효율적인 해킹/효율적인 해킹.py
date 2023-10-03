# breaking in
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().rstrip().split())
    graph[v].append(u)

need_visit = deque()

for i in range(1, n+1):   # 모든 노드 돌면서
    visited = [False for _ in range(n + 1)]
    need_visit.append(i)
    visited[i] = True
    while need_visit:
        tmp = need_visit.popleft()
        for nxt in graph[tmp]:
            if visited[nxt] == False:
                visited[nxt] = True
                ans[i] += 1
                need_visit.append(nxt)

mx = max(ans)

for i in range(1, n+1):
    if ans[i] == mx:
        print(i, end=' ')