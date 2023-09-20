# catch that cow
def bfs(n):
    if n == k:
        return
    else:
        visited[n] = 1
        need_visit.append(n)
        while need_visit:
            now = need_visit.popleft()
            if now == k:
                return
            for i in range(3):
                if i == 0:
                    nxt = now - 1
                if i == 1:
                    nxt = now + 1
                if i == 2:
                    nxt = now * 2
                if 0 <= nxt <= 100000 and visited[nxt] == 0:
                    visited[nxt] = visited[now] + 1
                    need_visit.append(nxt)


import sys
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split())
need_visit = deque()
visited = [0 for _ in range(100001)]
bfs(n)
if visited[k]:
    print(visited[k] - 1)
else:
    print(visited[k])