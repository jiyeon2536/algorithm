# ovce
import sys
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def bfs(r, c, visited):
    global total_v
    global total_o

    cnt_v = 0
    cnt_o = 0

    if yard[r][c] == 'v':
        cnt_v += 1
    elif yard[r][c] == 'o':
        cnt_o += 1

    need_visit = [(r, c)]
    visited[r][c] = True

    while need_visit:
        tmp = need_visit.pop(0)
        i = tmp[0]
        j = tmp[1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < m and 0 <= nj < n and yard[ni][nj] != '#' and not visited[ni][nj]:
                visited[ni][nj] = True
                if yard[ni][nj] == 'v':
                    cnt_v += 1
                elif yard[ni][nj] == 'o':
                    cnt_o += 1
                need_visit.append((ni, nj))

    if cnt_v >= cnt_o:
        total_v += cnt_v
    else:
        total_o += cnt_o


m, n = map(int, input().split())  # 가로 세로

yard = [input().rstrip() for _ in range(m)]

visited = [[False] * n for _ in range(m)]
total_v = 0
total_o = 0

for i in range(m):
    for j in range(n):
        if (yard[i][j] == 'v' or yard[i][j] == 'o') and not visited[i][j]:
            bfs(i, j, visited)

print(total_o, total_v)


