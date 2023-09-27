# 촌수 계산
import sys
from collections import deque
n = int(sys.stdin.readline().strip())
a, b = map(int, sys.stdin.readline().strip().split()) # 찾아야하는둘
m = int(sys.stdin.readline().strip())   # 연결 노드개수
family = [[] for _ in range(n + 1)]
for i in range(m):
    p, k = map(int, sys.stdin.readline().strip().split())
    family[p].append(k)
    family[k].append(p)


visited = [0 for _ in range(n+1)]

need_visit = deque()
need_visit.append(a)

visited[a] = 1  # 본인은 0 촌
while need_visit:
    tmp = need_visit.popleft()
    for i in family[tmp]:
        if visited[i] == 0:
            visited[i] = visited[tmp] + 1
            need_visit.append(i)

if visited[b] == 0:
    print(-1)
else:
    print(visited[b] - 1)