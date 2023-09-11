# DFS 와 BFS
def dfs(p):    # 재귀
    visited[p] = 1
    print(p, end=' ')
    for i in graph[p]:
        if visited[i] == 0:
            dfs(i)


def bfs(p):
    print(p, end=' ')
    visited[p] = 1
    need_visit.append(p)
    while need_visit:
        tmp = need_visit.popleft() # 맨 앞에꺼를 빼서
        for i in graph[tmp]:    # 그 인접 노드를 모두 순회
            if visited[i] == 0:
                visited[i] = 1
                print(i, end=' ')
                need_visit.append(i)


import sys
from collections import deque

n, m, v= map(int, sys.stdin.readline().strip().split()) # 정점, 간선, 탐색시작점

graph = [[] for _ in range(n+1)]

for i in range(m):
    s, e = map(int, sys.stdin.readline().strip().split())
    graph[s].append(e)
    graph[e].append(s)


for i in range(n+1):
    graph[i] = sorted(graph[i])

# 방문 체크 리스트
visited = [0] * (n+1)

need_visit = deque()

dfs(v)
print()
visited = [0] * (n+1)

bfs(v)

