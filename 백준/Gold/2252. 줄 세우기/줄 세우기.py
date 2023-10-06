# 줄 세우기
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]  # adjacency list
d = [0 for _ in range(n+1)]   # in-degree list

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    d[v] += 1

q = deque()
visited = [False for _ in range(n+1)]

for i in range(1, n+1):     # 0인 것 찾기
    if d[i] == 0 and visited[i] == False:
        print(i, end=' ')
        visited[i] = True
        q.append(i)
        while q:
            tmp = q.popleft()
            for nxt in graph[tmp]:
                d[nxt] -= 1
                if d[nxt] <= 0 and visited[nxt] == False:
                    visited[nxt] = True
                    print(nxt, end=' ')
                    q.append(nxt)

