# 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().rstrip().split())
# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호

# 인접리스트 만들기
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)

# bfs 초기 설정 - 최단거리 쓸거니까 숫자로
visited = [-1 for _ in range(n+1)]

def bfs(v):
    need_visit = deque()
    need_visit.append(v)
    visited[v] += 1
    while need_visit:
        tmp = need_visit.popleft()
        for nxt in graph[tmp]:
            if visited[nxt] == -1:
                visited[nxt] = visited[tmp] + 1
                need_visit.append(nxt)


bfs(x)

# 답 출력
if k not in visited:
    print(-1)

for index, value in enumerate(visited):
    if value == k:
        print(index)