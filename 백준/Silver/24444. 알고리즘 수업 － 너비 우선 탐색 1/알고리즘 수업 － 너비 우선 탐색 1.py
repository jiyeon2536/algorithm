# 알고리즘 수업 - 너비 우선 탐색 1
def bfs(v):
    cnt = 1
    visited[v] = cnt    # 첫번째 정점의 방문 체크
    need_visit.append(v)    # 그리고 큐에 넣음
    while need_visit:
        tmp = need_visit.popleft()  # 큐에서 빼고
        for i in graph[tmp]:    # 해당 인접 정점을 순회하면서
           if visited[i] == 0:  # 방문 안했으면
                cnt += 1    # 카운트 넣고
                visited[i] = cnt    # 방문순서를 넣어줌
                need_visit.append(i)   #


import sys
from collections import deque
n, m, r = map(int, sys.stdin.readline().strip().split())  # 정점의 수, 간선의 수, 시작 정점

graph = [[] for _ in range(n+1)]    # 인접 정점 그래프

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])


visited = [0] * (n + 1)    # 해당 인덱스 정점에 방문한 순서 저장할 리스트
need_visit = deque()

bfs(r)

for i in range(1, n+1):
    print(visited[i])