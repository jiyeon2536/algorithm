# 트리
# 리프노드의 개수
def dfs(v):
    global cnt
    if v == stop:
        return
    visited[v] = True
    child = 0
    for i in graph[v]:
        if visited[i] == False and i != stop:
            dfs(i)
            child += 1
    if child == 0:
        cnt += 1

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
# 루트노드의 부모는 -1
# 부모 노드가 주어진다

graph = [[] for _ in range(n)]

arr = list(map(int, input().split()))
root = 0
visited = [False for _ in range(n)]

for child, parent in enumerate(arr):
    if parent == -1:
        root = child
    graph[parent].append(child)

# 지울 노드
stop = int(input())
cnt = 0

dfs(root)

print(cnt)