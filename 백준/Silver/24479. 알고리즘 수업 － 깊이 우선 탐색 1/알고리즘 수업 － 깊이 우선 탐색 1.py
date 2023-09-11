def dfs(v):
    cnt = 0
    need_visit.append(v)
    while need_visit:
        tmp = need_visit.pop()
        if visited[tmp] == 0:
            cnt += 1
            visited[tmp] = cnt
            for i in range(len(graph[tmp])):
                if visited[graph[tmp][i]] == 0:
                    need_visit.append(graph[tmp][i])
    return

import sys
# 입력
n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i] = sorted(graph[i], reverse=True)


need_visit = []
# 방문 체크
visited = [0] * (n+1)
dfs(r)

for i in range(1, n+1):
    print(visited[i])