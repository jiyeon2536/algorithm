# A -> B
def bfs(n):
    if n == b:
        return
    else:
        visited[n] = 1
        need_visit.append(n)
        while need_visit:
            now = need_visit.popleft()
            if now == b:
                return
            for i in range(2):
                if i == 0:
                    nxt = now * 2
                elif i == 1:
                    nxt = now * 10 + 1
                if 1 <= nxt <= (10 ** 9) and nxt not in visited:
                    visited[nxt] = visited[now] + 1
                    need_visit.append(nxt)


import sys
from collections import deque
a, b = map(int, sys.stdin.readline().rstrip().split())
need_visit = deque()
visited = dict()
bfs(a)
if b in visited:
    print(visited[b])
else:
    print(-1)