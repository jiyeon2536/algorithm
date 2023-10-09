import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort(reverse=True)


q = deque()
q.append(r)
visited = [0 for _ in range(n + 1)]
cnt = 1
visited[r] = cnt

while q:
    tmp = q.popleft()
    for nxt in graph[tmp]:
        if visited[nxt] == 0:
            cnt += 1
            visited[nxt] = cnt
            q.append(nxt)

for i in range(1, n + 1):
    print(visited[i])
