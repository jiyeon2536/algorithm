# 바이러스
def bfs(v):
    visited[v] = 1
    need_visit.append(v)
    while need_visit:
        tmp = need_visit.popleft()
        for i in graph[tmp]:
            if visited[i] == 0:
                visited[i] = 1
                need_visit.append(i)


from collections import deque
import sys
n = int(sys.stdin.readline().strip()) # 정점의 수
m = int(sys.stdin.readline().strip()) # 간선의 수

# 연결 그래프 만들기
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

need_visit = deque()
visited = [0] * (n+1)
bfs(1)

print(sum(visited) - 1)