# 전쟁 - 전투
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split()) # col, row
colors = [sys.stdin.readline().strip() for _ in range(m)]

# 호수랑 같은 방법
visited = [[0] * n for _ in range(m)]

white = 0  # 힘 누적할 변수
black = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

need_visit = deque()

# bfs 마다 카운트 더해서 끝나면 제곱, 각 팀에 더하기
# white black 따로
for i in range(m):
    for j in range(n):
        if colors[i][j] == 'W' and visited[i][j] == 0:
            cnt = 1
            need_visit.append((i, j))
            visited[i][j] = 1
            while need_visit:
                tmp = need_visit.popleft()
                r = tmp[0]
                c = tmp[1]
                for k in range(4):
                    ni = r + di[k]
                    nj = c + dj[k]
                    if 0 <= ni < m and 0 <= nj < n and colors[ni][nj] == 'W' and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        need_visit.append((ni, nj))
                        cnt += 1
            white += (cnt ** 2)
        elif colors[i][j] == 'B' and visited[i][j] == 0:
            cnt = 1
            need_visit.append((i, j))
            visited[i][j] = 1
            while need_visit:
                tmp = need_visit.popleft()
                r = tmp[0]
                c = tmp[1]
                for k in range(4):
                    ni = r + di[k]
                    nj = c + dj[k]
                    if 0 <= ni < m and 0 <= nj < n and colors[ni][nj] == 'B' and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        need_visit.append((ni, nj))
                        cnt += 1
            black += (cnt ** 2)

print(white, black)





