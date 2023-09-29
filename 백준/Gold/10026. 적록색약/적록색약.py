# cow art
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp())
painting = [inp().rstrip() for _ in range(n)]

r_ls = []
g_ls = []
b_ls = []

for i in range(n):
    for j in range(n):
        if painting[i][j] == 'R':
            r_ls.append((i, j))
        if painting[i][j] == 'G':
            g_ls.append((i, j))
        if painting[i][j] == 'B':
            b_ls.append((i, j))


# 인간 - rgb 모두 구분
# 소 - r=g

def bfs(ls, target):
    cnt = 0
    need_visit = deque()
    for i, j in ls:
        if visited[i][j] == False:
            visited[i][j] = True
            cnt += 1
            need_visit.append((i, j))
            while need_visit:
                r, c = need_visit.popleft()
                for k in range(4):
                    ni = r + di[k]
                    nj = c + dj[k]
                    if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == False and painting[ni][nj] in target:
                        visited[ni][nj] = True
                        need_visit.append((ni, nj))
    return cnt


# 인간
visited = [[False] * n for _ in range(n)]
r_cnt_h = bfs(r_ls, 'R')
visited = [[False] * n for _ in range(n)]
g_cnt_h = bfs(g_ls, 'G')
visited = [[False] * n for _ in range(n)]
b_cnt_h = bfs(b_ls, 'B')

# 소
visited = [[False] * n for _ in range(n)]
r_cnt_c = bfs(r_ls, 'RG')
g_cnt_c = bfs(g_ls, 'RG')
visited = [[False] * n for _ in range(n)]
b_cnt_c = bfs(b_ls, 'B')


print(r_cnt_h + g_cnt_h + b_cnt_h, r_cnt_c + g_cnt_c + b_cnt_c)