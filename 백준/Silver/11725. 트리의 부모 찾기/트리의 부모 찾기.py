#  트리의 부모 찾기
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            parent[i] = v
            dfs(i)

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

# 인접그래프 만들기
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

dfs(1)

for i in range(2, n+1):
    print(parent[i])